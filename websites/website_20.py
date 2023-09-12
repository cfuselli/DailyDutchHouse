from bs4 import BeautifulSoup
import sys

sys.path.append("../")
from classes import House, Website
from common import *


base_url = "https://livresidential.nl"
url = "https://livresidential.nl/huurwoningen?range%5Bprice%5D=500%3A3500&refinementList%5Bcity%5D%5B0%5D=Amsterdam"

example_html = """

<a data-v-9ce6fcd4="" href="/huurwoningen/amsterdam/overtoomse-veld/marius-bauerstraat-30-g6" class="flex flex-col rounded hover:shadow border border-livgray-400 overflow-hidden"><div data-v-9ce6fcd4="" class="relative flex-shrink-0"><img data-v-9ce6fcd4="" alt="undefined in Amsterdam" class="h-48 w-full object-cover" data-src="https://cloud.livresidential.nl/26075/responsive-images/H6MiMtFLe5KzwvsHIv1JDbetMmliZ7RD7qEEIXXw___media_library_original_734_489.jpg" src="https://cloud.livresidential.nl/26075/responsive-images/H6MiMtFLe5KzwvsHIv1JDbetMmliZ7RD7qEEIXXw___media_library_original_734_489.jpg" lazy="loaded"> <!----></div> <div data-v-9ce6fcd4="" class="flex-1 bg-white p-5 border-b border-livgray-400 flex flex-col justify-between"><div data-v-9ce6fcd4="" class="flex-1"><p data-v-9ce6fcd4="" class="text-sm leading-5 font-medium text-c-500 mb-2">Appartement <!----></p> <h3 data-v-9ce6fcd4="" class="text-lg leading-7 font-bold text-c-800">
                    Marius Bauerstraat 30 G6
                </h3> <p data-v-9ce6fcd4="" class="text-base leading-6 text-c-500">
                    1062 AR Amsterdam
                </p> <p data-v-9ce6fcd4="" class="mt-3 text-base leading-5 font-medium text-c-700">
                    € 1.565 per maand
                    (excl.)</p></div></div> <div data-v-9ce6fcd4="" class="flex-1 bg-white flex flex-col justify-between"><div data-v-9ce6fcd4="" class="flex"><div data-v-9ce6fcd4="" class="flex items-center justify-center w-1/2 p-5 text-center border-r"><svg data-v-9ce6fcd4="" width="20" height="20" fill="none" xmlns="http://www.w3.org/2000/svg"><path data-v-9ce6fcd4="" d="M4.167 7.5l-2.5 2.5 2.5 2.5M7.5 4.167l2.5-2.5 2.5 2.5M12.5 15.834l-2.5 2.5-2.5-2.5M15.834 7.5l2.5 2.5-2.5 2.5M1.667 10h16.666M10 1.667v16.666" stroke="#6F7586" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg> <div data-v-9ce6fcd4="" class="ml-2 text-c-500">
                        55 <span data-v-9ce6fcd4="">m<sup>2</sup></span></div></div> <div data-v-9ce6fcd4="" class="flex items-center justify-center w-1/2 p-5"><svg data-v-9ce6fcd4="" width="20" height="20" fill="none" xmlns="http://www.w3.org/2000/svg"><path data-v-9ce6fcd4="" clip-rule="evenodd" d="M2.5 2.5h5.833v5.833H2.5V2.5zM11.666 2.5H17.5v5.833h-5.834V2.5zM11.666 11.666H17.5V17.5h-5.834v-5.834zM2.5 11.666h5.833V17.5H2.5v-5.834z" stroke="#6F7586" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg> <div data-v-9ce6fcd4="" class="ml-2 text-c-500">
                        3
                        kamers</div></div></div></div></a>

"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")

    houses = []

    articles = soup.find_all(
        "a",
        class_="flex flex-col rounded hover:shadow border border-livgray-400 overflow-hidden",
    )

    for article in articles:
        house = House()

        house.link = article["href"]

        # Find images
        image_container = article.find("img")
        if image_container:
            house.images.append(image_container["data-src"])

        # Address
        address_container = article.find(
            "h3", class_="text-lg leading-7 font-bold text-c-800"
        )
        if address_container:
            house.address = address_container.text.strip()

        # Address and City
        address_container = article.find("p", class_="text-base leading-6 text-c-500")
        if address_container:
            house.city = address_container.text.strip()

        # Price
        price_container = article.find(
            "p", class_="mt-3 text-base leading-5 font-medium text-c-700"
        )
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Additional Details
        details_container = article.find_all("div", class_="ml-2 text-c-500")
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
