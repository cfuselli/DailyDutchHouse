from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *


base_url = "https://www.keizerskroonmakelaars.nl"
url = "https://www.keizerskroonmakelaars.nl/huurwoningen"

example_html = """
<div id="RecID937261ab46903580164b64903d70a5c1b51688" class="col-xs-12 col-12 object object-element1">
	<div class="row">
 		
			
					
					
					
										
				
				
				
					
					
					
										
		
		
		
		<div class="col-xs-12 col-12 col-sm-4 object-picture">
			<div class="object-picture1">
				<div class="picture picture1 thumbnail img-thumbnail">
					                                     
 
  

					 

				
				
				
					
						<img src="https://images.realworks.nl/servlets/images/media.objectmedia/153124881.jpg?portalid=4286&amp;check=api_sha256%3af28725864eb562a19919a6da653f189be794c2fab05a637784e852b0720c7d0a&amp;width=1440&amp;height=960" class="img-responsive img-fluid" alt="">
				
				
					
						
						<a href="#" data-src="https://www.keizerskroonmakelaars.nl/huizen/937261ab46903580164b64903d70a5c1b51688/allfoto.htm" data-toggle="modal" data-target="#ModalCarousel" data-slide-to="1" class="object-a-photo">
							<div class="object-icon object-icon-photos text-center">
								<div class="object-icon-inside">
									<span class="glyphicon glyphicon-search" aria-hidden="true"></span>
									Bekijk grote foto's
								</div>
							</div>
						</a>
					
					
					
						
						
						<a href="https://www.keizerskroonmakelaars.nl/singel-264d-amsterdam-937261ab46903580164b64903d70a5c1b51688" class="object-a-more">
					
					
					
					
					
					
						
					
					
					
										
					
					
							<div class="object-icon object-icon-more text-center">
								<div class="object-icon-inside">
									<span class="glyphicon glyphicon-share"></span>
									Bekijk object
								</div>
							</div>
						</a>
					
					
				
				
				</div>
			</div>
				
					
		</div>

		
		
		
		<div class="col-xs-12 col-12 col-sm-6 object-info">
		
			
			<div class="object-adres">
				
				
				
				
				<a href="https://www.keizerskroonmakelaars.nl/singel-264d-amsterdam-937261ab46903580164b64903d70a5c1b51688" class="adreslink d-block mt-3 mt-sm-0">
					<h4 class="notranslate"><span class="adres">Singel 264D</span> <span class="plaatsnaam">Amsterdam </span></h4>
				</a>
				
				
				
				
				
				
			</div>

			<!-- Features element1.tpl -->
			<div class="object-features hidden-xs d-none d-sm-block">
                
                
                	<!-- kenmerken.tpl -->

     
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Soort_woning">
						<div class="features-title col-12 col-xs-12 col-sm-5">Soort woning</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">bovenwoning</div>
					</div>
				</div>
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Type_woning">
						<div class="features-title col-12 col-xs-12 col-sm-5">Type woning</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">bovenwoning</div>
					</div>
				</div>
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Woonoppervlakte">
						<div class="features-title col-12 col-xs-12 col-sm-5">Woonoppervlakte</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">80 m²</div>
					</div>
				</div>
    
    
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Inhoud">
						<div class="features-title col-12 col-xs-12 col-sm-5">Inhoud</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">321 m³</div>
					</div>
				</div>
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Aantal_kamers">
						<div class="features-title col-12 col-xs-12 col-sm-5">Aantal kamers</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">4</div>
					</div>
				</div>
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Aantal_slaapkamers">
						<div class="features-title col-12 col-xs-12 col-sm-5">Aantal slaapkamers</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">3</div>
					</div>
				</div>
    				<!-- kenmerkinsert.tpl1 -->
				<div class="object-feature">
					<div class="row Bouwjaar">
						<div class="features-title col-12 col-xs-12 col-sm-5">Bouwjaar</div>
						<div class="features-info col-12 col-xs-12 col-sm-7">tot 1906</div>
					</div>
				</div>
 
 

                
	        </div>

			<!-- Description -->
			<div class="object-description hidden-xs d-none d-sm-block hidden">
				**No sharing** Recently renovated, luxury and stylish apartment on a great location in a historic monumental building at the Singel! This high-end three bedroom apartment is located on the second floor and at the rear of the property. This unfurnished apartment has three floors with a luxury kitchen, three bedrooms, a bathroom and two toilets. Layout: Through the marble communal entrance you take...
			</div>

			
			
			<div class="object-view">
				
				
				<a href="https://www.keizerskroonmakelaars.nl/singel-264d-amsterdam-937261ab46903580164b64903d70a5c1b51688" class="btn btn-default btn-view-object btn-secondary">
					Bekijk dit object
				</a>
				

				
				
				
				
			</div>
				
			
			
				
				<div class="object-tags hidden-xs d-none d-sm-block">
					Tags: <a href="https://www.keizerskroonmakelaars.nl/tags/modern" title="modern">modern</a>
				</div>
				
			
			

		</div>
		<div class="col-xs-12 col-12 col-sm-2 object-extra">
			<div class="price">       
				                 
 

				<!-- Price -->
				
				    <span class="element_prijs1 prijs_aktief">Huurprijs</span>
   
    
        <span class="element_prijs2 prijs_aktief">€ 2.950&nbsp;per maand</span>
				
			</div>
			<div class="options">
				<div class="option option-favorite">
					       
           
    
  
    
               <span id="Fav937261ab46903580164b64903d70a5c1b51688" class="btn btn-default btn-secondary btn-option btn-favorite Favorietlink" role="button" data-toggle="tooltip" data-placement="top" title="Bewaar in favorieten" onclick="javascript:smf_WriteRemoveFav('Fav937261ab46903580164b64903d70a5c1b51688', '937261ab46903580164b64903d70a5c1b51688')"><span class="glyphicon glyphicon-star" aria-hidden="true"></span></span>
   
   
  


      
				</div>
			</div>
			

		</div>
	</div>
</div>
"""

def scrape_website(html):
	
	soup = BeautifulSoup(html, 'html.parser')
	
	houses = []
	
	articles = soup.find_all('div', class_='col-xs-12 col-12 object object-element1')
	
	for article in articles:
        
		house = House()
        
		# Link
		link_tag = article.find('a', class_='adreslink d-block mt-3 mt-sm-0')
		if link_tag:
			house.link = link_tag['href']
               
		# Find images
		img_tags = article.find('a', href='#')
		house.images.append(img_tags['data-src'])
               
		# Address
		address_container = article.find('span', class_='adres')
		if address_container:
			house.address = address_container.text.strip()
               
		# Address and City
		address_container = article.find('span', class_='plaatsnaam')
		if address_container:
			house.city = address_container.text.strip()
               
		# Price
		price_container = article.find(class_='element_prijs2 prijs_aktief')
		if price_container:
			house.price = get_price(price_container.text.strip())
               
		# Additional Details
		details_container = article.find_all('div', class_='object-feature')
		for detail in details_container:
			try:
				key = detail.find('div', class_='features-title').text.strip()
				value = detail.find('div', class_='features-info').text.strip()
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


