from bs4 import BeautifulSoup
from classes import House, Website
from common import *

url = "https://www.pararius.nl/huurwoningen/amsterdam"  # Replace with the actual URL
example_html = """
<section class="listing-search-item listing-search-item--list listing-search-item--featured">
                    <div class="listing-search-item__label">
                                        
            <span class="listing-label listing-label--featured">
            Uitgelicht
        </span>
    
                            </div>
        
        <div class="listing-search-item__depiction">
                            <a class="listing-search-item__link listing-search-item__link--depiction" href="/appartement-te-huur/amsterdam/c12bf29a/vrolikstraat" data-action="click->listing-search-item#onClick">
            
                    
        
    
    
    
    
                
    
    
        
    
    

    <wc-picture class="picture picture--listing-search-item picture--list" style="">
                                    
                            
            
                            
                        
        
    
                        <picture>
                                        
                                                                
                    <source srcset="https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=100&amp;auto=webp 100w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=200&amp;auto=webp 200w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=300&amp;auto=webp 300w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=400&amp;auto=webp 400w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=500&amp;auto=webp 500w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=600&amp;auto=webp 600w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=700&amp;auto=webp 700w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=800&amp;auto=webp 800w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=900&amp;auto=webp 900w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=1000&amp;auto=webp 1000w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=1100&amp;auto=webp 1100w, https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=1200&amp;auto=webp 1200w" sizes="(max-width: 767px) 90vw, 360px">
                
                    <img class="picture__image" alt="" src="https://casco-media-prod.global.ssl.fastly.net/c12bf29a-aa2f-577d-a6aa-d7cf24b75437/7f44a65e859cae5d77ec7a7d80554a23.jpg?width=600&amp;auto=webp" width="100%" height="100%">
                </picture></wc-picture>


                            </a>
                    </div>

        
        <h2 class="listing-search-item__title">
                            <a class="listing-search-item__link listing-search-item__link--title" href="/appartement-te-huur/amsterdam/c12bf29a/vrolikstraat" data-action="click->listing-search-item#onClick">
            
            Appartement Vrolikstraat 262 1

                            </a>
                    </h2>

        <div class="listing-search-item__sub-title'">
            1092 TX Amsterdam (Oosterparkbuurt)
        </div>

        
                    <div class="listing-search-item__price">
                €&nbsp;2.095 per maand
                            </div>
        
        <div class="listing-search-item__features">
            
                                        
                                
    
        
    <ul class="illustrated-features illustrated-features--compact">
                    <li class="illustrated-features__item illustrated-features__item--surface-area">58 m²</li>
                    <li class="illustrated-features__item illustrated-features__item--number-of-rooms">3 kamers</li>
                    <li class="illustrated-features__item illustrated-features__item--interior">Gestoffeerd</li>
            </ul>

                    </div>

        
                    <div class="listing-search-item__info">
                                                            <a class="listing-search-item__link" href="/makelaars/eindhoven/viadaan-nijmegen">ViaDaan</a>                                                </div>
        
        
        
        
            </section>"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")
    property_elements = soup.find_all("section", class_="listing-search-item")

    print(f"Found {len(property_elements)} properties")

    house_list = []

    for property_elem in property_elements:
        house = House()

        # Extract title and address
        title_elem = property_elem.find("h2", class_="listing-search-item__title")
        title_text = title_elem.text.strip()
        house.address = title_text

        sub_title_elem = property_elem.find(
            "div", class_="listing-search-item__sub-title'"
        )
        if sub_title_elem:
            house.city = sub_title_elem.text.strip()

        # Extract price
        price_elem = property_elem.find("div", class_="listing-search-item__price")
        if price_elem:
            price = get_price(price_elem.text.strip())
            house.price = price

        # Extract details
        features_elem = property_elem.find("ul", class_="illustrated-features")
        if features_elem:
            detail_items = features_elem.find_all(
                "li", class_="illustrated-features__item"
            )
            for detail_item in detail_items:
                key = detail_item.text.strip()
                house.details[key] = ""

        # Extract images from a more complex structure
        img_elem = property_elem.find(
            "img", class_="picture__image", alt=True, src=True
        )
        if img_elem:
            image_url = img_elem["src"]
            house.images.append(image_url)

        # Extract link
        link_elem = property_elem.find(
            "a", class_="listing-search-item__link--title", href=True
        )
        if link_elem:
            house.link = "https://www.pararius.nl" + link_elem["href"]

        house_list.append(house)

    return house_list


# Create an instance of the Website class for website 4
website = Website(url, example_html, scrape_website)
