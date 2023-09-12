from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *

import requests

url = "https://www.boelenmakelaardij.nl/huurwoningen/"
base_url = "https://www.boelenmakelaardij.nl"

example_html = """

<div class="col-12 col-lg-6 col-xl-4">
																																			<div class="object object-status-verhuurd object-price- mb-4">
																					<div class="row">
																	<div class="col-12">
																											
										
										<div class="object-image position-relative mb-3">
																					
																							<a href="https://www.boelenmakelaardij.nl/woningen/nassaukade-87-3-amsterdam-9363113121da001119463cb67ffe2e45c259b0/" title="Nassaukade 87 3 Amsterdam Frederik Hendrikbuurt Frederik Hendrikbuurt Noord" class="position-relative text-decoration-none d-block">
																																	<div class="object-image-img">
													
			
			<img data-src="https://images.realworks.nl/servlets/images/media.objectmedia/128964395.jpg?portalid=4286&amp;check=api_sha256%3A361f03b99f1ffbe984339b2813c09a89d3bbb052d85094fd316864b85bba8ff3&amp;=20220809123008&amp;width=720&amp;height=480" class="img-fluid img-cover w-100 lazy loaded" alt="Nassaukade 87 3 Amsterdam Frederik Hendrikbuurt Frederik Hendrikbuurt Noord" loading="lazy" src="https://images.realworks.nl/servlets/images/media.objectmedia/128964395.jpg?portalid=4286&amp;check=api_sha256%3A361f03b99f1ffbe984339b2813c09a89d3bbb052d85094fd316864b85bba8ff3&amp;=20220809123008&amp;width=720&amp;height=480" data-ll-status="loaded">

																			<div class="object-status position-absolute py-2 px-3">
				
				Verhuurd				
				</div>
																</div>
																																											</a>
										
																																<div class="object-favorite object-favorite-add position-absolute" data-favorite-id="432">
												<svg class="position-absolute" viewBox="0 -28 512.001 512" xmlns="http://www.w3.org/2000/svg"><path d="m256 455.515625c-7.289062 0-14.316406-2.640625-19.792969-7.4375-20.683593-18.085937-40.625-35.082031-58.21875-50.074219l-.089843-.078125c-51.582032-43.957031-96.125-81.917969-127.117188-119.3125-34.644531-41.804687-50.78125-81.441406-50.78125-124.742187 0-42.070313 14.425781-80.882813 40.617188-109.292969 26.503906-28.746094 62.871093-44.578125 102.414062-44.578125 29.554688 0 56.621094 9.34375 80.445312 27.769531 12.023438 9.300781 22.921876 20.683594 32.523438 33.960938 9.605469-13.277344 20.5-24.660157 32.527344-33.960938 23.824218-18.425781 50.890625-27.769531 80.445312-27.769531 39.539063 0 75.910156 15.832031 102.414063 44.578125 26.191406 28.410156 40.613281 67.222656 40.613281 109.292969 0 43.300781-16.132812 82.9375-50.777344 124.738281-30.992187 37.398437-75.53125 75.355469-127.105468 119.308594-17.625 15.015625-37.597657 32.039062-58.328126 50.167969-5.472656 4.789062-12.503906 7.429687-19.789062 7.429687zm-112.96875-425.523437c-31.066406 0-59.605469 12.398437-80.367188 34.914062-21.070312 22.855469-32.675781 54.449219-32.675781 88.964844 0 36.417968 13.535157 68.988281 43.882813 105.605468 29.332031 35.394532 72.960937 72.574219 123.476562 115.625l.09375.078126c17.660156 15.050781 37.679688 32.113281 58.515625 50.332031 20.960938-18.253907 41.011719-35.34375 58.707031-50.417969 50.511719-43.050781 94.136719-80.222656 123.46875-115.617188 30.34375-36.617187 43.878907-69.1875 43.878907-105.605468 0-34.515625-11.605469-66.109375-32.675781-88.964844-20.757813-22.515625-49.300782-34.914062-80.363282-34.914062-22.757812 0-43.652344 7.234374-62.101562 21.5-16.441406 12.71875-27.894532 28.796874-34.609375 40.046874-3.453125 5.785157-9.53125 9.238282-16.261719 9.238282s-12.808594-3.453125-16.261719-9.238282c-6.710937-11.25-18.164062-27.328124-34.609375-40.046874-18.449218-14.265626-39.34375-21.5-62.097656-21.5zm0 0"></path></svg>
											</div>
																				</div>

																												</div>
																	<div class="col-12">
																		<div class="object-info">
									
														
					
			<div class="object-address notranslate mb-3">

					
							
						
				<div class="object-address-line">
			
						
				
					
										
							<span class="object-street">Nassaukade</span>
				
						
												
								
																			
										<span class="object-housenumber">87</span>
							
									
									
																
											<span class="object-housenumber-addition">3</span>

																
									
													
							
					
							
						
				</div>
			
						
						
				
									
						<div class="object-address-line">
				
									
										
										
							<span class="object-place">Amsterdam</span>
				
										
										
										
										
							<span class="object-neighbourhood">Frederik Hendrikbuurt</span>
				
										
										
							<span class="object-neighbourhood">Frederik Hendrikbuurt Noord</span>
				
										
									
									
						</div>
				
					
							
						
							
		
			</div>

				
		
											
																																								<div class="object-features mb-3">
											
																								
	
	
	
	
	
	
	
	
	
					
				<div class="object-feature object-feature-woonhuissoort ">
				
					<div class="row">
				
						<div class="col-5">
				
							<div class="object-feature-title text-truncate">
				
							Soort woonhuis				
							</div>
				
						</div>
				
						<div class="col-7">
				
							<div class="object-feature-info text-truncate">
				
								Appartement, bovenwoning 				
							</div>
				
						</div>
				
					</div>
				
				</div>
				
				
	
	
	
	
					
				<div class="object-feature object-feature-bouwjaar ">
				
					<div class="row">
				
						<div class="col-5">
				
							<div class="object-feature-title text-truncate">
				
							Bouwjaar				
							</div>
				
						</div>
				
						<div class="col-7">
				
							<div class="object-feature-info text-truncate">
				
								1887 				
							</div>
				
						</div>
				
					</div>
				
				</div>
				
				
	
	
	
	
					
				<div class="object-feature object-feature-woonoppervlakte ">
				
					<div class="row">
				
						<div class="col-5">
				
							<div class="object-feature-title text-truncate">
				
							Woonopp.				
							</div>
				
						</div>
				
						<div class="col-7">
				
							<div class="object-feature-info text-truncate">
				
								76 m²				
							</div>
				
						</div>
				
					</div>
				
				</div>
				
				
	
	
	
	
	
	
					
				<div class="object-feature object-feature-inhoud ">
				
					<div class="row">
				
						<div class="col-5">
				
							<div class="object-feature-title text-truncate">
				
							Inhoud				
							</div>
				
						</div>
				
						<div class="col-7">
				
							<div class="object-feature-info text-truncate">
				
								225 m³				
							</div>
				
						</div>
				
					</div>
				
				</div>
				
				
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
					
				<div class="object-feature object-feature-aantalkamers ">
				
					<div class="row">
				
						<div class="col-5">
				
							<div class="object-feature-title text-truncate">
				
							Aantal kamers				
							</div>
				
						</div>
				
						<div class="col-7">
				
							<div class="object-feature-info text-truncate">
				
								3 kamers (2 slaapkamers) 				
							</div>
				
						</div>
				
					</div>
				
				</div>
				
				
	
	
	
	
	
		
	
	
	
	
			
			
	
	
	
	
	
	
	
	
	
	
	
											</div>
																																								</div>
									</div>
								</div>
							</div>
						</div>

"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all("div", class_="object")

    for article in articles:
        house = House()

        # Link
        link_container = article.find("a")
        if link_container:
            house.link = link_container["href"]

        # Images
        image_container = article.find("img")
        if image_container:
            house.images.append(image_container["data-src"])

        # Address
        address_container = article.find("div", class_="object-address-line")
        if address_container:
            house.address = address_container.text.strip().replace("\n", " ")

        # City
        city_container = article.find("span", class_="object-place")
        if city_container:
            house.city = city_container.text.strip()

        # Price
        price_container = article.find("div", class_="object-price")
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Let's scrape the link to get more details
        # We want to know the price (huurprijs), we need to extract if from the text
        response = requests.get(
            house.link,
            headers={
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
            },
        )
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, "html.parser")

        description_container = soup.find_all("div", class_="object-detail-description")
        for d in description_container:
            description = d.text.strip().split("€")[1]
            price = get_price(description)
            if price > 0 and price < 10000:
                house.price = get_price(description)
                break

        # Details
        details_container = article.find_all(
            "div", class_="object-feature-info text-truncate"
        )
        try:
            house.details["m2"] = details_container[2].text.strip()
            house.details["kamers"] = details_container[5].text.strip()
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
