from classes import *
import pickle
import os
from datetime import datetime
# from mongo import db


websites = []

from website_1 import website
websites.append(website)

from website_2 import website
websites.append(website)

from website_3 import website
websites.append(website)

from website_4 import website
websites.append(website)

from website_5 import website
websites.append(website)


existing_houses = []
if os.path.exists('file.pkl'):
    with open('file.pkl', 'rb') as file:
        existing_houses = pickle.load(file)
existing_addresses = [h.address for h in existing_houses]

all_houses = []

for website in websites:

    print("-----------")
    print(f"New website {website.url}")
    print("-----------")

    website.scrape_example()

    for idx, house in enumerate(website.houses, start=1):
        if idx == 1:
            print(f"House {idx} Info:")
            house.print()
        
        if 'Amsterdam' in house.address or 'Amsterdam' in house.city:
            if house.price < 1750:

                all_houses.append(house)


with open('webinterface/file.pkl', 'wb') as f:
    pickle.dump(all_houses, f)


added_houses = [house for house in all_houses if house.address not in existing_addresses]

print("--------------------")
print(f"Total houses: {len(all_houses)}")
print(f"New houses: {len(added_houses)}")
print("--------------------")


with open('webinterface/new_file.pkl', 'wb') as f:
    pickle.dump(added_houses, f)



