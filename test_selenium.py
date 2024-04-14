from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Set up Chrome options for headless mode
options = Options()
options.add_argument("--headless")  # Ensure headless mode is activated
options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
options.add_argument("--no-sandbox")  # Bypass OS security model, required on many systems
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
options.add_argument("enable-automation")  # Avoid popup about automated software
options.add_argument("--disable-infobars")  # Disable info bars from Chrome
options.add_argument("--disable-extensions")  # Disable extensions
options.add_argument("--window-size=1920,1080")  # Specify browser resolution

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the webpage
driver.get('https://www.pararius.nl/huurwoningen/amsterdam')

# Wait for JavaScript to load and for the page to be fully rendered
time.sleep(2)  # Adjust sleep time based on the specific needs and response times of the website

# Now you can scrape the content
content = driver.page_source
print(content)  # Output the page content or process it as needed

# Clean up
driver.quit()
