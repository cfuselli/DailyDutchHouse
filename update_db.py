from classes import *
import pickle
import os
from datetime import datetime
from mongo import db
import time
import pymongo

websites = []

# They just updated the website ahaha
# from website_1 import website
# websites.append(website)

from website_2 import website
websites.append(website)

from website_3 import website
websites.append(website)

from website_4 import website
websites.append(website)

from website_5 import website
websites.append(website)


all_houses = []

for website in websites:
    print("-----------")
    print(f"New website {website.url}")
    print("-----------")

    houses = website.scrape_example()

    for i, house in enumerate(houses):

        all_houses.append(house)


# Loop through the update values
for house in all_houses:

    address = house.address
    city = house.city
    new_link = house.link
    new_price = house.price


        # Update house that matches the address and city
    update_result = db.update_one({"address": address, "city": city}, 
                                  {"$set": {"link": new_link, 
                                            "price": new_price}})
    
    print(f"Updated {update_result.modified_count} house(s)")


print("Finished updating")