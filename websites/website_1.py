from bs4 import BeautifulSoup
from classes import House, Website
from common import *

url = "https://ikwilhuren.nu/huurwoningen"

example_html = """
<li id="post-2253892" class="search-result epl-listing-post epl-clearfix woning post-2253892 rental type-rental status-publish has-post-thumbnail hentry location-rotterdam vidii_group-101700-uptown epl-status-current">
		<div class="col-xl-5 col-lg-6 pl-0 pr-0 pr-md-3 mb-3 mb-md-0">
		<div class="search-result-img hoofdfoto">
						<a href="https://ikwilhuren.nu/huurwoningen/rotterdam/101700-uptown/jufferstraat-13">Bekijken</a>
			<!--<a href="" class="img-link">-->
												<figure>
							<span class="status-sticker new">Nieuw</span>		<img width="500" height="333" src="https://ikwilhuren.nu/wp-content/uploads/2023/09/54091731_uptownA1-500x333.jpg" class="img-fluid wp-post-image" alt="" srcset="https://ikwilhuren.nu/wp-content/uploads/2023/09/54091731_uptownA1-500x333.jpg 500w, https://ikwilhuren.nu/wp-content/uploads/2023/09/54091731_uptownA1-300x200.jpg 300w, https://ikwilhuren.nu/wp-content/uploads/2023/09/54091731_uptownA1-700x467.jpg 700w, https://ikwilhuren.nu/wp-content/uploads/2023/09/54091731_uptownA1-825x550.jpg 825w" sizes="(max-width: 500px) 100vw, 500px">						<figcaption>
						<p><i class="fa fa-fw fa-eye"></i> Bekijken</p>
					</figcaption>
				</figure>
			<!--</a>-->
					</div>
	</div>
	<div class="col-xl-7 col-lg-6 info">
		<div class="search-result-content">
			<div class="search-result-title adres">
				<a href="https://ikwilhuren.nu/huurwoningen/rotterdam/101700-uptown/jufferstraat-13">
					<h3>
						<span class="street-name straat">Jufferstraat 13</span>
						<small class="postal-code plaats">3011 XL Rotterdam</small>
					</h3>
				</a>
			</div>
			<div class="search-result-info search-result-price prijs huurprijs">
				<span class="label d-none">Huurprijs</span>
				<span class="page-price-rent"><span class="page-price" style="margin-right:0">€1.255</span><span class="rent-period">/Maand</span></span>			</div>
			<div class="search-result-info details">
								<ul class="search-result-specs">
									<li class="soortobject"><span class="label d-none">Type</span>Appartement</li>
													<li class="oppervlakte"><span class="label d-none">Oppervlakte</span>66 m<sup>2</sup></li>
																	<li class="slaapkamers"><span class="label d-none">Slaapkamers</span>2 slaapkamers</li>
																		<li class="beschikbaarper"><span class="label d-none">Beschikbaar</span>Vanaf 01-11-2023</li>
													<!-- <li>Gestoffeerd</li> -->
														<!-- <li>Gemeubileerd</li> -->
								</ul>
			</div>
			<div class="search-result-footer d-none d-lg-block">
				<div class="search-result-button pull-right">
					<a href="https://ikwilhuren.nu/huurwoningen/rotterdam/101700-uptown/jufferstraat-13" class="detaillink btn btn-theme-tertiary" title="Woning bekijken">Meer informatie <i class="fa fa-chevron-right"></i></a>
				</div>
								<div class="clearfix"></div>
			</div>
		</div>
	</div>
</li>
"""

def scrape_website(html):
	soup = BeautifulSoup(html, 'html.parser')
	property_elements = soup.find_all('li', class_='search-result')
	house_list = []

	for property_elem in property_elements:
		house = House()

		# Extract address and city
		address_elem = property_elem.find('span', class_='street-name')
		postal_code_elem = property_elem.find('small', class_='postal-code')
		if address_elem and postal_code_elem:
			house.address = address_elem.text.strip()
			house.city = postal_code_elem.text.strip()

		# Extract price
		price_elem = property_elem.find('span', class_='page-price')
		if price_elem:

			house.price = get_price(price_elem.text.strip())

		# Extract other details
		details_elems = property_elem.find_all('li')
		for detail_elem in details_elems:
			label_elem = detail_elem.find('span', class_='label')
			if label_elem:
				key = label_elem.text.strip()
				value = detail_elem.text.replace(key, '').strip()
				house.details[key] = value

		images_elem = property_elem.find_all('img', src=True)
		for image_elem in images_elem:
			house.images.append(image_elem['src'])


		# Extract link
		link_elem = property_elem.find('a', class_='detaillink', href=True)
		if link_elem:
			house.link = link_elem['href']

		house_list.append(house)

	return house_list
	
# Create instances of the Website class for each website
website = Website(url, example_html, scrape_website)
