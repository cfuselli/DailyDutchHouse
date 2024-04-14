from bs4 import BeautifulSoup
from classes import House, Website
from common import *

url = """https://www.funda.nl/zoeken/huur/?selected_area=%5B%22amsterdam%22%5D&sort=%22date_down%22"""  # Replace with the actual URL


example_html = """
<div data-test-id="search-result-item" class="bg-white" data-v-71621df9=""><div class="sm:flex" data-v-71621df9=""><a data-test-id="object-image-link" href="https://www.funda.nl/huur/amsterdam/appartement-42212987-johannes-verhulststraat-90-c/" class="h-full min-w-[228px] shrink-0 cursor-pointer" data-v-71621df9=""><div class="relative overflow-hidden rounded md:h-full" data-v-71621df9=""><div data-v-71621df9=""><div class="h-full w-full"><img alt="Johannes Verhulststraat 90 main image" loading="lazy" sizes="(min-width: 500px) 228px, calc(100vw - 2rem)" srcset="https://cloud.funda.nl/valentina_media/179/351/342_180x120.jpg 180w,https://cloud.funda.nl/valentina_media/179/351/342_360x240.jpg 360w,https://cloud.funda.nl/valentina_media/179/351/342_720x480.jpg 720w" height="148" width="216" class="w-full sm:h-full rounded"> <!----></div></div> <ul class="absolute left-2 top-2 flex w-56 flex-wrap" data-v-71621df9=""></ul> <div class="absolute right-0 flex w-fit flex-wrap bg-gradient-to-r from-transparent to-[#0000005c] py-0.5 text-right md:left-0 md:from-[#0000005c] md:to-transparent md:text-left bottom-0 md:bottom-1" data-v-71621df9=""><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" role="presentation" viewBox="0 0 48 48" class="mr-[0.1rem] h-5 w-5 text-white first:ml-[0.2rem] last:mr-[0.2rem]"><path d="M42 7.5A1.5 1.5 0 0040.5 6h-33A1.5 1.5 0 006 7.5v33A1.5 1.5 0 007.5 42H18v-3H9V9h30v30h-7.76L20.8 28.56l-2.12 2.12L30 42h10.5a1.5 1.5 0 001.5-1.5v-33z"></path></svg> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" role="presentation" viewBox="0 0 48 48" class="mr-[0.1rem] h-5 w-5 text-white first:ml-[0.2rem] last:mr-[0.2rem]"><path d="M42 9.5A1.5 1.5 0 0040.5 8h-10A1.5 1.5 0 0029 9.5v10a1.5 1.5 0 003 0v-7a14 14 0 11-8-2.5V7a17 17 0 1010.92 4h5.58A1.5 1.5 0 0042 9.5z" data-name="360"></path></svg> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" role="presentation" viewBox="0 0 48 48" class="mr-[0.1rem] h-5 w-5 text-white first:ml-[0.2rem] last:mr-[0.2rem]"><path d="M39.16 23.19a1.48 1.48 0 00-.51-.48l-.11-.09L13.32 6.24l-.16-.08h-.09l-.18-.06h-.11L12.6 6H12.19a1.49 1.49 0 00-1 .65 1.47 1.47 0 00-.1.2 1.46 1.46 0 00-.07.21v.08a1.48 1.48 0 000 .2V40.52a1.49 1.49 0 000 .2v.08a1.46 1.46 0 00.07.21 1.48 1.48 0 00.11.21 1.49 1.49 0 001 .65H12.9l.18-.06h.08l.16-.08 25.41-16.5a1.5 1.5 0 00.43-2.04zM14 10.26L35.16 24 14 37.74z"></path></svg></div></div></a> <div class="sm:ml-4 w-full pr-2 min-w-0" data-v-71621df9=""><div class="flex justify-between" data-v-71621df9=""><div class="min-w-0" data-v-71621df9=""><a href="https://www.funda.nl/huur/amsterdam/appartement-42212987-johannes-verhulststraat-90-c/" class="text-blue-2 visited:text-purple-1 cursor-pointer"><h2 data-test-id="street-name-house-number" class="mt-4 font-semibold sm:mt-0">
            Johannes Verhulststraat 90 C
        </h2> <div data-test-id="postal-code-city" class="text-dark-1 mb-2">
            1071 NK Amsterdam
        </div></a> <p data-test-id="price-rent" class="font-semibold">
        € 10.000 /maand
    </p> <!----> <ul class="mt-1 flex h-6 min-w-0 flex-wrap overflow-hidden"><li class="mr-4 flex flex-[0_0_auto]"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" role="presentation" viewBox="0 0 48 48" class="flex-0 mr-2"><path d="M38.5 32.25v-16.5a5 5 0 10-6.25-6.25h-16.5a5 5 0 10-6.25 6.25v16.5a5 5 0 106.25 6.25h16.5a5 5 0 106.25-6.25zm-6.25 3.25h-16.5a5 5 0 00-3.25-3.25v-16.5a5 5 0 003.25-3.25h16.5a5 5 0 003.25 3.25v16.5a5 5 0 00-3.25 3.25zM37 9a2 2 0 11-2 2 2 2 0 012-2zM11 9a2 2 0 11-2 2 2 2 0 012-2zm0 30a2 2 0 112-2 2 2 0 01-2 2zm26 0a2 2 0 112-2 2 2 0 01-2 2z"></path></svg>
            175 m²
        </li> <!----> <li class="mr-4 flex flex-[0_0_auto]"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" role="presentation" viewBox="0 0 48 48" class="flex-0 mr-2"><path d="M11 20l-3.999 5.999h33.998L37 20h3l3.999 5.999L44 26v9.5a1.5 1.5 0 01-1.5 1.5H39v1.5a1.5 1.5 0 01-3 0V37H12v1.5a1.5 1.5 0 01-3 0V37H5.5A1.5 1.5 0 014 35.5V26l.001-.001L8 20h3zm30 9H7v5h34v-5zM38.5 8A1.5 1.5 0 0140 9.5V20l-9-.001V21.5a1.5 1.5 0 01-1.5 1.5h-11a1.5 1.5 0 01-1.5-1.5v-1.501L8 20V9.5A1.5 1.5 0 019.5 8h29zM28 17h-8v3h8v-3zm9-6H11v5.999h6V15.5a1.5 1.5 0 011.5-1.5h11a1.5 1.5 0 011.5 1.5v1.499h6V11z"></path></svg>
            3
        </li> <li class="flex flex-[0_0_auto]"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" role="presentation" viewBox="0 0 48 48" class="flex-0 mr-2"><path d="M23.675 12.891l-6.852 13.063 7.032 1.628.492 7.872 7.31-13.373-7.51-1.63-.472-7.56zm2.45-8.897L27 18l6.274 1.362c1.62.351 2.295 1.818 1.5 3.274l-11.82 21.618c-.529.968-1.01.853-1.079-.248L21 30l-5.714-1.323c-1.612-.373-2.3-1.868-1.529-3.337L25.073 3.767c.511-.975.983-.874 1.052.227z"></path></svg>
            A++++
        </li> <!----></ul></div> <div class="mt-4 flex flex-row-reverse sm:mt-0" data-v-71621df9=""><button class="flex"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" role="presentation" viewBox="0 0 48 48" alt="Huis bewaren" class="text-blue-2"><path d="M39 9.86A10.17 10.17 0 0032 7a9.9 9.9 0 00-6 2 10.1 10.1 0 00-2 2 10.1 10.1 0 00-2-2 9.91 9.91 0 00-12 0 9.9 9.9 0 00-4 8c0 15 16 24 18 24s18-9 18-24a10 10 0 00-3-7.14zm-15 28a29.61 29.61 0 01-12.72-12.1A18.77 18.77 0 019 17a7 7 0 0113.41-2.81c.06.14.11.29.17.44a1.49 1.49 0 002.82 0c.05-.15.11-.3.17-.44A7 7 0 0139 17a18.77 18.77 0 01-2.28 8.81A29.61 29.61 0 0124 37.91z"></path></svg></button> <!----> <!----> <!----></div></div> <div class="mt-4 flex" data-v-71621df9=""><a href="https://www.funda.nl/makelaars/amsterdam/24131-de-graaf-en-groot-makelaars/" class="text-blue-2 min-w-0 cursor-pointer truncate" data-v-71621df9="">
                    De Graaf &amp; Groot Makelaars
                </a> <div class="ml-auto" data-v-71621df9=""><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" role="presentation" viewBox="0 0 48 48"><path fill="#005AD2" d="M10.626 35l5.452 5.342v-5.184H18V44h-.64l-5.439-5.368v5.21H10V35h.626zm10.546 0l2.342 5.357L25.842 35H28l-4.174 9h-.639L19 35h2.172zm8.44 0l3.888 4.781L37.387 35H38v9h-1.88v-4.714l-2.313 2.786h-.614l-2.312-2.786V44H29v-9h.613zm6.34-31C37.084 4 38 4.901 38 6.012v24.873C38 31.5 37.491 32 36.865 32h-6.24a1.125 1.125 0 01-1.135-1.115v-8.541c0-1.269 1.046-2.297 2.336-2.297h.233c2.11 0 3.823-1.682 3.823-3.758 0-2.077-1.712-3.759-3.823-3.759-2.11 0-3.822 1.682-3.822 3.759l.013 14.596c0 .616-.508 1.115-1.136 1.115h-6.229a1.125 1.125 0 01-1.135-1.115l.013-14.596c0-2.077-1.71-3.759-3.822-3.759-2.111 0-3.823 1.682-3.823 3.759 0 2.076 1.712 3.758 3.823 3.758h.233c1.29 0 2.336 1.028 2.336 2.297v8.54c0 .617-.508 1.116-1.135 1.116h-6.24A1.125 1.125 0 0110 30.885V6.012C10 4.902 10.917 4 12.047 4l8.415.01c1.647 0 2.982 1.313 2.982 2.931l-.151.049c-1.741.327-3.056 1.832-3.056 3.639 0 1.98 1.58 3.597 3.568 3.7l.195.004.195-.005c1.988-.102 3.568-1.72 3.568-3.7 0-1.806-1.316-3.311-3.056-3.638l-.152-.049c0-1.618 1.336-2.931 2.982-2.931L35.953 4z"></path></svg> <!----> <!----> <!----></div></div></div></div> <!----></div>"""


