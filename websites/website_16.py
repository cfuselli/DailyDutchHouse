from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *


base_url = "https://www.vbo.nl"
url = "https://www.vbo.nl/huurwoningen?q=Amsterdam&straal=&huurprijs_van=&huurprijs_tot=3000"

example_html = """

<div class="col-12 col-sm-6 col-lg-4">
                <a href="https://www.vbo.nl/huurwoningen/amsterdam/woning-480180-professor-jh-gunningstraat-81" class="propertyLink">
    <figure class="property">
                    <img src="https://d1zsattj8yq64o.cloudfront.net/media/15495472/424x318_crop.jpg" alt="Professor J.H. Gunningstraat 81">
                <div class="label">nieuw</div>
        <figcaption>
            <span class="street">Professor J.H. Gunningstraat 81</span><br>
            <span class="city">
                Amsterdam            </span><br>
            <span class="price">€ 3.000,- p/m</span>
                            <span class="energielabel energy-A">A</span>
                        <div class="bottom d-none d-md-block">
                <ul>
                                                                        <li>Bovenwoning</li>
                                                                            <li>Woonoppervlakte: 110 m²</li>
                                                                            <li>Aantal kamers: 3</li>
                                                                </ul>
            </div>
            <div class="broker d-none d-md-block">
                +31 Vastgoed
            </div>
        </figcaption>
    </figure>
</a>
            </div>

"""

def scrape_website(html):

    soup = BeautifulSoup(html, 'html.parser')

    houses = []

    articles = soup.find_all('div', class_='col-12 col-sm-6 col-lg-4')

    for article in articles:

        house = House()

        # Link
        link_tag = article.find('a', class_='propertyLink')
        if link_tag:
            house.link = link_tag['href']


        # Find images
        img_tags = article.find_all('img')
        for img_tag in img_tags:
            house.images.append(img_tag['src'])


        # Address
        address_container = article.find('span', class_='street')
        if address_container:
            house.address = address_container.text.strip()

        # Address and City
        address_container = article.find('span', class_='city')
        if address_container:
            house.city = address_container.text.strip()

        # Price
        price_container = article.find(class_='price')
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Additional Details
        details_container = article.find('div', class_='bottom d-none d-md-block')
        if details_container:
            details_container = details_container.find_all('li')
            for detail in details_container:
                if detail:
                    label = detail.text.strip().split(':')[0]
                    try:
                        value = detail.text.strip().split(':')[1]
                    except:
                        value = ''
                    house.details[label] = value[:50]


        if house.price != None:
            if house.price < 10000:

                houses.append(house)

    return houses


website = Website(url, example_html, scrape_website)



# Run the scrape_example function to test the scraper
# houses = website.scrape_example()


# # # Print the results
# for house in houses[::-1]:
#     house.print()
#     print()


