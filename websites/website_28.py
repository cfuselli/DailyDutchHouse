from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *

import requests

url = "https://www.principleproperties.nl/huurwoningen/?filter-sort-by=published&filter-sort-order="
base_url = "https://www.principleproperties.nl"

example_html = """



<article class="property-row post-12128420 property type-property status-publish has-post-thumbnail hentry amenities-geen-dieren amenities-gratis-parkereen amenities-inductie-fornuis amenities-laminaat amenities-magnetron amenities-open-keuken amenities-oven amenities-sharers amenities-shower amenities-vaatwasser amenities-wash-basin amenities-wasmachine locations-de-zetter locations-guisveld locations-wormerveer property_types-appartement availabilities-2020-06-01">
	<a href="https://www.principleproperties.nl/huurwoningen/wormerveer/guisveld/de-zetter/12128420/id-463110/" class="property-row-image">
        						                        <div class="badge-div">
            
            
            
            
        </div>
		
					<img width="400" height="300" src="https://www.principleproperties.nl/wp-content/uploads/2020/09/198356-400x300.jpg" class="attachment-property-row-thumbnail size-property-row-thumbnail wp-post-image" alt="" srcset="https://www.principleproperties.nl/wp-content/uploads/2020/09/198356-400x300.jpg 400w, https://www.principleproperties.nl/wp-content/uploads/2020/09/198356-300x225.jpg 300w, https://www.principleproperties.nl/wp-content/uploads/2020/09/198356.jpg 1000w" sizes="(max-width: 400px) 100vw, 400px">			</a><!-- /.property-row-image -->

	<div class="property-row-content">
		<div class="property-row-content-inner">
			<div class="property-row-main">
				<h2 class="property-row-title entry-title">
					<a href="https://www.principleproperties.nl/huurwoningen/wormerveer/guisveld/de-zetter/12128420/id-463110/">De Zetter</a>
				</h2>

													<div class="property-row-location">
						<a href="https://www.principleproperties.nl/huurwoningen/wormerveer/">Wormerveer</a> <span class="separator">/</span> <a href="https://www.principleproperties.nl/huurwoningen/wormerveer/guisveld/">Guisveld</a> <span class="separator">/</span> <a href="https://www.principleproperties.nl/huurwoningen/wormerveer/guisveld/de-zetter/">De Zetter</a>					</div>
				
				<div class="property-row-body">
					<p></p><p>Appartement te huur aan de&nbsp;De Zetter&nbsp;in&nbsp;Wormerveer Een zorgvuldig geselecteerde huurwoning in&nbsp;Wormerveer. Een 2 slaapkamer&nbsp;appartement(volledig gemeubileerd ) van ongeveer&nbsp;75 m2 gelegen aan de&nbsp;De</p>
<p></p>
				</div><!-- /.property-row-body -->
			</div><!-- /.property-row-main -->

																		
							<div class="property-row-meta">
				<a href="https://www.principleproperties.nl/huurwoningen/wormerveer/guisveld/de-zetter/12128420/id-463110/">
											<span class="property-row-meta-item property-row-meta-item-price">
							<span>Price:</span>
							<strong>€ 1,250</strong>
						</span><!-- /.property-box-meta-item -->
																<span class="property-row-meta-item property-row-meta-item-beds">
							<span>Bedroom:</span>
							<strong>2</strong>
						</span><!-- /.property-box-meta-item -->
					
											<span class="property-row-meta-item property-row-meta-item-area">
							<strong>75 m2</strong>
						</span><!-- /.property-box-meta-item -->
					

						                  	                	<span class="property-row-meta-item property-row-meta-item-area">
	                    	<span>Available per</span><strong>Sep 2023</strong>
	                    </span>
	                				</a>
				</div><!-- /.property-row-meta -->
					</div><!-- /.property-row-content-inner -->
	</div><!-- /.property-row-content -->
</article>




"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all(class_="property-row")

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
        address_container = article.find("h2")
        if address_container:
            house.address = address_container.text.strip()

        # City
        city_container = article.find(class_="property-row-location")
        if city_container:
            house.city = city_container.text.strip().split("/")[0]

        # Price
        price_container = article.find(class_="property-row-meta-item-price")
        if price_container:
            house.price = get_price(price_container.text.strip(), keep_comma=True)

        # Details
        details_container = article.find_all("strong")
        try:
            house.details["m2"] = details_container[1].text.strip()
            house.details["kamers"] = details_container[0].text.strip()
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
