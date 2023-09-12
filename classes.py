import requests
from bs4 import BeautifulSoup


# Define a House class to store property information
class House:
    def __init__(self):
        self.images = []
        self.status = None
        self.address = None
        self.city = None
        self.price = None
        self.details = {}
        self.link = None
        self.date = None
        self.house_n = None

    # Method to return house data as a dictionary
    def to_dict(self):
        house_dict = {
            "images": self.images,
            "status": self.status,
            "address": self.address,
            "city": self.city,
            "price": self.price,
            "details": self.details,
            "link": self.link,
            "date": self.date,
            "house_n": self.house_n,
            "email_sent": [],
        }
        return house_dict

    def print(self):
        print(f" - Address: {self.address}")
        print(f" - City: {self.city}")
        print(f" - Price: {self.price} €")
        print(" - Details:")
        for key, value in self.details.items():
            print(f"      {key}: {value}")
        print(f" - Images: {self.images}")
        print(f" - Link: {self.link}")
        print(f" - Date: {self.date}")
        print(f" - House number: {self.house_n}")
        print()

    def write_to_file(self, file_path):
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"---- House ----\n")
            file.write(f"Address: {self.address}\n")
            file.write(f"City: {self.city}\n")
            file.write(f"Price: {self.price}\n")
            file.write("Details:\n")
            for key, value in self.details.items():
                file.write(f"  {key}: {value}\n")
            file.write(f"Link: {self.link}\n\n")


class Website:
    def __init__(self, url, example_html=None, parser=None):
        self.url = url
        self.example_html = example_html
        self.parser = parser
        self.houses = []
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
        }

    def scrape(self, html):
        if self.parser:
            self.houses = self.parser(html)
            return self.houses
        else:
            print("No parser defined")
            return []

    def scrape_example(self):
        response = requests.get(self.url, headers=self.headers)

        if response.status_code == 200:
            html = response.text
            return self.scrape(html)
        else:
            print(f"Failed to retrieve data from {self.url}")
            print(response.status_code)
            print(response.text)
            print()
            return []
