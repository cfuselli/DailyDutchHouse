from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *

url = "https://househunting.nl/woningaanbod/?type=for-rent&filter_location=Amsterdam&lat=52.3675734&lng=4.9041389&street=&km=5&min-price=&max-price="
base_url = "https://househunting.nl"
example_html = ""


# Function to extract information from the HTML
def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")
    house_elements = soup.find_all("li", class_="location")

    houses = []
    for house_element in house_elements:
        house = House()

        # Extract image URL
        img_elem = house_element.find("img", class_="location_image")
        if img_elem and "src" in img_elem.attrs:
            house.images = [
                img_elem["src"],
            ]

        # Extract street and city
        street_elem = house_element.find("h3", class_="location_street")
        city_elem = house_element.find("p", class_="location_city")
        if street_elem:
            house.address = street_elem.text.strip()
        if city_elem:
            house.city = city_elem.text.strip()

        # Extract price
        price_elem = house_element.find("p", class_="location_price")
        if price_elem:
            house.price = get_price(price_elem.text.strip())

        # Extract link
        link_elem = house_element.find("a", href=True)
        if link_elem:
            house.link = link_elem["href"]

        houses.append(house)

    return houses


website = Website(url, example_html, scrape_website)

# Run the scrape_example function to test the scraper
houses = website.scrape_example()

# Print the results
for house in houses[::-1]:
    house.print()
    print()
