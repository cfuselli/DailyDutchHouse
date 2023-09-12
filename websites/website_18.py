from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *


base_url = "https://www.telvgm.nl"
url = "https://www.telvgm.nl/aanbod/woningaanbod/AMSTERDAM/huur/"

example_html = """
<li class="al2woning aanbodEntry even">			<div class="vakfoto" id="generated_id185_102839347"><div class="spotlight-invisible objectstatus theme-h" id="generated_id185_102839348">
		
			
	
																
	<div class="tehuur verhuurdov bannerstatusnieuw"><span></span>
			<span class="objectstatusbanner bannerstatusverhuurdov bannerstatusnieuw">Verhuurd o.v.</span>
		</div>
</div>

<div class="vaklink" id="generated_id185_102839349">	<div class="tooltip-wrapper tooltip-favoritebutton" id="generated_id185_102839351"><div class="tooltip"><span class="fa-stack"><i class="fa fa-circle fa-stack-2x"></i> <i class="fa fa-check fa-stack-1x fa-inverse"></i></span> <span id="woningSaved" class="hide">Woning is opgeslagen</span><span id="woningSave" class="hide">Bewaar deze woning</span></div><a class="favoriteButton" id="object-7226207" href="#"></a></div><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7226207-Jacob-Obrechtplein-7I/" class="aanbodEntryLink" id="generated_id185_102839352">
				<span id="generated_id185_102839354" class="hoofdfoto ">
				




<img width="420" height="280" id="foto154949683" loading="lazy" src="https://images.realworks.nl/servlets/images/media.objectmedia/154949683.webp?height=280&amp;check=sha256%3Af3892daddf4b9c1a698ced5bb4dd79167c69c8e202fa84b5bd05043d4ffbd4a3&amp;width=420&amp;resize=5" class="foto_" alt="Jacob Obrechtplein 7 I in Amsterdam 1071 KS">




	</span>
<span id="generated_id185_102839355" class="fotolist ">
	




<img width="150" height="100" id="foto154949699" loading="lazy" src="https://images.realworks.nl/servlets/images/media.objectmedia/154949699.webp?height=100&amp;check=sha256%3A6b6f859435d49e3b890226f1452139eed9a16c47eaa96586705d00316e77b602&amp;width=150&amp;resize=5" class="foto_1" alt="Jacob Obrechtplein 7 I in Amsterdam 1071 KS">




</span>


	</a>



</div></div><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7226207-Jacob-Obrechtplein-7I/" class="aanbodEntryLink" id="generated_id185_102839361">
					<div class="vakkenmerken" id="generated_id185_102839362">				<span class="kenmerkTitle">Overdracht</span>
				<span class="kenmerk first huurprijs">
			<span class="kenmerkName">Huurprijs</span>						<span class="kenmerkValue">
				€ 1.950,- p.m.
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
				1927
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
				71 m²
			</span>
		</span>
					<span class="kenmerk  inhoud">
			<span class="kenmerkName">Inhoud</span>						<span class="kenmerkValue">
				185 m³
			</span>
		</span>
					<span class="kenmerk  aantalkamers">
			<span class="kenmerkName">Aantal kamers</span>						<span class="kenmerkValue">
				3
			</span>
		</span>
				
</div>	</a><div class="vakmidden" id="generated_id185_102839369"><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7226207-Jacob-Obrechtplein-7I/" class="aanbodEntryLink" id="generated_id185_102839361"><div id="generated_id185_102839372" class="adr addressInfo notranslate">
	
							<h3 class="street-address">Jacob Obrechtplein 7 I</h3>
				<span class="zipcity">
			<span class="postal-code">1071 KS</span>
			<span class="locality">Amsterdam</span>
		</span>
	</div>

<div class="mediaicons mediaicons-link" id="generated_id185_102838566">
											<div class="photos" title="Foto's" data-href="/aanbod/woningaanbod/amsterdam/huur/huis-7226207-Jacob-Obrechtplein-7I/#Foto_s"></div>
											
	</div>

</a><div class="vlakonder" id="generated_id185_102839375"><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7226207-Jacob-Obrechtplein-7I/" class="aanbodEntryLink" id="generated_id185_102839361"></a><div class="schaduwbutton" id="generated_id185_102839376"><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7226207-Jacob-Obrechtplein-7I/" class="aanbodEntryLink" id="generated_id185_102839361"></a><a href="/aanbod/woningaanbod/amsterdam/huur/huis-7226207-Jacob-Obrechtplein-7I/" class="" id="generated_id185_102839378">
					<div class="meer_info" id="generated_id185_102839379">Meer info</div>
	</a>

</div></div></div>	<div class="clear" id="generated_id185_102839383"></div>
	

<script type="application/ld+json">
{"@context":"http://www.schema.org","@type":"Residence","name":"Jacob Obrechtplein 7 I in Amsterdam 1071 KS: Appartement te huur.","description":"Appartement te huur:  € 1.950,- Per maand. Jacob Obrechtplein 7 I in Amsterdam 1071 KS. ","address":{"@context":"http://www.schema.org","@type":"PostalAddress","streetAddress":"Jacob Obrechtplein 7 I","addressLocality":"Amsterdam","postalCode":"1071 KS","addressCountry":"Nederland"},"photo":"https://images.realworks.nl/servlets/images/media.objectmedia/154949683.webp?height=1000&check=sha256%3Af3892daddf4b9c1a698ced5bb4dd79167c69c8e202fa84b5bd05043d4ffbd4a3&width=1500&resize=1","geo":{"@context":"http://www.schema.org","@type":"GeoCoordinates","latitude":52.35289001464844,"longitude":4.878242015838623},"url":"/aanbod/woningaanbod/amsterdam/huur/huis-7226207-Jacob Obrechtplein-7I/","potentialAction":[{"@context":"http://www.schema.org","@type":"BuyAction","seller":{"@context":"http://www.schema.org","@type":"RealEstateAgent","name":"Tel Vastgoedmanagement","url":"https://www.telvgm.nl","logo":"https://static.realworks.nl/clients/44136/logos/2936.jpg","photo":"https://static.realworks.nl/clients/44136/photos/2936.jpg","image":"https://static.realworks.nl/clients/44136/photos/2936.jpg","email":"info@telvgm.nl","telephone":"020-3012949","faxNumber":"020-6753741","address":{"@context":"http://www.schema.org","@type":"PostalAddress","streetAddress":"Buitenveldertselaan 101","addressLocality":"Amsterdam","postalCode":"1082 VB","addressCountry":""},"geo":{"@context":"http://www.schema.org","@type":"GeoCoordinates","latitude":52.331901,"longitude":4.869313},"sameAs":["https://www.facebook.com/pages/Nico-Tel-Makelaars-og-BV/181612518517027","","https://www.instagram.com/telmakelaars/","","https://www.linkedin.com/company/nico-tel-makelaars"]},"priceSpecification":{"@context":"http://www.schema.org","@type":"PriceSpecification","price":1950.0,"priceCurrency":"EUR","validFrom":"Mon Sep 11 06:00:00 CEST 2023"}}]}
</script>
</li>
"""

def scrape_website(html):

    soup = BeautifulSoup(html, 'html.parser')

    houses = []

    articles = soup.find_all('li', class_='aanbodEntry')

    for article in articles:

        house = House()

        # Link
        link_tag = article.find('a', class_='aanbodEntryLink')
        if link_tag:
            house.link = base_url + link_tag['href']

        
        # Find images
        img_tags = article.find_all('img')
        for img_tag in img_tags:
            house.images.append(img_tag['src'])


        # Address
        address_container = article.find('h3', class_='street-address')
        if address_container:
            house.address = address_container.text.strip()

        # Address and City
        address_container = article.find('span', class_='zipcity')
        if address_container:
            house.city = address_container.text.strip().replace('\n', ' ')

        # Price
        price_container = article.find(class_='kenmerkValue')
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Additional Details
        details_container = article.find_all('span', class_='kenmerk')
        for detail in details_container:
            try:
                key = detail.find('span', class_='kenmerkName').text.strip()
                value = detail.find('span', class_='kenmerkValue').text.strip()
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


