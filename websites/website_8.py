
from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *

url = "https://koopsmakelaardij.nl/zoeken/huur"
base_url ="https://koopsmakelaardij.nl"
example_html = ""
# Function to extract information from the HTML
def scrape_website(html):
    soup = BeautifulSoup(html, 'html.parser')
    house_elements = soup.find_all('div', class_='c-gallery-item js-gallery-item horizontal')

    house_list = []

    for house_elem in house_elements:
        house = House()

        # Extract image URLs
        img_wrappers = house_elem.find_all('div', class_='image-wrapper')
        for img_wrapper in img_wrappers:
            img_elem = img_wrapper.find('img')
            if img_elem:
                house.images.append(img_elem['src'])

        # Extract location (City and Street)
        location_elem = house_elem.find('h4')
        if location_elem:
            location_parts = location_elem.text.split()
            if len(location_parts) >= 1:
                house.city = location_parts[0]
        street_elem = house_elem.find('div', class_ = 'street')
        if street_elem:
            house.address=street_elem.text.strip()

        # Extract additional details
        details_elem = house_elem.find('p', class_='main-properties')
        if details_elem:
            details_parts = details_elem.text.split()
            if len(details_parts) >= 3:
                house.details['rooms'] = details_parts[0][-1]
                house.details['m2'] = details_parts[3]

        # Extract property type and features
        more_properties_elem = house_elem.find('div', class_='more-properties')
        if more_properties_elem:
            property_type = more_properties_elem.find('div')
            if property_type:
                house.property_type = property_type.text.strip()
            features_elems = more_properties_elem.find_all('div', class_='sep')
            features = [elem.text.strip() for elem in features_elems]
            house.features = features

        # Extract price
        price_elem = house_elem.find('div', class_='price')
        if price_elem:
            house.price = get_price(price_elem.text.strip())
            
        # Extract link
        link_elem = house_elem.find('a', class_='o-media__link', href=True)
        if link_elem:
            house.link = base_url+link_elem['href']


        

        house_list.append(house)

    return house_list

website = Website(url, example_html, scrape_website)

# Run the scrape_example function to test the scraper
# houses = website.scrape_example()


# # Print the results
# for house in houses[::-1]:
#     house.print()
#     print()