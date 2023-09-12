from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *


base_url = "https://www.rappange.com/huurwoningen"
url = "https://www.rappange.com/huurwoningen"

example_html = """
<div id="RecID9370833e17bb84b99d4d528c9e3584567feb59" class="col-xs-12 object object-element2">
	<div class="row">
  		
		
		<div class="col-xs-12 col-12 col-sm-4 col-md-6 object-picture">
			<div class="row">
				<div class="col-xs-12 col-12 col-md-6 object-picture1">
					<div class="picture picture1 thumbnail img-thumbnail">
						                                     
 
  

						 

						<img src="https://images.realworks.nl/servlets/images/media.objectmedia/146252429.jpg?portalid=4286&amp;check=api_sha256%3aa1769a152511cfc3e0e9f053c9863753946b1b670619d15bc1ec8d422e15e59b&amp;width=1440&amp;height=960" class="img-responsive img-fluid" alt="">
		
		
		
			
						<a href="#" data-src="https://www.rappange.com/huizen/9370833e17bb84b99d4d528c9e3584567feb59/allfoto.htm" data-toggle="modal" data-target="#ModalCarousel" data-slide-to="1" class="object-a-photo">
							<div class="object-icon object-icon-photos text-center">
								<div class="object-icon-inside">
									<span class="glyphicon glyphicon-search" aria-hidden="true"></span>
									Grote foto's
								</div>
							</div>
						</a>
			
			
			
				
				
						<a href="https://www.rappange.com/jan-van-goyenkade-27-1-amsterdam-9370833e17bb84b99d4d528c9e3584567feb59" class="object-a-more">
					
			
			
					
			
			
				
					
			
			
										
				
				
							<div class="object-icon object-icon-more text-center">
								<div class="object-icon-inside">
									<span class="glyphicon glyphicon-share"></span>
									Bekijk object
								</div>
							</div>
						</a>
					</div>
				
				
				
				</div>
				<div class="col-xs-12 col-12 col-sm-6 hidden-xs hidden-sm d-none d-md-block object-picture2">
					<div class="picture picture2 thumbnail img-thumbnail">
						<img src="https://images.realworks.nl/servlets/images/media.objectmedia/146252427.jpg?portalid=4286&amp;check=api_sha256%3a076c9d42d228bc6cda343852df283dac822cb9cabc2dda1b6895d68e7225026e&amp;width=1440&amp;height=960" class="img-responsive img-fluid" alt="">
				
				
				
					
						<a href="#" data-src="https://www.rappange.com/huizen/9370833e17bb84b99d4d528c9e3584567feb59/allfoto.htm" data-toggle="modal" data-target="#ModalCarousel" data-slide-to="2" class="object-a-photo">
							<div class="object-icon object-icon-photos text-center">
								<div class="object-icon-inside">
									<span class="glyphicon glyphicon-search" aria-hidden="true"></span>
									Grote foto's
								</div>
							</div>
						</a>
				
				
				
					
					
						<a href="https://www.rappange.com/jan-van-goyenkade-27-1-amsterdam-9370833e17bb84b99d4d528c9e3584567feb59" class="object-a-more">
					
				
				
					
				
				
					
					
				
				
										
				
				
							<div class="object-icon object-icon-more text-center">
								<div class="object-icon-inside">
									<span class="glyphicon glyphicon-share"></span>Bekijk object
								</div>
							</div>
						</a>
					</div>
				</div>
			</div>
		
				
				
					
					
					
					
										
					
					
				
					
		</div>

		
		
		<div class="col-xs-12 col-12 col-sm-6 col-md-4 object-info">
		
		
		
		
			
			<div class="object-adres">
				
				
				
				
				<a href="https://www.rappange.com/jan-van-goyenkade-27-1-amsterdam-9370833e17bb84b99d4d528c9e3584567feb59" class="adreslink d-block mt-3 mt-sm-0">
					<h4 class="notranslate"><span class="adres">Jan van Goyenkade 27-1</span> <span class="plaatsnaam">Amsterdam </span></h4>
				</a>
				
				
				
				
				
				
			</div>

			<!-- Features element1.tpl -->
			<div class="object-features hidden-xs d-none d-sm-block">
                
                
                	<!-- kenmerken.tpl -->

     
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Soort_woning">
						<div class="features-title col-12 col-xs-12 col-sm-5">Soort woning</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">tussenverdieping</div>
					</div>
				</div>
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Type_woning">
						<div class="features-title col-12 col-xs-12 col-sm-5">Type woning</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">tussenverdieping</div>
					</div>
				</div>
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Woonoppervlakte">
						<div class="features-title col-12 col-xs-12 col-sm-5">Woonoppervlakte</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">270 m²</div>
					</div>
				</div>
    
    
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Inhoud">
						<div class="features-title col-12 col-xs-12 col-sm-5">Inhoud</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">1050 m³</div>
					</div>
				</div>
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Aantal_kamers">
						<div class="features-title col-12 col-xs-12 col-sm-5">Aantal kamers</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">8</div>
					</div>
				</div>
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Aantal_slaapkamers">
						<div class="features-title col-12 col-xs-12 col-sm-5">Aantal slaapkamers</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">4</div>
					</div>
				</div>
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Bouwjaar">
						<div class="features-title col-12 col-xs-12 col-sm-5">Bouwjaar</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">vanaf 1906 t/m 1930</div>
					</div>
				</div>
 
 

                
	        </div>

			<!-- Description -->
			<div class="object-description hidden-xs d-none d-sm-block hidden">
				Jan van Goyenkade 27-I 1075 HS Amsterdam ***for English see below*** UNIEK OBJECT VAN MAAR LIEFST CA. 270M2; PRACHTIG UITZICHT OP DE JAN VAN GOYENKADE. WONEN OP DE EERSTE VERDIEPING IN HET PRACHTIG MONUMENTALE COMPLEX WESTHOVE MET LIFT IN AMSTERDAM ZUID Wonen in alle rust in een appartement van ca. 270 m2 op één etage, met lift gelegen in het unieke complex Westhove. Dit prachtige authentieke...
			</div>

			
			
			<div class="object-view">
				
				
				<a href="https://www.rappange.com/jan-van-goyenkade-27-1-amsterdam-9370833e17bb84b99d4d528c9e3584567feb59" class="btn btn-default btn-view-object btn-secondary">
					Bekijk dit object
				</a>
				

				
				
				
				
			</div>
				
			
			
			
				
					
				
			

		</div>
		<div class="col-xs-12 col-12 col-sm-2 object-extra">
			<div class="price">       
				                 
 

				<!-- Price -->
				
				    <span class="element_prijs1 prijs_aktief">Huurprijs</span>
   
    
        <span class="element_prijs2 prijs_aktief">€ 6.000&nbsp;per maand</span>
				
			</div>
			<div class="options">
				<div class="option option-favorite">
					       
           
    
  
    
               <span id="Fav9370833e17bb84b99d4d528c9e3584567feb59" class="btn btn-default btn-secondary btn-option btn-favorite Favorietlink" role="button" data-toggle="tooltip" data-placement="top" title="Bewaar in favorieten" onclick="javascript:smf_WriteRemoveFav('Fav9370833e17bb84b99d4d528c9e3584567feb59', '9370833e17bb84b99d4d528c9e3584567feb59')"><span class="glyphicon glyphicon-star" aria-hidden="true"></span></span>
   
   
  


      
				</div>
			</div>
			

		</div>
	</div>
</div>
<input type="hidden" id="mgmMarker9370833e17bb84b99d4d528c9e3584567feb59" name="mgmMarker9370833e17bb84b99d4d528c9e3584567feb59" value="9370833e17bb84b99d4d528c9e3584567feb59~1~52.35137953,4.86622093~1075HS~Amsterdam~Amsterdam~Jan van Goyenkade~27~-1~WH~1~tussenverdieping~<span class=adres>Jan van Goyenkade 27-1</span> <span class=plaatsnaam>Amsterdam </span>~<b>Huurprijs</b><br/>€ 6.000&nbsp;per maand~6000~per maand~Huurprijs~6.000~https://www.rappange.com/jan-van-goyenkade-27-1-amsterdam-9370833e17bb84b99d4d528c9e3584567feb59~https://images.realworks.nl/servlets/images/media.objectmedia/146252429.jpg?portalid=4286&amp;check=api_sha256%3aa1769a152511cfc3e0e9f053c9863753946b1b670619d15bc1ec8d422e15e59b&amp;width=1440&amp;height=960~0~1~04/07/2023~1">"""

