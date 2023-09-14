from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *

import requests

url = "https://www.isaak.nl/aanbod/woningaanbod/huur/"
base_url = "https://www.isaak.nl"

example_html = """

<li class="al2woning aanbodEntry even">			<div class="vakfoto" id="generated_id159_29926993"><div class="spotlight-invisible objectstatus theme-f" id="generated_id159_29926994">
		
			
	
																			
	<div class="tehuur nieuw"><span></span>
			<span class="objectstatusbanner bannerstatusnieuw">Nieuw</span>
		</div>
</div>

<div class="vaklink" id="generated_id159_29926995">	<div class="tooltip-wrapper tooltip-favoritebutton" id="generated_id159_29926997"><div class="tooltip"><span class="fa-stack"><i class="fa fa-circle fa-stack-2x"></i> <i class="fa fa-check fa-stack-1x fa-inverse"></i></span> <span id="woningSaved" class="hide">Woning is opgeslagen</span><span id="woningSave" class="hide">Bewaar deze woning</span></div><a class="favoriteButton" id="object-7248023" href="#"></a></div><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7248023-Van-Walbeeckstraat-18II/" class="aanbodEntryLink" id="generated_id159_29926998">
				<span id="generated_id159_29927000" class="hoofdfoto ">
				




<img width="420" height="280" id="foto155572553" loading="lazy" src="https://images.realworks.nl/servlets/images/media.objectmedia/155572553.webp?height=280&amp;check=sha256%3A5c32e0888955085386a89cb1fc520f81370fb53d64637ac09c7c2c700096bea4&amp;width=420&amp;resize=5" class="foto_" alt="Van Walbeeckstraat 18 Ii in Amsterdam 1058 CR">




	</span>
<span id="generated_id159_29927001" class="fotolist ">
	




<img width="150" height="100" id="foto155572575" loading="lazy" src="https://images.realworks.nl/servlets/images/media.objectmedia/155572575.webp?height=100&amp;check=sha256%3A82306920e62c941cf7376424d837536a4b5188b3fb18487584caee5ce76f79a2&amp;width=150&amp;resize=5" class="foto_1" alt="Van Walbeeckstraat 18 Ii in Amsterdam 1058 CR">




</span>


	</a>



</div></div><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7248023-Van-Walbeeckstraat-18II/" class="aanbodEntryLink" id="generated_id159_29927007">
					<div class="vakkenmerken" id="generated_id159_29927008">				<span class="kenmerkTitle">Overdracht</span>
				<span class="kenmerk first huurprijs">
			<span class="kenmerkName">Huurprijs</span>						<span class="kenmerkValue">
				€ 1.800,- p.m.
			</span>
		</span>
								<span class="kenmerkTitle">Bouwvorm</span>
				<span class="kenmerk first soortobject">
			<span class="kenmerkName">Soort object</span>						<span class="kenmerkValue">
				Appartement
			</span>
		</span>
					<span class="kenmerk  bouwjaar">
			<span class="kenmerkName">Bouwjaar</span>						<span class="kenmerkValue">
				1931
			</span>
		</span>
					<span class="kenmerk  bouwvorm">
			<span class="kenmerkName">Bouwvorm</span>						<span class="kenmerkValue">
				Bestaande bouw
			</span>
		</span>
								<span class="kenmerkTitle">Indeling</span>
				<span class="kenmerk first woonoppervlakte">
			<span class="kenmerkName">Woonoppervlakte</span>						<span class="kenmerkValue">
				63 m²
			</span>
		</span>
					<span class="kenmerk  inhoud">
			<span class="kenmerkName">Inhoud</span>						<span class="kenmerkValue">
				205 m³
			</span>
		</span>
					<span class="kenmerk  aantalkamers">
			<span class="kenmerkName">Aantal kamers</span>						<span class="kenmerkValue">
				3
			</span>
		</span>
				
</div>	</a><div class="vakmidden" id="generated_id159_29927015"><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7248023-Van-Walbeeckstraat-18II/" class="aanbodEntryLink" id="generated_id159_29927007"><div id="generated_id159_29927018" class="adr addressInfo notranslate">
	
							<h3 class="street-address">Van Walbeeckstraat 18 II</h3>
				<span class="zipcity">
			<span class="postal-code">1058 CR</span>
			<span class="locality">Amsterdam</span>
		</span>
	</div>

<div class="mediaicons mediaicons-link" id="generated_id159_29926215">
											<div class="photos" title="Foto's" data-href="/aanbod/woningaanbod/amsterdam/huur/huis-7248023-Van-Walbeeckstraat-18II/#Foto_s"></div>
											
	</div>

</a><div class="vlakonder" id="generated_id159_29927021"><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7248023-Van-Walbeeckstraat-18II/" class="aanbodEntryLink" id="generated_id159_29927007"></a><div class="schaduwbutton" id="generated_id159_29927022"><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7248023-Van-Walbeeckstraat-18II/" class="aanbodEntryLink" id="generated_id159_29927007"></a><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7248023-Van-Walbeeckstraat-18II/" class="" id="generated_id159_29927024">
					<div class="meer_info" id="generated_id159_29927025">Meer info</div>
	</a>

</div></div></div>	<div class="clear" id="generated_id159_29927029"></div>
	

<script type="application/ld+json">
{"@context":"http://www.schema.org","@type":"Residence","name":"Van Walbeeckstraat 18 Ii in Amsterdam 1058 CR: Appartement te huur.","description":"Appartement te huur: Huurprijs € 1.800,- Per maand. Van Walbeeckstraat 18 Ii in Amsterdam 1058 CR. ","address":{"@context":"http://www.schema.org","@type":"PostalAddress","streetAddress":"Van Walbeeckstraat 18 II","addressLocality":"Amsterdam","postalCode":"1058 CR","addressCountry":"Nederland"},"photo":"https://images.realworks.nl/servlets/images/media.objectmedia/155572553.webp?height=1000&check=sha256%3A5c32e0888955085386a89cb1fc520f81370fb53d64637ac09c7c2c700096bea4&width=1500&resize=1","geo":{"@context":"http://www.schema.org","@type":"GeoCoordinates","latitude":52.360347747802734,"longitude":4.85127592086792},"url":"/aanbod/woningaanbod/amsterdam/huur/huis-7248023-Van Walbeeckstraat-18II/","potentialAction":[{"@context":"http://www.schema.org","@type":"RentAction","realEstateAgent":{"@context":"http://www.schema.org","@type":"RealEstateAgent","name":"Isaak Makelaardij o.g. B.V.","url":"https://www.isaak.nl","logo":"https://static.realworks.nl/clients/42216/logos/1759.jpg","photo":"https://static.realworks.nl/clients/42216/photos/1759.jpg","image":"https://static.realworks.nl/clients/42216/photos/1759.jpg","email":"makelaar@isaak.nl","telephone":"020-6202022","faxNumber":"","address":{"@context":"http://www.schema.org","@type":"PostalAddress","streetAddress":"C. van Eesterenlaan 1","addressLocality":"Amsterdam","postalCode":"1019 JK","addressCountry":"Nederland"},"geo":{"@context":"http://www.schema.org","@type":"GeoCoordinates","latitude":52.372755,"longitude":4.938785},"sameAs":["","","","",""]},"priceSpecification":{"@context":"http://www.schema.org","@type":"UnitPriceSpecification","price":1800.0,"unitCode":"MON","priceCurrency":"EUR","validFrom":"Thu Sep 14 06:00:00 CEST 2023"}}]}
</script>
</li>


"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all(class_="aanbodEntry")

    for article in articles:
        house = House()

        # Link
        link_container = article.find_all("a", href=True)
        if link_container:
            house.link = base_url + link_container[1]["href"]

        # Images
        image_container = article.find("img")
        if image_container:
            house.images.append(image_container["src"])

        # Address
        address_container = article.find("h3", class_="street-address")
        if address_container:
            house.address = address_container.text.strip()

        # City
        city_container = article.find("span", class_="locality")
        if city_container:
            house.city = city_container.text.strip()

        # Price
        price_container = article.find("span", class_="kenmerkValue")
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Details
        details_container = article.find_all("span", class_="kenmerkValue")
        try:
            house.details["m2"] = details_container[0].text.strip()
            house.details["kamers"] = details_container[1].text.strip()
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
