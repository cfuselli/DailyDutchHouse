import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import jinja2
from jinja2 import Template

import argparse
import pymongo
import time
from mongo import db
from datetime import datetime, timedelta
import os
import re
import json 


parser = argparse.ArgumentParser(description='Your script description here')
# Add a --remote flag that's False by default
parser.add_argument('--local', action='store_true', help='Use local OAuth authentication')
parser.add_argument('--test', action='store_true', help='Test mode')
parser.add_argument('--user', default='carlo', help='User name, to be defined in secrets/user_queries.json')

def get_secrets():
    with open('secrets/secrets.json', 'r') as config_file:
        secrets = json.load(config_file)
    return secrets

def get_user(user):
    with open('secrets/user_queries.json', 'r') as f:
        user_queries = json.load(f)
    return user_queries[user]

def get_creds(local=False):

    credentials_path = 'secrets/client_secret_1_819495169002-0sugkiip1v5i8r5j2jsbte0fvb0h59c1.apps.googleusercontent.com.json'
    
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

    if local:
        print("Using local OAuth authentication")

        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=0)

    else:

        print("Using remote OAuth authentication")
        creds = None
        if os.path.exists('secrets/token.json'):
            creds = Credentials.from_authorized_user_file('secrets/token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open('secrets/token.json', 'w') as token:
                token.write(creds.to_json())

    return creds

def get_html_message(houses):

    with open('webinterface/static/styles.css', 'r') as css_file:
        css_content = css_file.read()

    # Load your HTML template
    with open('webinterface/templates/index.html', 'r') as template_file:
        template_content = template_file.read()

    # Create a Jinja2 template
    template = Template(template_content)

    # Render the template with the house data
    rendered_html = template.render(houses=houses,
                                    api_key_geoapify=secrets['api_key_geoapify'])

    rendered_html = re.sub('exclude_from_email.*?end_exclude_from_email','',rendered_html, flags=re.DOTALL)
    rendered_html = re.sub('exclude_from_email_2.*?end_exclude_from_email_2','',rendered_html, flags=re.DOTALL)

    # Add the CSS to the HTML
    rendered_html = rendered_html.replace('</head>', f'<style>{css_content}</style></head>')

    return rendered_html


def send_message(houses):

    html_message = get_html_message(houses)

    # Create an email message with HTML content
    message = MIMEMultipart()
    message['to'] = recipient_email
    _test = 'TEST EMAIL - ' if args.test else ''
    message['subject'] = f'{_test}House Listings - {len(houses)} new'
    message.attach(MIMEText(html_message, 'html'))

    try:
        # Send the email
        sent_message = service.users().messages().send(userId='me', body={'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}).execute()
        print(f'Sent message to {recipient_email}. Message Id: {sent_message["id"]}')
    except HttpError as error:
        print(f'An error occurred: {error}')

    return message


def get_houses(query, seconds=3600):

    # Find houses published in the last hour
    # with prices between 1000 and 1500
    # with the word amsterdam regex in city or address

    query['date'] = {"$gte": datetime.now() - timedelta(seconds=seconds)}
    query['email_sent'] = {"$nin": ['true', user]}
    
    houses = db.find(query).sort("date", pymongo.DESCENDING)
    houses = [house for house in houses]

    if args.test:
        query['date'] = {"$gte": datetime.now() - timedelta(days=100)}
        houses = db.find(query).sort("date", pymongo.DESCENDING)
        houses = [house for house in houses][:5]

    return houses

def get_landlord_message():
    """For now not used"""

    landlord_message_file = 'secrets/message.txt'
    if os.path.exists(landlord_message_file):
        with open(landlord_message_file) as f:
            landlord_message=''.join(line.rstrip() for line in f)
    else:
        landlord_message = 'Provide message for landlord in secrets/message.txt'

    return landlord_message


# Parse the command-line arguments
args = parser.parse_args()

secrets = get_secrets()

creds = get_creds(local=args.local)

service = build('gmail', 'v1', credentials=creds)

sender_email = os.environ.get('DAILYDUTCHHOUSE_EMAIL')

user = args.user

# Set frequency of emails  
sleep_time = 30 # seconds

# Initialize a variable to track the time of the last successful execution
last_execution_time = time.time() - 7000  # Set to 2 hours ago to send the first email

# Run the script in an infinite loop
while True:
    try:
        # Calculate the number of seconds since the last successful execution
        current_time = time.time()
        seconds_since_last_execution = current_time - last_execution_time

        # Let's fetch continuously the user info, in case it changes
        user_info = get_user(user)
        recipient_email = user_info['email']
        user_query = user_info['query']

        # Call the get_houses function and pass the user_query and seconds_since_last_execution
        houses = get_houses(user_query, seconds_since_last_execution+1000)

        # Call the send_message function and pass the seconds_since_last_execution
        print(f"Found {len(houses)} new houses")

        if len(houses) > 0:
            send_message(houses)
            ids = [house["_id"] for house in houses]

            db.update_many({"_id": {"$in": ids}}, {"$addToSet": {"email_sent": user}})

        # Update the last_execution_time to the current time
        last_execution_time = current_time

        # Sleep for an hour (3600 seconds) before running again
        time.sleep(sleep_time)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(sleep_time)

