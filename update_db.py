from classes import *
import pickle
import os
from datetime import datetime
from mongo import db
import time
import pymongo
import get_websites
from maps import get_geodata



# Add argument to update price and link or geodata

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--update", help="update price and link or geodata",
                    choices=["price_and_link", "geodata", "email_sent_default", "fix_wrong_link"],
                    default=None)


args = parser.parse_args()


what_to_update = args.update



def get_all_houses_scraped():
    websites = get_websites.get_websites_list()
    all_houses = []

    for website in websites:
        print("-----------")
        print(f"New website {website.url}")
        print("-----------")

        houses = website.scrape_example()

        for i, house in enumerate(houses):

            all_houses.append(house)

    return all_houses

# Loop through the update values
if what_to_update == "price_and_link":

    all_houses = get_all_houses_scraped()
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
    
    db_houses = db.find()
    for house in db_houses:

        if 'place_id' not in house.get('geodata', {}).keys():

            geodata = get_geodata(house['address']+" "+house['city'])

            update_result = db.update_one({'link': house['link']},
                                        {'$set': {'geodata': geodata}})

            print(f"Updated {update_result.modified_count} house(s)")

if what_to_update == "email_sent_default":

    # If email_sent is not in the house, add it with an empty list
    update_result = db.update_many({"email_sent": {"$exists": False}}, {"$set": {"email_sent": []}})
    
    print(f"Updated {update_result.modified_count} house(s)")


if what_to_update == 'fix_wrong_link':

    # The links that contain the following string are wrong
    wrong_link = 'https://househunting.nlhttps://'

    # Let's find all the houses that have a link that contains the wrong link
    houses = db.find({'link': {'$regex': wrong_link}})
    for house in houses:
        # Replace the wrong link with the correct link
        new_link = house['link'].replace(wrong_link, 'https://')
        update_result = db.update_one({'link': house['link']}, {'$set': {'link': new_link}})
        print(f"Updated {update_result.modified_count} house(s)")

print("Finished updating")