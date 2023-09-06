from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *

base_url = "https://www.vindjeplekbijdekey.nl"
url = "https://www.vindjeplekbijdekey.nl/huren#stad=27"

example_html = """
<li>
            <figure class="col-xs-12 col-sm-3">
                
                <a href="/huren/amsterdam/zoutkeetsgracht-9-1013lc" title="Meer informatie woning Zoutkeetsgracht 9  - Amsterdam"><img src="/media/cache/dekey_thumb/uploads/dossier/images/64f2e4a719789.jpg" class="img-responsive" alt=""></a>

                                    <div class="ribbon-wrapper">
                        <div class="ribbon-orange">
                            nieuw
                        </div>
                    </div>

                                            </figure>
            <div class="col-xs-12 col-sm-9">
                                <h2>
					<a href="/huren/amsterdam/zoutkeetsgracht-9-1013lc" title="Meer informatie woning Zoutkeetsgracht 9  - Amsterdam">
                    Zoutkeetsgracht 9 
                    <span>1013 LC, Amsterdam</span>
					</a>
                </h2>
                <ul class="features pull-left">
                                            <li>4 kamers - 94 m²</li>
                                                                                        <li>appartement</li>
                                                                                                                                                                                                                    <li>
                            Balkon
                        </li>
                                        
                </ul>
                <ul class="pull-right price-holder">
                                            <li class="price"><span>€ 2.250,00</span> p.m. </li>
                                                                <li><a href="/huren/amsterdam/zoutkeetsgracht-9-1013lc" class="btn" title="Bekijk deze woning">Bekijk deze woning</a></li>
                                    </ul>
            </div>
            <div class="clearfix"></div>
        </li>
"""

def scrape_website(html):
    soup = BeautifulSoup(html, 'html.parser')
    property_list = soup.find('ul', class_='search-list')

    house_list = []

    if property_list:
        property_elements = property_list.find_all('li')

        for property_elem in property_elements:
            
                            # Extract city
            city_elem = property_elem.find('span')
            if city_elem:
                city = city_elem.text.strip()

            if 'Amsterdam' in city:

                house = House()

                house.city = city

                # Extract title and link
                title_elem = property_elem.find('h2')
                if title_elem:
                    house_elem = title_elem.find('a', href=True)
                    if house_elem:
                        house.address = title_elem.text.strip()
                        house.link = base_url+house_elem['href']

                # Extract city
                city_elem = property_elem.find('span')
                if city_elem:
                    house.city = city_elem.text.strip()

                # Extract price
                price_elem = property_elem.find('li', class_='price')
                if price_elem:
                    house.price = get_price(price_elem.text.strip())

                # Extract details
                details_elem = property_elem.find('ul', class_='features')
                if details_elem:
                    details_list = details_elem.find_all('li')
                    for detail in details_list:
                        detail_text = detail.text.strip()
                        if 'kamers' in detail_text:
                            rooms = re.search(r'(\d+)\s+kamers', detail_text)
                            if rooms:
                                house.details['Rooms'] = rooms.group(1)
                        elif 'm²' in detail_text:
                            area = re.search(r'(\d+)\s+m²', detail_text)
                            if area:
                                house.details['Area'] = area.group(1)

                # Extract images
                image_elem = property_elem.find('img', src=True)
                if image_elem:
                    house.images.append(base_url+image_elem['src'])

                if 'Amsterdam' in house.address:
                    house_list.append(house)

    return house_list


# Create an instance of the Website class for the new website
website = Website(url, example_html, scrape_website)

# Run the scrape_example function to test the scraper
houses = website.scrape_example()

# Print the results
for house in houses[::-1]:
    house.print()
    print()
