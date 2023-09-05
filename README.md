# DailyDutchHouse

Author: Carlo Fuselli


## Description

- This is my small project for house hunting in this crazy Amsterdam market. 

- The idea is to scrape the main websites for house renting and buying and to store the data in a database.

- The data is then used to create a dashboard with the latest offers and some statistics.

- You can also recieve periodic emails with the latest offers.

- The project runs with a MongoDB database and a Flask server.

- The emails work through a Gmail account and the Gmail API.

- The website is hosted only locally for now.

- The project is still in development.


## To use (for me for now)

- run `python3 run2.py` to start the scraping
- run `python3 app.py` to start the server
- run `python3 send_email.py` to send the emails


## This is how it should look like

- Website

![alt text](https://github.com/cfuselli/DailyDutchHouse/blob/main/figures/website.png?raw=true)

- Email

![alt text](https://github.com/cfuselli/DailyDutchHouse/blob/main/figures/email.png?raw=true)
