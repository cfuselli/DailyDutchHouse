from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *

import requests

url = "https://www.smitenheinen.nl/woningaanbod/huur"
base_url = "https://www.smitenheinen.nl"

example_html = """


<article class=""><div class="relative shadow-card bg-white h-full"><div class="news-top-img relative"><div class="image-slider relative slick-initialized slick-slider"><div class="-right-0 z-10 top-auto fas fa-chevron-left absolute text-2xl pb-6 px-5 bottom-0 text-white mr-11 cursor-pointer arrow-shadow slick-arrow" style=""></div><div class="slick-list draggable"><div class="slick-track" style="opacity: 1; width: 3872px; transform: translate3d(-352px, 0px, 0px);"><div class="slick-slide slick-cloned" data-slick-index="-1" id="" aria-hidden="true" tabindex="-1" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="-1">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514551.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div><div class="slick-slide slick-current slick-active" data-slick-index="0" aria-hidden="false" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="0">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514539.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div><div class="slick-slide" data-slick-index="1" aria-hidden="true" tabindex="-1" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="-1">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514547.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div><div class="slick-slide" data-slick-index="2" aria-hidden="true" tabindex="-1" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="-1">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514607.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div><div class="slick-slide" data-slick-index="3" aria-hidden="true" tabindex="-1" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="-1">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514569.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div><div class="slick-slide" data-slick-index="4" aria-hidden="true" tabindex="-1" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="-1">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514551.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div><div class="slick-slide slick-cloned" data-slick-index="5" id="" aria-hidden="true" tabindex="-1" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="-1">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514539.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div><div class="slick-slide slick-cloned" data-slick-index="6" id="" aria-hidden="true" tabindex="-1" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="-1">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514547.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div><div class="slick-slide slick-cloned" data-slick-index="7" id="" aria-hidden="true" tabindex="-1" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="-1">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514607.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div><div class="slick-slide slick-cloned" data-slick-index="8" id="" aria-hidden="true" tabindex="-1" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="-1">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514569.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div><div class="slick-slide slick-cloned" data-slick-index="9" id="" aria-hidden="true" tabindex="-1" style="width: 352px;"><div><a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" aria-label="Eerste Hugo de Grootstraat 8 2 AMSTERDAM" class="relative block w-full h-full" style="width: 100%; display: inline-block;" tabindex="-1">
<img class="object-cover mx-auto" style="max-height:292px" loading="lazy" src="https://d7fj146x2b74d.cloudfront.net/wonen/450x300/146514551.jpg" width="450" height="280" alt="Eerste Hugo de Grootstraat 8(Amsterdam">
</a></div></div></div></div><div class="-right-0 z-10 top-auto fas fa-chevron-right absolute text-2xl pb-6 px-5 bottom-0 text-white cursor-pointer arrow-shadow slick-arrow" style=""></div></div>
<span class="status bg-primary text-white  px-4 py-2 font-bold   absolute top-0 right-0 block bg-status-beschikbaar">
Te huur
</span></div><div class="py-6 px-4 lg:px-8">
<span class="text-sm text-grey font-semibold">1052 KP Amsterdam</span><h3 class="mb-5 leading-none text-primary text-lg break-all">
<a class="text-primary hover:underline text-lg break-all" href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam">
Eerste Hugo de Grootstraat 8 2
</a></h3><span class="h4 font-sans text-grey block mb-14 font-bold w-full"><div class="grid"><div class=" order-2  ">
€ 2.250
p.m.                                                     <span class="text-md"></span></div></div>
</span><div class="absolute bottom-0 left-0 bg-grey-light pl-8 pr-3 w-full py-2"><div class="grid grid-cols-5"><div class="flex flex-row text-sm text-grey col-span-3"><div class="mr-3"><img src="/assets/images/default/icons/meters.svg" width="13" height="13" title="70m²" alt="70m²" class="inline mr-1">                                70 m²</div><div><img src="/assets/images/default/icons/kamers.svg" width="25" height="25" title="2 slaapkamers" alt="2 slaapkamers" class="inline">                                2</div></div><div class="col-span-2 text-sm">
<a href="/woningaanbod/huur/amsterdam/eerste-hugo-de-grootstraat-8-2-amsterdam" class="float-right font-semibold text-grey hover:underline">
Bekijk woning
<i class="ml-2 fas fa-chevron-right"></i></a></div></div></div></div></div></article>



"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all("article")

    for article in articles:
        house = House()

        link_container = article.find_all("a", href=True)
        if link_container:
            house.link = base_url + link_container[0]["href"]

        image_container = article.find("img")
        if image_container:
            house.images.append(image_container["src"])

        address_container = article.find(
            "span", class_="text-sm text-grey font-semibold"
        )
        if address_container:
            house.city = address_container.text.strip()

        city_container = article.find(
            "h3", class_="mb-5 leading-none text-primary text-lg break-all"
        )
        if city_container:
            house.address = city_container.text.strip()

        price_container = article.find("div", class_="grid")
        if price_container:
            house.price = get_price(price_container.text.strip())

        details_container = article.find_all(
            "div", class_="flex flex-row text-sm text-grey col-span-3"
        )
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
