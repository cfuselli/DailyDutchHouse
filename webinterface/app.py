from flask import Flask, render_template, request
import re
import pickle
import pymongo
import json

import sys
sys.path.append('../')
from classes import *
from mongo import db

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    with open('../secrets/secrets.json', 'r') as config_file:
        secrets = json.load(config_file)

    if request.method == 'POST':

        # Get the MongoDB query from the form input field
        query_text = request.form.get('query', '')
        
        if query_text == '':
            query_text = "{}"

        # Execute the MongoDB query and fetch the results
        try:
            houses = db.find(eval(query_text)).sort("date", pymongo.DESCENDING)
        except Exception as e:
            error_message = str(e)
            houses = []
        else:
            error_message = None

        return render_template('index.html', 
                               houses=houses, 
                               query_text=query_text,
                               error_message=error_message,
                               api_key_geoapify=secrets['api_key_geoapify'])

    houses = db.find().sort("date", pymongo.DESCENDING)
    houses = [house for house in houses]

    print(f"Total houses: {len(houses)}")

    return render_template('index.html', houses=houses, api_key_geoapify=secrets['api_key_geoapify'])

if __name__ == '__main__':
    print("Starting Flask server...")


    app.run(debug=True)
