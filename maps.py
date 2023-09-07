import requests
import json
import re
import time

# See here for very useful nominatim manual
# https://nominatim.org/release-docs/develop/api/Search/

template = "https://nominatim.openstreetmap.org/search?q={}&format=geocodejson&addressdetails=1&countrycodes=nl&layers=address&limit=1"

api_key_geoapify = json.load(open('secrets/secrets.json', 'r'))['api_key_geoapify']

def clean_string(city_address):
    stopwords = ['appartement', 'huis', 'project', 'house']
    querywords = city_address.split()

    new_querywords = []
    for queryword in querywords:
        if 'Amsterdam' in queryword:
                new_querywords.append('Amsterdam')
        else:
            new_querywords.append(queryword)

    querywords = new_querywords

    seen = set()
    result = []
    for item in querywords:
        if item not in seen:
            seen.add(item)
            result.append(item)

    querywords = result

    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    city_address = ' '.join(resultwords)

    city_address = re.sub("[\(\[].*?[\)\]]", "", city_address)
    city_address = city_address.replace('-', ' ')
    city_address = city_address.replace(' ', '+')

    return city_address


def get_geodata(house):

    try:
        address = house['address']
        city = house['city']
    except:
        address = house.address
        city = house.city
    query = (address+' '+city)
    query = clean_string(query)
    url = template.format(query)
    data = requests.get(url).json()

    # Wait one second to be nice to the API
    time.sleep(1)

    if len(data) > 0:
        # print("Returned more than one result")
        # print(json.dumps(data, indent=4))

        if len(data['features']) > 0:
            result = data['features'][0]['properties']['geocoding']
            result['coordinates'] = data['features'][0]['geometry']['coordinates']

            return result
        
        else:
            print("Returned no features")
            print(house.link)
            print(json.dumps(data, indent=4))
            return {}
    else:

        print("Returned no results")
        print(house.link)
        print(json.dumps(data, indent=4))
        return {}



test = False
if test:
    from mongo import db
    houses = db.find()
    houses = [house for house in houses]
    print(f"Found {len(houses)} houses")

    for i,house in enumerate(houses[::-1]):
        address = house['address']
        city = house['city']
        query = (address+' '+city)
        query = clean_string(query)
        url = template.format(query)
        data = requests.get(url).json()

        for f in data['features']:

            print(house['address'])
            print(house['city'])
            print(f['properties']['geocoding']['label'])
            print(f['geometry']['coordinates'])
            print()

        time.sleep(1.1)


# https://maps.geoapify.com/v1/staticmap?style=osm-carto&width=600&height=400&center=lonlat:4.8911942,52.3663442&zoom=13&apiKey={api_key_geoapify}&marker=lonlat:4.8911942,52.3663442

# <img width="600" height="400" 
# src="https://maps.geoapify.com/v1/staticmap?style=osm-carto&width=600&height=400&center=lonlat:4.8911942,52.3663442&zoom=13&apiKey={api_key_geoapify}&marker=lonlat:4.8911942,52.3663442">

# {
#     "type": "Feature",
#     "properties": {
#         "geocoding": {
#             "place_id": 169856536,
#             "osm_type": "way",
#             "osm_id": 1078654527,
#             "osm_key": "highway",
#             "osm_value": "residential",
#             "type": "street",
#             "label": "Middenweg, Betondorp, Oost, Amsterdam, Noord-Holland, Nederland, 1097 VB, Nederland",
#             "name": "Middenweg",
#             "postcode": "1097 VB",
#             "locality": "Betondorp",
#             "district": "Oost",
#             "city": "Amsterdam",
#             "state": "Noord-Holland",
#             "country": "Nederland",
#             "country_code": "nl",
#             "admin": {
#                 "level10": "Amsterdam",
#                 "level8": "Amsterdam",
#                 "level4": "Noord-Holland",
#                 "level3": "Nederland"
#             }
#         }
#     },
#     "geometry": {
#         "type": "Point",
#         "coordinates": [
#             4.9477449,
#             52.3427972
#         ]
#     }
# }