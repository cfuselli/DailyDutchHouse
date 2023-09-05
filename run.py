from classes import *
import pickle
import os
from datetime import datetime
from mongo import db
import time
import pymongo

websites_list = []

from websites.website_1 import website
websites_list.append(website)

from websites.website_2 import website
websites_list.append(website)

from websites.website_3 import website
websites_list.append(website)

from websites.website_4 import website
websites_list.append(website)

from websites.website_5 import website
websites_list.append(website)

def scrape_and_insert():
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

    print("--------------------")
    print(f"Total houses: {len(all_houses)}")
    print(f"New houses: {len(add_houses)}")
    print(f"House counter: {house_n}")  # Print the final house counter
    print("--------------------")

    add_dicts = [house.to_dict() for house in add_houses]

    if add_dicts:
        db.insert_many(add_dicts)

    print(f"Added {len(add_houses)} houses to the database")
    print(datetime.now())


# Run the script in an infinite loop
while True:
    try:
        scrape_and_insert()
        # Sleep for an hour (3600 seconds) before running again
        time.sleep(300)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(60)
