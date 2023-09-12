from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *


url = "https://www.hoenmakelaars.nl/huurwoningen?plaats=AMSTERDAM&objectType=huurwoning&prijsMaximum="
base_url = "https://www.hoenmakelaars.nl"

example_html = """

<div class="card shadow bg-white rounded-lg">
                        <a href="/huurwoningen/spiegelgracht-21-iii">
						<div class="card-img-caption">
							<h3 class="card-text">Spiegelgracht 21III<br>1017 JP AMSTERDAM</h3>
							
                            <img src="/fotos/771_foto1_object_big.jpg" class="card-img-top" alt="Spiegelgracht 21 III">
                            
							<div class="card-overlay"></div>							
						</div>
						<div class="card-body">
							<div class="row">
								<div class="col-9">
									<p class="card-text">&nbsp;<br>80 m<sup>2</sup>  |  3 kamers<br><span class="text-blue ">€ 3.500,- per maand</span></p>
								</div>
								<div class="col-3 text-right align-self-end">
									<img src="img/btn_arrow_right.svg" alt="Bekijken">
								</div>
							</div>
						</div>
                        </a>    
					</div>

"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all("div", class_="card shadow bg-white rounded-lg")

    for article in articles:
        # Do the entire scraping here
        house = House()

        # Link
        link_container = article.find("a")
        if link_container:
            house.link = base_url + link_container["href"]

        # Images
        image_container = article.find("img")
        if image_container:
            house.images.append(base_url + image_container["src"])

        # Address: get text from address_container, before the <br>
        address_container = article.find("h3", class_="card-text")

        for br in address_container.find_all("br"):
            br.replace_with("||")
        address, city = address_container.text.split("||")
        house.address = address.strip()
        house.city = city.strip()

        # Details
        details_container = article.find("p", class_="card-text")
        for br in details_container.find_all("br"):
            br.replace_with("||")

        details_container = details_container.text.split("||")
        try:
            house.details["m2"] = details_container[1]
            house.price = get_price(details_container[2])
        except:
            print("Error in details_container", details_container)
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
