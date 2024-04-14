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

        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'Accept-Language': 'en-US,en;q=0.9',
 'Accept-Encoding': 'gzip, deflate, br'}

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
            print(f"Response with {len(html)} characters")
            return self.scrape(html)
        else:
            print(f"Failed to retrieve data from {self.url}")
            print(response.status_code)
            print(response.text)
            print()
            return []

    def scrape_selenium(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        import time

        # Set up Chrome options for headless mode
        options = Options()
        options.binary_location = '/snap/chromium'  # Specify the path to Chromium
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("enable-automation")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--incognito")
        options.add_argument("--no-first-run")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-sync")
        # Initialize WebDriver
        try:
            service = Service(ChromeDriverManager().install())
        except:
            service = Service(ChromeDriverManager('123.0.6312.105').install())


        driver = webdriver.Chrome(service=service, options=options)

        driver.get(self.url)
        time.sleep(2)
        html = driver.page_source
        print(f"Response with {len(html)} characters")
        return self.scrape(html)

    def scrape_requests_html(self):
        from requests_html import HTMLSession
        session = HTMLSession()
        try:
            response = session.get(self.url, headers=self.headers)
            response.html.render()
            print(f"Response with {len(response.html.html)} characters")
            return self.scrape(response.html.html)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def scrape_pyppeteer(self):
        from pyppeteer import launch

        async def main():
            browser = await launch()
            page = await browser.newPage()
            await page.goto(self.url)
            html = await page.content()
            print(f"Response with {len(html)} characters")
            await browser.close()
            return self.scrape(html)

        import asyncio
        asyncio.get_event_loop().run_until_complete(main())

    def scrape_test(self):
        response = requests.get(self.url, headers=self.headers)

        if response.status_code == 200:
            html = response.text
            print(html)
        
        else:
            print(f"Failed to retrieve data from {self.url}")
            print(response.status_code)
            print(response.text)
            print()
            return []
            

