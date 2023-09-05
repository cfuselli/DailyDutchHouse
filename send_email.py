import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


import argparse
import pymongo
import time
from mongo import db
from datetime import datetime, timedelta
import os


parser = argparse.ArgumentParser(description='Your script description here')
# Add a --remote flag that's False by default
parser.add_argument('--remote', action='store_true', help='Use remote OAuth authentication')
# Parse the command-line arguments
args = parser.parse_args()



def get_creds(remote=False):

    credentials_path = 'secrets/client_secret_1_819495169002-0sugkiip1v5i8r5j2jsbte0fvb0h59c1.apps.googleusercontent.com.json'

    if not remote:
        SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=0)

    else:
        creds = None
        if os.path.exists('secrets/token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

    return creds

creds = get_creds(args.remote)

service = build('gmail', 'v1', credentials=creds)


_email = os.environ.get('DAILYDUTCHHOUSE_EMAIL')
sender_email = _email
recipient_email = _email


def send_message(houses):

    # Create an HTML message with the list of houses
    html_message = """
    <html>
    <head>
    <style>
    /* Your CSS styles here */
    body {
        font-family: Arial, sans-serif;
        background-color: #f5f5f5;
        margin: 0;
        padding: 0;
    }

    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    .house-container {
        margin-bottom: 20px;
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        display: flex;
        flex-direction: row; /* Display content in a row */
    }

    .text-column {
        flex: 2;
        padding: 20px;
    }

    .image-column {
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        background-color: #f0f0f0;
    }

    .image-container img {
        max-width: 100%;
        height: auto;
    }

    .house-title {
        font-size: 20px;
        color: #333;
        margin-bottom: 10px;
    }

    .details {
        list-style-type: none;
        padding: 0;
        font-size: 16px;
        color: #555;
    }

    .details li {
        margin: 5px 0;
    }

    .details strong {
        color: #333;
    }

    .house-link {
        text-decoration: none;
        color: #007bff;
    }

    .house-link:hover {
        text-decoration: underline;
    }


        /* Styles for the form container and example queries */
        .container-query {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            padding: auto;
        }

        .form-container {
            flex: 1;
            background-color: #f4f4f4;
            border: 1px solid #ddd;
            padding: 20px;
            margin-right: 10px;
        }

        .form-container label {
            display: block;
            font-weight: bold;
            margin-bottom: 10px;
        }


        .form-container textarea {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 12pt;
            resize: vertical; /* Allows vertical resizing */
        }

        .form-container button {
            background-color: #007BFF;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .example-queries {
            flex: 1;
            background-color: #fff;
            border: 1px solid #ddd;
            padding: 20px;
        }

        .example-queries h3 {
            font-size: 18px;
            margin-bottom: 10px;
        }

        .example-queries ul {
            list-style-type: none;
            padding: 0;
        }

        .example-queries li {
            margin-bottom: 10px;
        }

        .example-queries a {
            color: #007BFF;
            text-decoration: none;
        }

        .example-queries a:hover {
            text-decoration: underline;
        }

                /* Updated styles for improved mobile readability */
            .house-container {
                flex-direction: column; /* Display content in a column on mobile */
            }

            .image-column {
                flex: 1;
                text-align: center; /* Center the image */
                margin-top: 10px; /* Add some spacing between text and image */
            }

            .image-container img {
                max-width: 100%; /* Ensure the image is responsive */
                height: auto;
            }
    </style>
    </head>
    <body>
        <h1>House Listings</h1>
    """

    for house in houses:
        html_message += f"""
        <div class="house-container">
            <div class="text-column">
                <h2 class="house-title">House n: {house["house_n"]}</h2>
                <ul class="details">
                    <li><strong>Address:</strong> {house["address"]}</li>
                    <li><strong>City:</strong> {house["city"]}</li>
                    <li><strong>Price:</strong> {house["price"]}</li>
                    <li><strong>Status:</strong> {house["status"]}</li>
                    <li><strong>Details:</strong></li>
        """

        # Add house details
        for key, value in house["details"].items():
            html_message += f"<li><strong>{key}:</strong> {value}</li>"

        html_message += f"""
                </ul>
                <p><strong>Link:</strong> <a href="{house['link']}">{house['link']}</a></p>
            </div>
            <div class="image-column">
                <div class="image-container">
                    <img src="{house['images'][0]}" alt="House Image">
                </div>
            </div>
        </div>
        """

    html_message += """
    </body>
    </html>
    """

    # Create an email message with HTML content
    message = MIMEMultipart()
    message['to'] = recipient_email
    message['subject'] = f'House Listings - {len(houses)} new'
    message.attach(MIMEText(html_message, 'html'))

    try:
        # Send the email
        sent_message = service.users().messages().send(userId='me', body={'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}).execute()
        print(f'Sent message to {recipient_email}. Message Id: {sent_message["id"]}')
    except HttpError as error:
        print(f'An error occurred: {error}')

    return message


def get_houses(seconds=3600):

    # Find houses published in the last hour
    # with prices between 1000 and 1500
    # with the word amsterdam regex in city or address
    houses = db.find({"date": {"$gte": datetime.now() - timedelta(seconds=seconds)},
            "price": {"$gte": 1000, "$lte": 1800},
                "$or": [{"city": {"$regex": "amsterdam", "$options": "i"}},
                        {"address": {"$regex": "amsterdam", "$options": "i"}}]
            }).sort("date", pymongo.DESCENDING)

    houses = [house for house in houses]

    return houses


# Initialize a variable to track the time of the last successful execution
last_execution_time = time.time() - 7000  # Set to 2 hours ago to send the first email

# Run the script in an infinite loop
while True:
    try:
        # Calculate the number of seconds since the last successful execution
        current_time = time.time()
        seconds_since_last_execution = current_time - last_execution_time

        houses = get_houses(seconds_since_last_execution+300)

        # Call the send_message function and pass the seconds_since_last_execution
        print(f"Found {len(houses)} new houses")

        if len(houses) > 0:
            send_message(houses)
            ids = [house["_id"] for house in houses]
            db.update_many({"_id": {"$in": ids}}, {"$set": {"email_sent":'true'}})

        # Update the last_execution_time to the current time
        last_execution_time = current_time

        # Sleep for an hour (3600 seconds) before running again
        time.sleep(1800)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(30)
