from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *


base_url = "https://kamernet.nl"
url = "https://kamernet.nl/en/for-rent/apartment-amsterdam?radius=5&minSize=&maxRent=17"

example_html = """
<div class="rowSearchResultRoom col s12 m6 l4">
    <div class="tile-wrapper ka-tile" id="https://kamernet.nl/en/for-rent/apartment-amsterdam/groenlandstraat/apartment-2168185" accessdirectly="true" href="https://kamernet.nl/en/for-rent/apartment-amsterdam/groenlandstraat/apartment-2168185" data-roomid="2168185" onclick="goToRoomDetails(event,'https://kamernet.nl/en/for-rent/apartment-amsterdam/groenlandstraat/apartment-2168185','_blank'); sendClickTilesListingMPEvent()" itemscope="" itemtype="https://schema.org/Residence">
        <div class="col s12 no-padding">


            <div class="tile-img">          
                <a href="https://kamernet.nl/en/for-rent/apartment-amsterdam/groenlandstraat/apartment-2168185">
<div class="kamernet-bluegreen tile-new-advert"><span class="white-text align-center-all">New!</span></div>                    <img class=" lazyloaded" src="https://resources.kamernet.nl/image/870160ba-da61-4aa9-a9b9-4d0337bdb2c3/resize/680-452" data-src="https://resources.kamernet.nl/image/870160ba-da61-4aa9-a9b9-4d0337bdb2c3/resize/680-452" alt="Kamer in Amsterdam, Groenlandstraat op Kamernet.nl: Furnished Apartment with Garden">
                </a>
                <div class="mdi-action-favorite-outline white-text tile-favorite stop-navigation" onclick="DisplayRoomSetFavorite(2168185, this)"></div>

                <div class="tile-special">

                </div>
            </div>


            <div class="tile-data" itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress">
                    <meta itemprop="postalCode" content="1060MG">
                <a href="https://kamernet.nl/en/for-rent/apartment-amsterdam/groenlandstraat/apartment-2168185" class="tile-title truncate">Groenlandstraat</a>
                <div class="tile-city">Amsterdam</div>
                <div class="tile-room-type">
                    <span> -</span> Apartment
                </div>
                    <div class="tile-bedroom-numbers">
                        <span> -</span> 1 bedroom                    </div>
                <div class="tile-details">
                    <div class="tile-rent">
                        € 1475,-
                        <span>
Utilities incl.                        </span>
                    </div>
                    <div class="tile-surface">50 <span>m<sup>2</sup></span></div>
                    <div class="tile-furnished">Furnished</div>
                </div>
                <div class="tile-availability">
                    <div class="left">
                        <i class="fa fa-calendar" aria-hidden="true"></i>
                        12-09-'23 -
12-09-'24                    </div>
                    <div class="right tile-dateplaced">
                        New!
                    </div>
                </div>
            </div>
        </div>
        <meta itemprop="image" content="https://resources.kamernet.nl/image/99d3967d-00d8-4065-909f-f3416e9b7383">
        <meta itemprop="url" content="https://kamernet.nl/en/for-rent/apartment-amsterdam/groenlandstraat/apartment-2168185">
            <div itemprop="geo" itemscope="" itemtype="http://schema.org/GeoCoordinates">
                <meta itemprop="latitude" content="52.3469560000">
                <meta itemprop="longitude" content="4.7926610000">
            </div>
    </div>
</div>"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all("div", class_="rowSearchResultRoom col s12 m6 l4")

    for article in articles:
        house = House()

        # Link
        link_tag = article.find("a", class_="tile-title truncate")
        if link_tag:
            house.link = link_tag["href"]

        # Find images
        img_tags = article.find_all("img")
        for img_tag in img_tags:
            house.images.append(img_tag["data-src"])

        # Address
        address_container = article.find("a", class_="tile-title truncate")
        if address_container:
            house.address = address_container.text.strip()

        # Address and City
        address_container = article.find("div", class_="tile-city")
        if address_container:
            house.city = address_container.text.strip()

        # Price
        price_container = article.find(class_="tile-rent")
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Additional Details
        details_container = article.find_all("div", class_="tile-details")
        for detail in details_container:
            label = detail.find("div", class_="tile-surface")
            if label:
                label = label.text.strip()
                value = detail.find("div", class_="tile-furnished").text.strip()
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
