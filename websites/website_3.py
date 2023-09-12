from bs4 import BeautifulSoup
from classes import House, Website
from common import *

url = "https://www.vanhuisuit-makelaars.nl/nl/aanbod/alle/huurwoningen-amsterdam"

example_html = """
<article class="result">
    <div class="result__visuals">
        <div class="offer-result-slider slick-initialized slick-slider"><button type="button" class="slick-prev slick-arrow" style="display: block;"><i class="far fa-arrow-left"></i></button>
                            <div aria-live="polite" class="slick-list draggable"><div class="slick-track" role="listbox" style="opacity: 1; width: 1770px; transform: translate3d(-354px, 0px, 0px);"><div class="offer-result-slide slick-slide slick-cloned" data-slick-index="-1" aria-hidden="true" tabindex="-1" style="width: 354px;">
                    <div class="offer-result-visual">
                        <img src="https://www.vanhuisuit-makelaars.nl/properties/img/5397731/3.jpg" loading="lazy" alt="">

                    </div>
                </div><div class="offer-result-slide slick-slide slick-current slick-active" data-slick-index="0" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide300" style="width: 354px;">
                    <div class="offer-result-visual">
                        <img src="https://www.vanhuisuit-makelaars.nl/properties/img/5397731/1.jpg" loading="lazy" alt="">

                    </div>
                </div><div class="offer-result-slide slick-slide" data-slick-index="1" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide301" style="width: 354px;">
                    <div class="offer-result-visual">
                        <img src="https://www.vanhuisuit-makelaars.nl/properties/img/5397731/2.jpg" loading="lazy" alt="">

                    </div>
                </div><div class="offer-result-slide slick-slide" data-slick-index="2" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide302" style="width: 354px;">
                    <div class="offer-result-visual">
                        <img src="https://www.vanhuisuit-makelaars.nl/properties/img/5397731/3.jpg" loading="lazy" alt="">

                    </div>
                </div><div class="offer-result-slide slick-slide slick-cloned" data-slick-index="3" aria-hidden="true" tabindex="-1" style="width: 354px;">
                    <div class="offer-result-visual">
                        <img src="https://www.vanhuisuit-makelaars.nl/properties/img/5397731/1.jpg" loading="lazy" alt="">

                    </div>
                </div></div></div>
                            
                            
                    <button type="button" class="slick-next slick-arrow" style="display: block;"><i class="far fa-arrow-right"></i></button></div>

                    <div class="status-label status-label--blue">
    Nieuw
</div>        
    </div>
    <h2 class="result__address">Bilderdijkkade 22 4<span>Amsterdam</span></h2>
    <strong class="result__price">€ 2.750,- </strong>
    <div class="content-split">
        <ul class="result__data-list">
            <li class="result__data-item">63 m²</li>
            <li class="result__data-item">1 slaapkamer(s)</li>
            <li class="result__data-item">Gemeubileerd</li>
        </ul>
        <a href="https://www.vanhuisuit-makelaars.nl/aanbod/amsterdam-west/detail/bilderdijkkade-224-amsterdam" class="button button--secondary">Bekijken</a>
    </div>
</article>
"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")
    property_elements = soup.find_all("article", class_="result")

    house_list = []

    for property_elem in property_elements:
        house = House()

        # Extract address and city
        address_elem = property_elem.find("h2", class_="result__address")
        if address_elem:
            address_text = address_elem.text.strip()
            parts = address_text.split()
            if len(parts) >= 2:
                house.address = " ".join(parts[:-1])
                house.city = parts[-1]

        # Extract price
        price_elem = property_elem.find("strong", class_="result__price")
        if price_elem:
            house.price = get_price(price_elem.text.strip())

        # Extract details
        details_elems = property_elem.find_all("li", class_="result__data-item")
        for detail_elem in details_elems:
            detail_text = detail_elem.text.strip()
            # Split the detail text into key and value if there's a space
            if " " in detail_text:
                key, value = detail_text.split(maxsplit=1)
                house.details[key] = value
            else:
                house.details[detail_text] = ""

        image_elems = property_elem.find_all("img", src=True)
        for image_elem in image_elems:
            house.images.append(image_elem["src"])

        # Extract link
        link_elem = property_elem.find("a", class_="button--secondary", href=True)
        if link_elem:
            house.link = link_elem["href"]

        house_list.append(house)

    return house_list


# Create an instance of the Website class for the third website
website = Website(url, example_html, scrape_website)