def scrape_website(html):

    soup = BeautifulSoup(html, 'html.parser')

    houses = []

    articles = soup.find_all('div', class_='col-xs-12 object object-element2')

    for article in articles:

        house = House()

        # Link
        link_tag = article.find('a', class_='object-a-more')
        if link_tag:
            house.link = link_tag['href']


        # Find images
        img_tags = article.find_all('a', class_='object-a-photo')
        for img_tag in img_tags:
            house.images.append(img_tag['data-src'])

        # Address and City
        address_container = article.find('span', class_='adres')
        city_container = article.find('span', class_='plaatsnaam')
        if address_container and city_container:
            house.city = city_container.text.strip()
            house.address = address_container.text.strip()

        # Price
        price_container = article.find(class_='element_prijs2')
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Additional Details
        details_container = article.find_all('div', class_='object-feature')
        for detail in details_container:
            label = detail.find('div', class_='features-title')
            if label:
                label = label.text.strip()
                value = detail.find('div', class_='features-info').text.strip()
                house.details[label] = value[:50]

        if house.price != None:
            if house.price < 10000:
                
                print(img_tags)
                print('------------------')

                houses.append(house)

    return houses


website = Website(url, example_html, scrape_website)



# Run the scrape_example function to test the scraper
# houses = website.scrape_example()


# # # Print the results
# for house in houses[::-1]:
#     house.print()
#     print()


