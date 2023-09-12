from bs4 import BeautifulSoup
import sys
sys.path.append('../')
from classes import House, Website
from common import *


base_url = "https://www.expathousing.com"
url = "https://www.expathousing.com/availableproperties/"

example_html = """
<li class="listing listing-list col span_12 first ">
                            <figure class="col span_4 first">
                                <h6 class="snipe status for-rent  "><span>New For Rent </span></h6>                <span class="prop-type-icon"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="18" height="18" viewBox="0 0 20 20"> <path d="M19.871 12.165l-8.829-9.758c-0.274-0.303-0.644-0.47-1.042-0.47-0 0 0 0 0 0-0.397 0-0.767 0.167-1.042 0.47l-8.829 9.758c-0.185 0.205-0.169 0.521 0.035 0.706 0.096 0.087 0.216 0.129 0.335 0.129 0.136 0 0.272-0.055 0.371-0.165l2.129-2.353v8.018c0 0.827 0.673 1.5 1.5 1.5h11c0.827 0 1.5-0.673 1.5-1.5v-8.018l2.129 2.353c0.185 0.205 0.501 0.221 0.706 0.035s0.221-0.501 0.035-0.706zM12 19h-4v-4.5c0-0.276 0.224-0.5 0.5-0.5h3c0.276 0 0.5 0.224 0.5 0.5v4.5zM16 18.5c0 0.276-0.224 0.5-0.5 0.5h-2.5v-4.5c0-0.827-0.673-1.5-1.5-1.5h-3c-0.827 0-1.5 0.673-1.5 1.5v4.5h-2.5c-0.276 0-0.5-0.224-0.5-0.5v-9.123l5.7-6.3c0.082-0.091 0.189-0.141 0.3-0.141s0.218 0.050 0.3 0.141l5.7 6.3v9.123z" fill="#ffffff"></path> </svg></span>                <ul class="listing-actions"><li><span class="listing-images-count" data-tooltip="16 Photos"><i class="fa fa-image"></i></span></li><li><span class="listing-views" data-tooltip="7 Views"><i class="fa fa-bar-chart"></i></span></li></ul>                					<a class="listing-featured-image" href="https://www.expathousing.com/available-properties/orteliusstraat-1056-nv-amsterdam-3243/"><img src="https://www.expathousing.com/wp-content/uploads/2023/09/40136_original-14-818x540.jpg" class="attachment-listings-featured-image size-listings-featured-image wp-post-image entered lazyloaded" alt="" loading="lazy" data-lazy-src="https://www.expathousing.com/wp-content/uploads/2023/09/40136_original-14-818x540.jpg" data-ll-status="loaded"><noscript>&lt;img width="818" height="540" src="https://www.expathousing.com/wp-content/uploads/2023/09/40136_original-14-818x540.jpg" class="attachment-listings-featured-image size-listings-featured-image wp-post-image" alt="" loading="lazy" /&gt;</noscript></a>
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
                        <figure class="col span_1 first list-agent-image"><a href="https://www.expathousing.com/author/"><img class="author-img" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20749%20755'%3E%3C/svg%3E" data-lazy-src="https://www.expathousing.com/wp-content/themes/realestate-7/images/user-default.png"><noscript>&lt;img width="749" height="755" class="author-img" src="https://www.expathousing.com/wp-content/themes/realestate-7/images/user-default.png" /&gt;</noscript></a></figure>                        <div class="col span_5">
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


    articles = soup.find_all('li', class_='listing')

    for article in articles:

        house = House()

        # Link
        link_tag = article.find('a', class_='listing-featured-image')
        if link_tag:
            house.link = link_tag['href']

        # Image
        img_tag = article.find('img')
        if img_tag and 'data-lazy-src' in img_tag.attrs:
            house.images.append(img_tag['data-lazy-src'])


        # Address and City
        address_container = article.find('h4', class_='marT0 marB0 edited-')
        city_container = article.find('p', class_='location muted marB0')
        if address_container and city_container:
            house.city = city_container.text.strip()
            house.address = address_container.text.strip()

        # Price
        price_container = article.find('span', class_='listing-price')
        if price_container:
            house.price = get_price(price_container.text.strip())

        # Additional Details
        details_container = article.find_all('li', class_='row')
        for detail in details_container:
            label = detail.find('span', class_='muted left')
            if label:
                label = label.text.strip()
                value = detail.find('span', class_='right').text.strip()
                house.details[label] = value

        houses.append(house)

    return houses


website = Website(url, example_html, scrape_website)



# Run the scrape_example function to test the scraper
# houses = website.scrape_example()


# # # Print the results
# for house in houses[::-1]:
#     house.print()
#     print()


