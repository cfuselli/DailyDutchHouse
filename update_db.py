from classes import *
import pickle
import os
from datetime import datetime
from mongo import db
import time
import pymongo
import get_websites
from maps import get_geodata

websites = get_websites.get_websites_list()

all_houses = []

what_to_update = "geodata"

for website in websites:
    print("-----------")
    print(f"New website {website.url}")
    print("-----------")

    houses = website.scrape_example()

    for i, house in enumerate(houses):

        all_houses.append(house)



# Loop through the update values
if what_to_update == "price_and_link":
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

if what_to_update == "geodata":
    for house in all_houses:

        # check if the geodata['place_id'] exists

        get_house = db.find_one({'link': house.link})

        if 'place_id' not in get_house.get('geodata', {}).keys():

            geodata = get_geodata(house)

            update_result = db.update_one({'link': house.link},
                                        {'$set': {'geodata': geodata}})

            print(f"Updated {update_result.modified_count} house(s)")


print("Finished updating")