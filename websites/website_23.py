from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *

import requests

url = "https://jlgrealestate.com/woningen/?#JYtBCsAgDMD-0rMHEXbpb6oV5lCUamFD_Ptku4WQTCiVKQNCk3R1MFCFo_hnm4-QejBNfU6BRopMQwty7GGnp6r8G04odO_HHdbCWi8"
base_url = "https://jlgrealestate.com"

example_html = """
<article class="card card--wonen card--has-image card--has-overlay card--has-content">
	<div class="card__inner">
		<a href="https://jlgrealestate.com/woningen/huur/vinkeveen/molenkade-20r26/" class="card__overlay u-z3">
			<span class="u-vh">Bekijk de detail pagina van huur Vinkeveen Molenkade 20R26</span>
		</a>

		<figure class="card__figure">
						<div class="card__tags">
				<span class="card__type card__tag back-white">huur</span>
									<span class="card__neighbourhood card__tag back-green color-white">Vinkeveen</span>
							</div>
						<div class="card__slider card__slider--list js--wonen-list-flickity" data-flickity="{ &quot;cellAlign&quot;: &quot;left&quot;, &quot;contain&quot;: true, &quot;lazyLoad&quot;: true, &quot;resize&quot;: true, &quot;draggable&quot;: false}">
														<img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/wonen-list-thumb.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942101-480x480.jpg" alt="">
														<img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/wonen-list-thumb.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942107-480x480.jpg" alt="">
														<img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/wonen-list-thumb.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942113-480x480.jpg" alt="">
														<img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/wonen-list-thumb.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942119-480x480.jpg" alt="">
														<img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/wonen-list-thumb.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942125-480x480.jpg" alt="">
														<img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/wonen-list-thumb.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942129-480x480.jpg" alt="">
							</div>
			<div class="card__slider card__slider--grid js--wonen-grid-flickity flickity-enabled" data-flickity="{ &quot;cellAlign&quot;: &quot;left&quot;, &quot;contain&quot;: true, &quot;lazyLoad&quot;: true, &quot;resize&quot;: true, &quot;draggable&quot;: false}" tabindex="0">
														
														
														
														
														
														
							<div class="flickity-viewport" style="height: 268.875px; touch-action: pan-y;"><div class="flickity-slider" style="left: 0px; transform: translateX(0%);"><img class="card__image flickity-lazyloaded is-selected" src="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942101-480x352.jpg" alt="" style="position: absolute; left: 0%;"><img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/thumbnail.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942107-480x352.jpg" alt="" style="position: absolute; left: 100%;" aria-hidden="true"><img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/thumbnail.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942113-480x352.jpg" alt="" style="position: absolute; left: 200%;" aria-hidden="true"><img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/thumbnail.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942119-480x352.jpg" alt="" style="position: absolute; left: 300%;" aria-hidden="true"><img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/thumbnail.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942125-480x352.jpg" alt="" style="position: absolute; left: 400%;" aria-hidden="true"><img class="card__image" src="https://jlgrealestate.com/app/themes/jlg/assets/placeholders/thumbnail.svg" data-flickity-lazyload="https://jlgrealestate.com/app/uploads/realworks/wonen/7.225.959/154942129-480x352.jpg" alt="" style="position: absolute; left: 500%;" aria-hidden="true"></div></div><button class="flickity-button flickity-prev-next-button previous" type="button" disabled="" aria-label="Previous"><svg class="flickity-button-icon" viewBox="0 0 100 100"><path d="M 10,50 L 60,100 L 70,90 L 30,50  L 70,10 L 60,0 Z" class="arrow"></path></svg></button><button class="flickity-button flickity-prev-next-button next" type="button" aria-label="Next"><svg class="flickity-button-icon" viewBox="0 0 100 100"><path d="M 10,50 L 60,100 L 70,90 L 30,50  L 70,10 L 60,0 Z" class="arrow" transform="translate(100, 100) rotate(180) "></path></svg></button><ol class="flickity-page-dots"><li class="dot is-selected" aria-label="Page dot 1" aria-current="step"></li><li class="dot" aria-label="Page dot 2"></li><li class="dot" aria-label="Page dot 3"></li><li class="dot" aria-label="Page dot 4"></li><li class="dot" aria-label="Page dot 5"></li><li class="dot" aria-label="Page dot 6"></li></ol></div>
			<figcaption class="u-vh">Kleine gallerij voor huur Vinkeveen Molenkade 20R26</figcaption>
		</figure>
		
		<div class="card__content back-white color-gray-80">
			<div class="group u-contain">
				<div class="card__heading heading semi puny">
					<h2>Molenkade 20R26</h2>
				</div>
				<div class="card__prose prose clean">
					<p>3645 AX, Vinkeveen</p>
				</div>

									<div class="card__price prose median clean tiny color-gray-100">
						<p>€ 2.000,- p/m</p>
					</div>
							</div>
			<div class="card__footer group color-gray-100"><ul class="card__list"><li class="card__item"><span class="card__icon card__icon--surface fill-brown-100"><svg class="svg" aria-hidden="true"><use xlink:href="#icon-surface"></use></svg></span><span class="card__text">76</span></li><li class="card__item"><span class="card__icon card__icon--surface fill-brown-100"><svg class="svg" aria-hidden="true"><use xlink:href="#icon-bedroom"></use></svg></span><span class="card__text">2</span></li><li class="card__item"><span class="card__icon card__icon--surface fill-brown-100"><svg class="svg" aria-hidden="true"><use xlink:href="#icon-furnished"></use></svg></span><span class="card__text">Gestoffeerd</span></li></ul></div>		</div>
	</div>
</article>


"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all(class_="card")

    for article in articles:
        print("ciao")
        house = House()

        # Link
        link_container = article.find("a")
        if link_container:
            house.link = link_container["href"]

        # Images
        image_container = article.find("img")
        if image_container:
            house.images.append(image_container["data-flickity-lazyload"])

        # Address
        address_container = article.find("h2")
        if address_container:
            house.address = address_container.text.strip()

        # City
        city_container = article.find("div", class_="card__prose prose clean")
        if city_container:
            house.city = city_container.text.strip()

        # Price
        price_container = article.find(
            "div", class_="card__price prose median clean tiny color-gray-100"
        )
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Details
        details_container = article.find_all("li", class_="card__item")
        try:
            house.details["m2"] = details_container[0].text.strip()
            house.details["kamers"] = details_container[1].text.strip()
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
