

from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *


base_url = "https://cityhomes.nl"
url = "https://cityhomes.nl/woningen?city=amsterdam"

example_html = """
<div data-v-262f37a9="" class="col_4"><a data-v-262f37a9="" class="property_single_link"><div class="property_single"><img src="https://cityhomes.ams3.cdn.digitaloceanspaces.com/d824a21e_251b_45ba_890d_83fc7b3f95b9_df93e637c7.jpg" class="img_property img_responsive"><div class="property_meta"><div class="property_name_wrapper"><h2 class="property_name">Amsterdam</h2><!----></div><p class="property_location">Van Tuyll Van Serooskerkenweg (Stadionbuurt)</p><p class="price">€2200 per maand excl.</p><ul class="prop_facility"><li><img src="https://cityhomes.nl/_nuxt/icon-space.a1d7b45a.svg" class="icon_prop"> 65m<sup>2</sup></li><li><img src="https://cityhomes.nl/_nuxt/icon-bedrooms.c0459b76.svg" class="icon_prop">1 slaapkamer </li><li><img src="https://cityhomes.nl/_nuxt/icon-furniture.7aae40e1.svg" class="icon_prop"> Gestoffeerd</li></ul></div></div></a></div>
"""

def scrape_website(html):
    soup = BeautifulSoup(html, 'html.parser')

    houses = []

    articles = soup.find_all('a', class_='property_single_link')

    for article in articles:

        house = House()

        house.link = 'https://cityhomes.nl/woningen'

        # Image
        img_tag = article.find('img')
        if img_tag and 'src' in img_tag.attrs:
            house.images.append(img_tag['src'])


        # Address and City
        address_container = article.find('h2', class_='property_name')
        city_container = article.find('p', class_='property_location')
        if address_container and city_container:
            house.city = address_container.text.strip()
            house.address = city_container.text.strip()

        # Price
        price_container = article.find('p', class_='price')
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Additional Details
        details_container = article.find_all('li')
        for detail in details_container:
            label = detail.find('img')
            if label:
                label = label['src'].split('/')[-1].split('.')[0].split('-')[-1].capitalize()
                value = detail.text.strip()
                house.details[label] = value

        houses.append(house)

    return houses


website = Website(url, example_html, scrape_website)



# Run the scrape_example function to test the scraper
# houses = website.scrape_example()


# # # Print the results
# for house in houses[::-1]:
#     house.print()
#     print()


