from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *

base_url = "https://www.hausing.com"
url = "https://www.hausing.com/properties-for-rent-amsterdam"

example_html = ""

def scrape_website(html):

    soup = BeautifulSoup(html, 'html.parser')
    property_elements = soup.find_all('div', {'role': 'listitem'})

    house_list = []

    for property_elem in property_elements:

        house = House()

        house.city = 'Amsterdam'

        # Extract street name and house number
        street_name_elem = property_elem.find('div', class_='address')
        if street_name_elem:
            house.address = street_name_elem.text.strip()


        # Extract price
        price_elem = property_elem.find_all('p', class_='price-text-small-5')
        if price_elem:
            price = price_elem[1].text.strip()
            house.price = price

        # Extract details
        details_elems = property_elem.find_all('div', class_='sqm-space-right')
        house.details['Rooms'] = details_elems[0].text.strip()
        house.details['Area m2'] = details_elems[2].text.strip()

        # Extract images
        img_elem = property_elem.find('img', alt=True, srcset=True)
        if img_elem:
            srcset = img_elem['srcset']
            # Split the srcset into individual image URLs
            srcset_parts = srcset.split(',')
            for srcset_part in srcset_parts:
                # Extract the URL from the srcset part
                image_url = srcset_part.split()[-2].strip()
                house.images.append(image_url)

        # Extract link
        link_elem = property_elem.find('a', class_='link-post', href=True)
        if link_elem:
            house.link = base_url+link_elem['href']

        available = property_elem.find('p', 'availability-caption-2').text.strip()
        if available == 'Available':
            if house.link:
                house_list.append(house)

    return house_list



# Create an instance of the Website class for the new website
website = Website(url, example_html, scrape_website)

# Run the scrape_example function to test the scraper
# houses = website.scrape_example()

# print('Number of houses:', len(houses))

# # Print the results
# for house in houses[::-1]:
#     house.print()
#     print()
