
from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *


url = "https://www.huurzone.nl/huurwoningen/amsterdam?page=1&sort_by=price_asc&autocomplete_identifier=Y2l0eS9hbXN0ZXJkYW0"

example_html = ""


def scrape_website(html):

    soup = BeautifulSoup(html, 'html.parser')
    houses = []

    # Assuming each listing is contained within an 'a' tag with the provided structure
    listings = soup.find_all('a', class_='h-full')

    for listing in listings:
        house = House()

        house.city = 'Amsterdam'

        # Image
        img_tag = listing.find('img')
        if img_tag and 'src' in img_tag.attrs:
            house.images.append(img_tag['src'])

        # Title
        title_tag = listing.find('h2', class_='heading-text')
        if title_tag:
            house.title = title_tag.text.strip()

        # Location
        location_tag = listing.find('p', class_='text-sm')
        if location_tag:
            house.address = location_tag.text.strip()

        # Size & Bedrooms
        size_tags = listing.find_all('p', class_='text-sm')
        if len(size_tags) > 1:
            house.details['Size'] = size_tags[1].text.strip().replace('m<sup>2</sup>', 'm^2')
        if len(size_tags) > 2:
            house.details['Bedrooms'] = size_tags[2].text.strip()

        # Price
        price_tag = listing.find('span', class_='text-xl')
        if price_tag:
            price = get_price(price_tag.text.strip())
            house.price = price

        # URL
        if 'href' in listing.attrs:
            house.link = listing['href']

        houses.append(house)

    return houses



website = Website(url, example_html, scrape_website)




# Run the scrape_example function to test the scraper
# houses = website.scrape_example()


# # Print the results
# for house in houses[::-1]:
#     house.print()
#     print()


