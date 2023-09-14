from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *

import requests

url = "https://haagen-partners.nl/woningen/#q1YqLkksKS1WslJKSi1OzsjMTkpMLFLSUcovSkktSqoEimfn5xcUFGVmFVslFifrZJSWFsF5SrUA"
base_url = "https://haagen-partners.nl"

example_html = """


<div class="woning-card post-8728 venum_wonen type-venum_wonen status-publish has-post-thumbnail hentry">
	<a href="https://haagen-partners.nl/woning/amsterdam-schoolstraat-2-c/">
		<div class="inner">
			<div class="image-container">
				<div class="prijs">
					€ 2.100,-				</div>
				
				<div class="thumbnail">
					<img width="640" height="427" src="https://haagen-partners.nl/wp-content/uploads/venum/wonen/5.421.141/pub-a42b9bbc-2498-4a9e-85ef-1d4ac3d46dd3-l-9.jpg" class="attachment-large size-large wp-post-image" alt="" decoding="async" srcset="https://haagen-partners.nl/wp-content/uploads/venum/wonen/5.421.141/pub-a42b9bbc-2498-4a9e-85ef-1d4ac3d46dd3-l-9.jpg 1024w, https://haagen-partners.nl/wp-content/uploads/venum/wonen/5.421.141/pub-a42b9bbc-2498-4a9e-85ef-1d4ac3d46dd3-l-9-480x320.jpg 480w, https://haagen-partners.nl/wp-content/uploads/venum/wonen/5.421.141/pub-a42b9bbc-2498-4a9e-85ef-1d4ac3d46dd3-l-9-768x512.jpg 768w" sizes="(max-width: 640px) 100vw, 640px">
					<div class="woning-status">
						<span>Beschikbaar</span>
					</div>
				</div>
			</div>

			<div class="item-content">
				<div class="item-header">
											<h3>
							<span class="straat">Schoolstraat</span>							<span class="plaats">Amsterdam</span>	
						</h3>
					
											<span class="wijk"></span>
									</div>

				<div class="item-misc">
					<span class="slaapk"><i class="fas fa-bed"></i>Slaapkamers 1</span>					<span class="badk"><i class="fas fa-bath"></i>Badkamers 1</span>									</div>
			</div>
		</div>
	</a>
</div>



"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all(class_="woning-card")

    for article in articles:
        house = House()

        # Link
        link_container = article.find("a", href=True)
        if link_container:
            house.link = link_container["href"]

        # Images
        image_container = article.find("img")
        if image_container:
            house.images.append(image_container["src"])

        # Address
        address_container = article.find("h3")
        if address_container:
            house.address = address_container.text.strip()

        # City
        city_container = article.find("span", class_="plaats")
        if city_container:
            house.city = city_container.text.strip()

        # Price
        price_container = article.find("div", class_="prijs")
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Details
        details_container = article.find(class_="item-misc")
        try:
            house.details["m2"] = details_container.find_all("span")[0].text.strip()
            house.details["kamers"] = details_container.find_all("span")[1].text.strip()

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
