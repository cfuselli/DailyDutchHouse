from bs4 import BeautifulSoup
import sys
sys.path.append('.')
sys.path.append('../')
from classes import House, Website
from common import *
import os

base_url = 'https://ikwilhuren.nu'
url = "https://ikwilhuren.nu/aanbod/direct-beschikbaar/"

example_html = """
<div class="col-sm-6 d-flex flex-column">
                                        
    <div class="card card-woning shadow-sm rounded-5 rounded-end-0 rounded-bottom-0 overflow-hidden flex-grow-1">
        <div class="card-img-top">
            <div class="badges position-absolute end-0 me-4 mt-4 index-1 d-flex gap-2">
                                                                            <span class="badge bg-white text-body shadow-xs">
                        <span class="status-dot bg-status-te-huur rounded-circle me-1"></span>
                                                      Te huur
                                             </span>
                            </div>
            <div class="ratio" style="--bs-aspect-ratio: 66%;">
                <picture class="h-100 w-100">
                                            <img loading="lazy" width="576" height="383" srcset="/media/a3/a3f342f61dbc6d97528cacb00acc5b14/394x262/thumb.jpg 420w,
                                                               /media/a3/a3f342f61dbc6d97528cacb00acc5b14/576x383/thumb.jpg 576w" sizes="(max-width: 420px) 420px, 576px" src="//d.static.nbo.nl/media/a3/a3f342f61dbc6d97528cacb00acc5b14/768x510/thumb.jpg" alt="Rottumstraat 35" class="d-block w-100 h-100" style="object-fit: cover;">
                                    </picture>
            </div>
        </div>
        <div class="card-body d-flex flex-column">
            <h3 class="card-title fs-5 text-secondary mb-0">
                <a class="stretched-link" href="/object/duiven-6922ew-35-rottumstraat-5283b6133c6ebbfa0afbf57cb8446e0c/">
                    Rottumstraat 35
                </a>
            </h3>
            <span>6922EW Duiven</span>

            <span class="small">
                <span class="d-flex gap-1">
                    <span><svg class="svg-inline--fa fa-calendar text-success fa-fw" aria-hidden="true" focusable="false" data-prefix="fal" data-icon="calendar" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="currentColor" d="M112 0c8.8 0 16 7.2 16 16V64H320V16c0-8.8 7.2-16 16-16s16 7.2 16 16V64h32c35.3 0 64 28.7 64 64v32 32V448c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V192 160 128C0 92.7 28.7 64 64 64H96V16c0-8.8 7.2-16 16-16zM416 192H32V448c0 17.7 14.3 32 32 32H384c17.7 0 32-14.3 32-32V192zM384 96H64c-17.7 0-32 14.3-32 32v32H416V128c0-17.7-14.3-32-32-32z"></path></svg><!-- <i class="fal fa-calendar text-success fa-fw"></i> Font Awesome fontawesome.com --></span>
                                            Direct beschikbaar
                                    </span>
                                    <span class="d-flex gap-1"><span><svg class="svg-inline--fa fa-heart text-success fa-fw" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="heart" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M47.6 300.4L228.3 469.1c7.5 7 17.4 10.9 27.7 10.9s20.2-3.9 27.7-10.9L464.4 300.4c30.4-28.3 47.6-68 47.6-109.5v-5.8c0-69.9-50.5-129.5-119.4-141C347 36.5 300.6 51.4 268 84L256 96 244 84c-32.6-32.6-79-47.5-124.6-39.9C50.5 55.6 0 115.2 0 185.1v5.8c0 41.5 17.2 81.2 47.6 109.5z"></path></svg><!-- <i class="far fa-solid fa-heart text-success fa-fw"></i> Font Awesome fontawesome.com --></span>Direct inschrijven via deze site</span>
                
                 <span title="Sinds 0.97435185185185 dagen online">Nieuw</span>
                            </span>

            <div class="pt-4 dotted-spans mt-auto">
                <span class="fw-bold">€ 1.055,- /mnd</span>
                <span>117 m<sup>2</sup></span>                <span>3  slaapkamers </span>            </div>
        </div>
    </div>

                                    </div>
"""

def scrape_website(html):
    soup = BeautifulSoup(html, 'html.parser')
    property_elements = soup.find_all('div', class_='card-woning')

    house_list = []

    for property_elem in property_elements:
        house = House()

        # Extract title and link
        title_elem = property_elem.find('h3', class_='card-title')
        if title_elem:
            house.address = title_elem.text.strip()
            link_elem = title_elem.find('a', href=True)
            if link_elem:
                house.link = base_url+link_elem['href']

        # Extract city
        city_elem = property_elem.find('span', text=True)
        if city_elem:
            city_parts = city_elem.text.strip().split()
            if len(city_parts) > 1:
                house.city = city_parts[1]

        # Extract price
        price_elem = property_elem.find('span', class_='fw-bold')
        if price_elem:
            house.price = get_price(price_elem.text.strip())

         # Extract details
        details_elem = property_elem.find('div', class_='pt-4')
        if details_elem:
            details_spans = details_elem.find_all('span', class_='fw-bold')
            if len(details_spans) >= 2:
                house.details['Area'] = details_spans[1].text.strip()
                room_span = details_elem.find('span', text=re.compile(r'\d+\s+slaapkamers'))
                if room_span:
                    rooms = re.search(r'(\d+)\s+slaapkamers', room_span.text)
                    if rooms:
                        house.details['Rooms'] = rooms.group(1)

        # Extract images
        image_elem = property_elem.find('img', src=True)
        if image_elem:
            house.images.append(base_url + '/media/'+ image_elem['src'].split('/media/')[1])

        house_list.append(house)

    return house_list


# def scrape_website(html):
# 	soup = BeautifulSoup(html, 'html.parser')
# 	property_elements = soup.find_all('li', class_='search-result')
# 	house_list = []

# 	for property_elem in property_elements:
# 		house = House()

# 		# Extract address and city
# 		address_elem = property_elem.find('span', class_='street-name')
# 		postal_code_elem = property_elem.find('small', class_='postal-code')
# 		if address_elem and postal_code_elem:
# 			house.address = address_elem.text.strip()
# 			house.city = postal_code_elem.text.strip()

# 		# Extract price
# 		price_elem = property_elem.find('span', class_='page-price')
# 		if price_elem:

# 			house.price = get_price(price_elem.text.strip())

# 		# Extract other details
# 		details_elems = property_elem.find_all('li')
# 		for detail_elem in details_elems:
# 			label_elem = detail_elem.find('span', class_='label')
# 			if label_elem:
# 				key = label_elem.text.strip()
# 				value = detail_elem.text.replace(key, '').strip()
# 				house.details[key] = value

# 		images_elem = property_elem.find_all('img', src=True)
# 		for image_elem in images_elem:
# 			house.images.append(image_elem['src'])


# 		# Extract link
# 		link_elem = property_elem.find('a', class_='detaillink', href=True)
# 		if link_elem:
# 			house.link = link_elem['href']

# 		house_list.append(house)

# 	return house_list
	
# Create instances of the Website class for each website
website = Website(url, example_html, scrape_website)


# # Run the scrape_example function to test the scraper
# houses = website.scrape_example()

# # Print the results
# for house in houses[::-1]:
#     house.print()
#     print()
