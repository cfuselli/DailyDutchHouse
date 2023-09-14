from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *

import requests

url = (
    "https://huismanmakelaardij.nl/ons-aanbod?types=Huur&filter_order=desc&filter=price"
)
base_url = "https://huismanmakelaardij.nl/"

example_html = """


<div class="property span12">
                                <div class="row">
                                    <div class="image span3">
                                        <div class="content">
                                                                                        <a href="https://huismanmakelaardij.nl/ons-aanbod/overtoom-186-2" alt="overtoom 186-2"></a>
                                            <img src="https://huismanmakelaardij.nl/timthumb.php?src=https://huismanmakelaardij.nl/uploads/building/overtoom-186-2.jpg&amp;w=270&amp;h=200" alt="overtoom 186-2">
                                                                                                                                            <div class="sold">Verhuurd</div>
                                                                                            
                                        </div>
                                    </div>

                                    <div class="body span9">
                                        <div class="title-price row">
                                            <div class="title span4">
                                                <h2>
                                                    <a href="https://huismanmakelaardij.nl/ons-aanbod/overtoom-186-2">overtoom 186-2</a>
                                                </h2>
                                            </div>

                                                                                        <div class="price">
                                                € 2.350 p.m.                                            </div>
                                                                                    </div>

                                        <div class="location">Amsterdam</div>
                                                                                <div class="area">
                                            <span class="key">Soort woning:</span>
                                            <span class="value">
                                                Vrijstaand                                            </span>
                                        </div>
                                        <div class="area">
                                            <span class="key">Woonoppervlak:</span>
                                            <span class="value">
                                                74 m <sup>2</sup>
                                            </span>
                                        </div>
                                        <div class="area">
                                            <span class="key">Aantal kamers:</span>
                                            <span class="value">
                                                3                                            </span>
                                        </div>
                                        <div class="area">
                                            <span class="key">Aantal slaapkamers:</span>
                                            <span class="value">
                                                2                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>


"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all(class_="property")

    for article in articles:
        house = House()

        # Link
        link_container = article.find("a")
        if link_container:
            house.link = link_container["href"]

        # Images
        image_container = article.find("img")
        if image_container:
            try:
                house.images.append(
                    image_container["src"].split("src=")[1].split("&")[0]
                )
            except:
                pass

        # Address
        address_container = article.find("h2")
        if address_container:
            house.address = address_container.text.strip()

        # City
        city_container = article.find("div", class_="location")
        if city_container:
            house.city = city_container.text.strip()

        # Price
        price_container = article.find("div", class_="price")
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Details
        details_container = article.find_all("div", class_="area")
        try:
            house.details["m2"] = (
                details_container[1]
                .text.strip()
                .replace(" ", "")
                .replace("\n", "")
                .replace("\r", " ")
            )

            house.details["kamers"] = (
                details_container[2]
                .text.strip()
                .replace(" ", "")
                .replace("\n", "")
                .replace("\r", " ")
            )

            house.details["slaapkamers"] = (
                details_container[3]
                .text.strip()
                .replace(" ", "")
                .replace("\n", "")
                .replace("\r", " ")
            )

        except:
            pass

        print(house.details)

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
