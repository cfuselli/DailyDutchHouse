
from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *

url = "https://www.expathousing.com/?search-listings=true"

example_html = """
<li class="listing listing-list col span_12 first ">
                            <figure class="col span_4 first">
                                <h6 class="snipe status for-rent  "><span>New For Rent </span></h6>                <span class="prop-type-icon"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="18" height="18" viewBox="0 0 20 20"> <path d="M19.871 12.165l-8.829-9.758c-0.274-0.303-0.644-0.47-1.042-0.47-0 0 0 0 0 0-0.397 0-0.767 0.167-1.042 0.47l-8.829 9.758c-0.185 0.205-0.169 0.521 0.035 0.706 0.096 0.087 0.216 0.129 0.335 0.129 0.136 0 0.272-0.055 0.371-0.165l2.129-2.353v8.018c0 0.827 0.673 1.5 1.5 1.5h11c0.827 0 1.5-0.673 1.5-1.5v-8.018l2.129 2.353c0.185 0.205 0.501 0.221 0.706 0.035s0.221-0.501 0.035-0.706zM12 19h-4v-4.5c0-0.276 0.224-0.5 0.5-0.5h3c0.276 0 0.5 0.224 0.5 0.5v4.5zM16 18.5c0 0.276-0.224 0.5-0.5 0.5h-2.5v-4.5c0-0.827-0.673-1.5-1.5-1.5h-3c-0.827 0-1.5 0.673-1.5 1.5v4.5h-2.5c-0.276 0-0.5-0.224-0.5-0.5v-9.123l5.7-6.3c0.082-0.091 0.189-0.141 0.3-0.141s0.218 0.050 0.3 0.141l5.7 6.3v9.123z" fill="#ffffff"></path> </svg></span>                <ul class="listing-actions"><li><span class="listing-images-count" data-tooltip="16 Photos"><i class="fa fa-image"></i></span></li><li><span class="listing-views" data-tooltip="6 Views"><i class="fa fa-bar-chart"></i></span></li></ul>                					<a class="listing-featured-image" href="https://www.expathousing.com/available-properties/orteliusstraat-1056-nv-amsterdam-3243/"><img src="https://www.expathousing.com/wp-content/uploads/2023/09/40136_original-8-818x540.jpg" class="attachment-listings-featured-image size-listings-featured-image wp-post-image" alt="" loading="lazy"></a>
							            </figure>
                        <div class="list-listing-info col span_8 first">
                <div class="list-listing-info-inner">
                    <header>
                                                <h4 class="marT0 marB0 edited-"><a href="https://www.expathousing.com/available-properties/orteliusstraat-1056-nv-amsterdam-3243/">Orteliusstraat</a></h4>
                                                <p class="location muted marB0">
                            1056 NV, AMSTERDAM </p>
                    </header>
                                        <p class="price marB10"><span class="listing-price">€2.850</span></p>
                                        <p class="listing-list-excerpt marB0">Orteliusstraat (110m2) Baarsjes EUR 2,850.00 Exclusive G/W/E/Internet and TV
 
 Home suitable for family or couple + child/children!
 
 Property not suitable for sharers or students!
 
 Pets are not allowed for this property!
 
 Property has recently been renovated.
 
 Photos used for this advertisement are an impression of the house. There is no […]</p>
                    <ul class="propinfo propinfo-list marB0 padT0 CHILD_THEME">
                        <li class="property-type"><span class="muted left">Type:</span><span class="right">Appartement</span></li>
                                                <li class="row beds"><span class="muted left">Bedrooms</span><span class="right">3</span></li>                        <li class="property-size"><span class="muted left">Size:</span><span class="right">110.0 sq meters</span></li><li class=""><span class="muted left">Available From:</span><span class="right">01-09-2023</span></li>
                    </ul>
                    <div class="col span_12 first list-agent-info">
                        <figure class="col span_1 first list-agent-image"><a href="https://www.expathousing.com/author/"><img class="author-img" src="https://www.expathousing.com/wp-content/themes/realestate-7/images/user-default.png"></a></figure>                        <div class="col span_5">
                            <p class="muted marB0"><small>Agent</small></p>
                            <p class="marB0"><a href="https://www.expathousing.com/author/"> </a></p>
                        </div>
                        <div class="col span_5">
                                                    </div>
                    </div>
                    <div class="clear"></div>
                </div>
            </div>
                    </li>

"""


def scrape_website(html):

    soup = BeautifulSoup(html, 'html.parser')
    houses = []

    # Assuming each listing is contained within a 'li' tag with the class 'listing'
    listings = soup.find_all('li', class_='listing')

    for listing in listings:
        house = House()

        # URL and Image
        url_img_tag = listing.find('a', class_='listing-featured-image')
        if url_img_tag:
            house.link = url_img_tag['href']
            img_tag = url_img_tag.find('img')
            if img_tag and 'src' in img_tag.attrs:
                house.images.append(img_tag['src'])

        # Address
        address_tag = listing.find('h4')
        if address_tag:
            house.address = address_tag.text.strip()

        # Location
        location_tag = listing.find('p', class_='location')
        if location_tag:
            house.city = location_tag.text.strip()

        # Price
        price_tag = listing.find('span', class_='listing-price')
        if price_tag:
            price = get_price(price_tag.text.strip())
            house.price = price

        # Details
        prop_info_tags = listing.find_all('li')
        for tag in prop_info_tags:
            left_span = tag.find('span', class_='muted left')
            right_span = tag.find('span', class_='right')
            if left_span and right_span:
                key = left_span.text.strip().replace(':', '')
                value = right_span.text.strip()
                house.details[key] = value

        houses.append(house)

    return houses



website = Website(url, example_html, scrape_website)


# Run the scrape_example function to test the scraper
# houses = website.scrape_example()


# # Print the results
# for house in houses[::-1]:
#     house.print()
#     print()