def scrape_website(html):
    soup = BeautifulSoup(html, "html.parser")
    property_elements = soup.find_all("div", {"data-test-id": "search-result-item"})

    print(f"Found {len(property_elements)} properties")

    house_list = []

    for property_elem in property_elements:
        house = House()

        # Extract street name and house number
        street_name_elem = property_elem.find(
            "h2", {"data-test-id": "street-name-house-number"}
        )
        if street_name_elem:
            house.address = street_name_elem.text.strip()

        # Extract postal code and city
        postal_code_elem = property_elem.find(
            "div", {"data-test-id": "postal-code-city"}
        )
        if postal_code_elem:
            house.city = postal_code_elem.text.strip()

        # Extract price
        price_elem = property_elem.find("p", {"data-test-id": "price-rent"})
        if price_elem:
            price = get_price(price_elem.text.strip())
            house.price = price

        # Extract details
        details_elems = property_elem.find_all("li", {"class": "flex-[0_0_auto]"})
        for detail_elem in details_elems:
            detail_text = detail_elem.text.strip()

            # Split the detail text into key and value if there's a space
            if " " in detail_text:
                key, value = detail_text.split(maxsplit=1)
                house.details[key] = value
            else:
                house.details[detail_text] = ""

        # Extract images
        img_elem = property_elem.find("img", alt=True, srcset=True)
        if img_elem:
            srcset = img_elem["srcset"]
            # Split the srcset into individual image URLs
            srcset_parts = srcset.split(",")
            for srcset_part in srcset_parts:
                # Extract the URL from the srcset part
                image_url = srcset_part.split()[-2].strip()
                house.images.append(image_url)

        # Extract link
        link_elem = property_elem.find(
            "a", {"data-test-id": "object-image-link"}, href=True
        )
        if link_elem:
            house.link = link_elem["href"]

        house_list.append(house)

    return house_list


# Create an instance of the Website class for the new website
website = Website(url, example_html, scrape_website)
