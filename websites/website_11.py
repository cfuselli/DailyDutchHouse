
from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *


base_url = "https://parkerwilliams.nl"

url = "https://parkerwilliams.nl/residential-listings/rent/amsterdam?locationofinterest=Amsterdam"

example_html = """
<article class="objectcontainer col-12 col-xs-12 col-sm-6 col-md-6 col-lg-4">
        <div class="object   ">
            <div class="object_status_container">
                        <span class="object_status rented_under_conditions">
                            Rented subject to conditions
                        </span>
            </div>
            <a class="img-container" href="/residential-listings/rent/amsterdam/oude-leliestraat/8-d?forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;take=12">
                <div class="datashort">
                    <span class="street">Oude Leliestraat 8D</span>
                        <span class="location">Amsterdam</span>
                                                <span class="obj_price">
                                €2,350 /mo
                            </span>
                </div>

                <div class="content">
                    <img width="350" alt="Rented subject to conditions: Oude Leliestraat 8D, 1015AW Amsterdam" class="img-responsive object_image_srcset img-fluid" loading="lazy" srcset="https://haywebattachments.blob.core.windows.net/public/2293/2945780/86965575/$m/img_0048.jpg 600w,
                            https://haywebattachments.blob.core.windows.net/public/2293/2945780/86965575/$s/img_0048.jpg 300w" sizes="auto" src="https://haywebattachments.blob.core.windows.net/public/2293/2945780/86965575/$s/img_0048.jpg">
                </div>
            </a>

            <div class="data">
                <div class="stats">
                        <a class="item photos" href="/residential-listings/rent/amsterdam/oude-leliestraat/8-d?forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;take=12">
                            <i class="fal fa-image" aria-hidden="true"></i>23
                        </a>
                                                                                                        <a class="item  make-favorite object-favorite " id="object-favorite-2945780" data-property-id="2945780" data-property-address="Rented subject to conditions: Oude Leliestraat 8D, 1015AW Amsterdam" href="#" data-toggle="tooltip" data-trigger="hover" data-placement="top" title="" data-original-title="Save as favourite">
                            <span class="favorite fav-icon">
                                <i class="fal fa-heart" aria-hidden="true"></i>
                            </span>
                        </a>
                                            <a class="item  object-follow " id="object-follow-2945780" data-property-id="2945780" data-property-address="Rented subject to conditions: Oude Leliestraat 8D, 1015AW Amsterdam" href="#" data-toggle="tooltip" data-trigger="hover" data-placement="top" title="" data-original-title="Follow listing">
                            <span class="follow fol-icon">
                                <i class="fal fa-bell" aria-hidden="true"></i>
                            </span>
                        </a>
                                    </div>
                <h3 class="obj_address">
                    <a href="/residential-listings/rent/amsterdam/oude-leliestraat/8-d?forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;take=12">
                        <span class="street">Oude Leliestraat 8D</span>
                            <span class="zipcode">1015AW</span>
                                                    <span class="locality">Amsterdam</span>
                    </a>
                </h3>
                <a class="saletitle" href="/residential-listings/rent/amsterdam/oude-leliestraat/8-d?forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;take=12">
                </a>
                <a class="object_data_labels" href="/residential-listings/rent/amsterdam/oude-leliestraat/8-d?forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;take=12">
                        <span class="object_label object_rooms">
                            <span class="number">3</span>
                            <i class="fa fa-clone" aria-hidden="true"></i>
                            <span class="text">rooms</span>
                        </span>

                        <span class="object_label object_bed_rooms">
                            <span class="number">2</span>
                            <i class="fa fa-bed" aria-hidden="true"></i>
                            <span class="text">bedrooms</span>
                        </span>
                                            <span class="object_label object_bath_rooms">
                            <span class="number">1</span>
                            <i class="fa fa-bath" aria-hidden="true"></i>
                            <span class="text">Bathroom</span>
                        </span>

                        <span class="object_label object_sqfeet">
                            <span class="number">63 m²</span>
                            <span class="text">Liveable area</span>
                        </span>






                                                            
                                            <span class="object_label object_fitment_upholstered">
                            <i class="fa fa-booth-curtain" aria-hidden="true"></i>
                            <span class="text">Upholstered</span>
                        </span>

                </a>
                <a class="obj_price" href="/residential-listings/rent/amsterdam/oude-leliestraat/8-d?forsaleorrent=1&amp;localityid=1290&amp;locationofinterest=Amsterdam&amp;take=12">
                            <span class="obj_price">
                                €2,350 /mo
                            </span>
                </a>
            </div>
        </div>
    </article>

"""

def scrape_website(html):
    soup = BeautifulSoup(html, 'html.parser')
    houses = []

    articles = soup.find_all('article', class_='objectcontainer col-12 col-xs-12 col-sm-6 col-md-6 col-lg-4')

    for article in articles:
        house = House()

        # Link and Images
        link_container = article.find('a', class_='img-container')
        if link_container:
            house.link = base_url + link_container['href']
            img_tag = link_container.find('img')
            if img_tag and 'src' in img_tag.attrs:
                house.images.append(img_tag['src'])

        # Address and City
        address_container = article.find('span', class_='street')
        city_container = article.find('span', class_='locality')
        if address_container and city_container:
            house.address = address_container.text.strip()
            house.city = city_container.text.strip()

        # Price
        price_container = article.find('span', class_='obj_price')
        if price_container:
            house.price = get_price(price_container.text.strip(), keep_comma=True)

        # Additional Details
        details_container = article.find_all('span', class_='object_label')
        for detail in details_container:
            label = detail.find('span', class_='text').text.strip()
            
            if detail.find('span', class_='number'):
                value = detail.find('span', class_='number').text.strip()    
                house.details[label] = value

        houses.append(house)

    return houses


website = Website(url, example_html, scrape_website)


# Run the scrape_example function to test the scraper
houses = website.scrape_example()


# Print the results
for house in houses[::-1]:
    house.print()
    print()


