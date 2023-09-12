from bs4 import BeautifulSoup
from classes import House, Website
from common import *

url = "https://koopsmakelaardij.nl/zoeken/huur"

example_html = """
<div class="c-gallery-item js-gallery-item horizontal"><div class="o-media"><a href="/portiekflat-te-huur/amsterdam/haparandadam/11117803.html" class="o-media__link"><div class="o-media__image"><div class="image-wrapper"><img src="https://images.ccid.nl/unsafe/300x200/https://koopsmakelaardij.nl/media/image/original/5cd188673dbcedea.jpg"></div><div class="image-wrapper"><img src="https://images.ccid.nl/unsafe/300x200/https://koopsmakelaardij.nl/media/image/original/04bd6c3937f96f2c.jpg"></div><div class="o-media__image-labels"><span class="o-media__image-label o-media__image-label--0 u-textSmaller u-caps">Nieuw</span><span class="o-media__image-label o-media__image-label--type u-textSmaller u-caps">Huur</span></div></div><div class="flex-combine"><div class="o-media__title"><h4>Amsterdam</h4><p class="u-textSmaller main-properties"><div class="street">Haparandadam</div>3 Kamers<span class="sep"></span> ca. 115 m2</p></div><div class="more-properties"><div>Portiekflat</div><span class="sep"></span><div>Balkon</div><span class="sep"></span><div>Gemeubileerd</div></div><div class="price">€ 3.000,-</div></div></a></div></div>
"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")
    property_elements = soup.find_all("div", class_="o-media")

    house_list = []

    for property_elem in property_elements:
        house = House()

        # Extract city
        city_elem = property_elem.find("h4")
        if city_elem:
            house.city = city_elem.text.strip()

        # Extract address
        address_elem = property_elem.find("div", class_="street")
        if address_elem:
            house.address = address_elem.text.strip()

        # Extract price
        price_elem = property_elem.find("div", class_="price")
        if price_elem:
            house.price = get_price(price_elem.text.strip())

        # Extract details
        details_elem = property_elem.find("p", class_="main-properties")
        if details_elem:
            details_text = details_elem.text.strip()
            details_list = details_text.split(" ")
            if len(details_list) >= 3:
                house.details["Rooms"] = details_list[0]
                house.details["Area"] = details_list[2]

        images_elem = property_elem.find_all("img", src=True)
        for image_elem in images_elem:
            house.images.append(image_elem["src"])

        # Extract link
        link_elem = property_elem.find("a", class_="o-media__link", href=True)
        if link_elem:
            house.link = url + link_elem["href"]

        house_list.append(house)

    return house_list


# Create an instance of the Website class for the second website
website = Website(url, example_html, scrape_website)
