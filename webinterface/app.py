from flask import Flask, render_template, request
import re
import pickle
import pymongo
import json
from datetime import datetime, timedelta

import sys

sys.path.append("../")
from classes import *
from mongo import db

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    with open("../secrets/secrets.json", "r") as config_file:
        secrets = json.load(config_file)

    if request.method == "POST":
        # Get the MongoDB query from the form input field
        query_text = request.form.get("query", "")

        if query_text == "":
            query_text = "{}"

        # Execute the MongoDB query and fetch the results
        try:
            houses = db.find(eval(query_text)).sort("date", pymongo.DESCENDING)
        except Exception as e:
            error_message = str(e)
            houses = []
        else:
            error_message = None

        return render_template(
            "index.html",
            houses=houses,
            query_text=query_text,
            error_message=error_message,
            api_key_geoapify=secrets["api_key_geoapify"],
        )

    houses = db.find().sort("date", pymongo.DESCENDING)
    houses = [house for house in houses]

    print(f"Total houses: {len(houses)}")

    return render_template(
        "index.html", houses=houses, api_key_geoapify=secrets["api_key_geoapify"]
    )


from urllib.parse import urlparse


@app.route("/statistics")
def statistics():
    # Calculate statistics
    total_houses = db.count_documents({})

    all_links = [house["link"] for house in db.find({}, {"link": 1})]

    base_urls = set()
    for link in all_links:
        parsed_url = urlparse(link)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        base_urls.add(base_url)

    last_houses = {}
    last_publish_times = {}

    for website in base_urls:
        last_house = db.find_one(
            {"link": {"$regex": f"^{re.escape(website)}"}},
            sort=[("date", pymongo.DESCENDING)],
        )
        if last_house:
            last_publish_time = last_house["date"]
            last_publish_times[website] = last_publish_time
            current_time = datetime.now()
            time_difference = current_time - last_publish_time
            if time_difference.days > 0:
                last_houses[website] = f"{time_difference.days} days ago"
            elif time_difference.seconds < 3600:
                minutes = time_difference.seconds // 60
                last_houses[website] = f"{minutes} minutes ago"
            else:
                hours = time_difference.seconds // 3600
                last_houses[website] = f"{hours} hours ago"
        else:
            last_houses[website] = "N/A"

    # Sort websites by the time of the last house published
    sorted_websites = sorted(last_publish_times, key=lambda x: last_publish_times[x])[
        ::-1
    ]

    yesterday = datetime.now() - timedelta(days=1)
    houses_last_24_hours = db.count_documents({"date": {"$gte": yesterday}})

    total_houses_filter = db.count_documents(
        {"city": {"$regex": "Amsterdam"}, "price": {"$lte": 1800}}
    )
    houses_last_24_hours_filter = db.count_documents(
        {
            "date": {"$gte": yesterday},
            "city": {"$regex": "Amsterdam"},
            "price": {"$lte": 1800},
        }
    )

    return render_template(
        "statistics.html",
        total_houses=total_houses,
        total_houses_filter=total_houses_filter,
        sorted_websites=sorted_websites,
        last_houses=last_houses,
        houses_last_24_hours=houses_last_24_hours,
        houses_last_24_hours_filter=houses_last_24_hours_filter,
    )


if __name__ == "__main__":
    print("Starting Flask server...")

    app.run(debug=True)
