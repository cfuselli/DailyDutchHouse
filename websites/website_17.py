from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *


base_url = "https://www.vva.amsterdam"
url = "https://www.vva.amsterdam/woningaanbod/huur/amsterdam?availability=1&locationofinterest=Amsterdam&moveunavailablelistingstothebottom=true&orderby=9"

example_html = """

<article class="objectcontainer col-12 col-xs-12 col-sm-6 col-md-6 col-lg-4">
        <div class="object   ">
            <div class="object_status_container">
                        <span class="object_status new_forrent">
                            Nieuw in verhuur
                        </span>
            </div>
            <a class="img-container" href="/woningaanbod/huur/amsterdam/sint-willibrordusstraat/58-g-ref-01541?availability=1&amp;countryid=1&amp;forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;moveunavailablelistingstothebottom=true&amp;orderby=9&amp;take=12">
                <div class="datashort">
                    <span class="street">Sint Willibrordusstraat 58g</span>
                        <span class="location">Amsterdam</span>
                                                <span class="obj_price">
                                € 1.750,- /mnd
                            </span>
                </div>

                <div class="content">
                    <img width="350" alt="Te huur: Sint Willibrordusstraat 58g, 1073VD Amsterdam" class="img-responsive object_image_srcset img-fluid" loading="lazy" srcset="https://haywebattachments.blob.core.windows.net/public/2291/2951866/87134905/$m/3529313.1479138523-629.jpg 600w,
                            https://haywebattachments.blob.core.windows.net/public/2291/2951866/87134905/$s/3529313.1479138523-629.jpg 300w" sizes="auto" src="https://haywebattachments.blob.core.windows.net/public/2291/2951866/87134905/$s/3529313.1479138523-629.jpg">
                </div>
            </a>

            <div class="data">
                <div class="stats">
                        <a class="item photos" href="/woningaanbod/huur/amsterdam/sint-willibrordusstraat/58-g-ref-01541?availability=1&amp;countryid=1&amp;forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;moveunavailablelistingstothebottom=true&amp;orderby=9&amp;take=12">
                            <i class="fal fa-image" aria-hidden="true"></i>19
                        </a>
                                                                                                                                        </div>
                <h3 class="obj_address">
                    <a href="/woningaanbod/huur/amsterdam/sint-willibrordusstraat/58-g-ref-01541?availability=1&amp;countryid=1&amp;forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;moveunavailablelistingstothebottom=true&amp;orderby=9&amp;take=12">
                        <span class="street">Sint Willibrordusstraat 58g</span>
                            <span class="zipcode">1073VD</span>
                                                    <span class="locality">Amsterdam</span>
                    </a>
                </h3>
                <a class="saletitle" href="/woningaanbod/huur/amsterdam/sint-willibrordusstraat/58-g-ref-01541?availability=1&amp;countryid=1&amp;forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;moveunavailablelistingstothebottom=true&amp;orderby=9&amp;take=12">
                </a>
                <a class="object_data_labels" href="/woningaanbod/huur/amsterdam/sint-willibrordusstraat/58-g-ref-01541?availability=1&amp;countryid=1&amp;forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;moveunavailablelistingstothebottom=true&amp;orderby=9&amp;take=12">
                        <span class="object_label object_rooms">
                            <span class="number">3</span>
                            <i class="fa fa-clone" aria-hidden="true"></i>
                            <span class="text">kamers</span>
                        </span>

                        <span class="object_label object_bed_rooms">
                            <span class="number">2</span>
                            <i class="fa fa-bed" aria-hidden="true"></i>
                            <span class="text">slaapkamers</span>
                        </span>
                                            <span class="object_label object_bath_rooms">
                            <span class="number">1</span>
                            <i class="fa fa-bath" aria-hidden="true"></i>
                            <span class="text">Badkamer</span>
                        </span>

                        <span class="object_label object_sqfeet">
                            <span class="number">60 m²</span>
                            <span class="text">Woonopp.</span>
                        </span>






                        <span class="object_label object_sqfeet">
                            <span class="number">60 m²</span>
                            <span class="text">Perceelopp.</span>
                        </span>
                                                            
                        <span class="object_label object_fitment_furnished">
                            <i class="fa fa-loveseat" aria-hidden="true"></i>
                            <span class="text">Gemeubileerd</span>
                        </span>
                    
                </a>
                <a class="obj_price" href="/woningaanbod/huur/amsterdam/sint-willibrordusstraat/58-g-ref-01541?availability=1&amp;countryid=1&amp;forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;moveunavailablelistingstothebottom=true&amp;orderby=9&amp;take=12">
                            <span class="obj_price">
                                € 1.750,- /mnd
                            </span>
                </a>
            </div>
        </div>
    </article>

"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all(
        "article", class_="objectcontainer col-12 col-xs-12 col-sm-6 col-md-6 col-lg-4"
    )

    for article in articles:
        house = House()

        # Link
        link_tag = article.find("a", class_="img-container")
        if link_tag:
            house.link = base_url + link_tag["href"]

        # Find images
        img_tags = article.find_all("img")
        for img_tag in img_tags:
            house.images.append(img_tag["src"])

        # Address
        address_container = article.find("span", class_="street")
        if address_container:
            house.address = address_container.text.strip()

        # Address and City
        address_container = article.find("span", class_="locality")
        if address_container:
            house.city = address_container.text.strip()

        # Price
        price_container = article.find(class_="obj_price")
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Additional Details
        details_container = article.find_all("a", class_="object_data_labels")
        for detail in details_container:
            labels = detail.find_all("span", class_="object_label")
            for label in labels:
                label = label.find_all("span")
                try:
                    key = label[0].text.strip()
                    value = label[1].text.strip()
                    house.details[key] = value[:50]
                except:
                    pass

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
