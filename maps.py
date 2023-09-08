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


def get_geodata(query):

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

            print("Returned no features, trying combinations")
            combs = get_missing_words_combi(query)
            for i,comb in enumerate(combs):
                print(f"Trying combination {i+1}/{len(combs)}")
                url = template.format(comb)
                data = requests.get(url).json()
                if len(data['features']) > 0:
                    result = data['features'][0]['properties']['geocoding']
                    result['coordinates'] = data['features'][0]['geometry']['coordinates']

                    return result
                
            print(f"Returned no features for query {query}")
            print(json.dumps(data, indent=4))
            return {}
    else:

        print("Something went wrong")
        print(house.link)
        print(json.dumps(data, indent=4))
        return {}


def get_missing_words_combi(query):

    from itertools import combinations

    # Input string containing words
    input_string = query.replace('+', ' ')

    # Split the input string into words
    words = input_string.split()

    # Generate all combinations of indices for one missing word
    combinations_indices_one_missing = list(combinations(range(len(words)), 1))

    # Generate all combinations of indices for two missing words
    combinations_indices_two_missing = list(combinations(range(len(words)), 2))

    # Generate all combinations of indices for three missing words
    combinations_indices_three_missing = list(combinations(range(len(words)), 3))

    # Generate a list of strings with one missing word for each combination
    missing_word_strings_one_missing = []
    for indices in combinations_indices_one_missing:
        missing_words = words.copy()
        for index in indices:
            missing_words[index] = ""
        missing_word_string = " ".join(missing_words)
        missing_word_strings_one_missing.append(missing_word_string)

    # Generate a list of strings with two missing words for each combination
    missing_word_strings_two_missing = []
    for indices in combinations_indices_two_missing:
        missing_words = words.copy()
        for index in indices:
            missing_words[index] = ""
        missing_word_string = " ".join(missing_words)
        missing_word_strings_two_missing.append(missing_word_string)

    # Generate a list of strings with three missing words for each combination
    missing_word_strings_three_missing = []
    for indices in combinations_indices_three_missing:
        missing_words = words.copy()
        for index in indices:
            missing_words[index] = ""
        missing_word_string = " ".join(missing_words)
        missing_word_strings_three_missing.append(missing_word_string)

    # Combine the lists of strings with one, two, and three missing words
    combined_missing_word_strings = (
        missing_word_strings_one_missing
        + missing_word_strings_two_missing
        + missing_word_strings_three_missing
    )

    combined_missing_word_strings = [c.replace(' ', '+') for c in combined_missing_word_strings]

    return combined_missing_word_strings

test = False
if test:

    print("Testing get_geodata()")
    query = "Beethovenstraat IV  1077 JA Amsterdam"
    query = clean_string(query)
    url = template.format(query)
    data = requests.get(url).json()
    print(json.dumps(data, indent=4))

    for f in data['features']:

        print(query)
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