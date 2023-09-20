from classes import *
import pickle
import os
from datetime import datetime
import time
import pymongo

from mongo import db
from maps import get_geodata

import get_websites
import importlib


def scrape_and_insert(websites_list):
    all_houses = []
    add_houses = []

    # Query the last inserted house number from the database
    last_house = db.find_one({}, sort=[("house_n", pymongo.DESCENDING)])

    if last_house:
        house_n = last_house.get("house_n", 0) + 1
    else:
        house_n = 1  # Initialize to 1 if there are no existing houses

    for website in websites_list:

        
        print("-----------")
        print(f"New website {website.url}")
        print("-----------")

        try:

            website.scrape_example()

            for i, house in enumerate(website.houses):
                if i == 1:
                    print(f"House info:")
                    house.print()

                existing_house = db.find_one({"link": house.link})

                if not existing_house:
                    # Add the current date and house number to the house data
                    house.date = datetime.now()
                    house.house_n = house_n
                    add_houses.append(house)

                    # Increment the house number and update the last inserted house number in the database
                    house_n += 1

                all_houses.append(house)

        except Exception as e:
            print(f"An error occurred: {e}")
            
    print("--------------------")
    print(f"Total houses: {len(all_houses)}")
    print(f"New houses: {len(add_houses)}")
    print(f"House counter: {house_n}")  # Print the final house counter
    print("--------------------")

    add_dicts = [house.to_dict() for house in add_houses]

    # Populate geodata
    for house in add_dicts:
        geodata = get_geodata(house["address"] + " " + house["city"])
        house["geodata"] = geodata

    if add_dicts:
        db.insert_many(add_dicts)

    print(f"Added {len(add_houses)} houses to the database")
    print(datetime.now())


# Run the script in an infinite loop
while True:
    try:
        importlib.reload(get_websites)
        websites_list = get_websites.get_websites_list()
        scrape_and_insert(websites_list)
        # Sleep for an hour (3600 seconds) before running again
        time.sleep(60)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(60)
