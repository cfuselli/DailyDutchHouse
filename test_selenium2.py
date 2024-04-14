from selenium import webdriver

# import options
from selenium.webdriver.chrome.options import Options

options = Options()
# if on my mac, do nothing, if on the server, set the binary location
#
# if the location of home is /home/runner, then it is on the server
if os.path.expanduser('~') == '/home/carlo': 
    print('On the server')
    options.binary_location = '/usr/bin/chromium-browser'  # or '/snap/bin/chromium' if the other doesn't work
else:
    pass


options.add_argument("--headless")  # Ensure headless mode is activated
options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
options.add_argument("--no-sandbox")  # Bypass OS security model, required on many systems
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
options.add_argument("enable-automation")  # Avoid popup about automated software
options.add_argument("--disable-infobars")  # Disable info bars from Chrome
options.add_argument("--disable-extensions")  # Disable extensions
options.add_argument("--window-size=1920,1080")  # Specify browser resolution
driver = webdriver.Chrome(options=options)

driver.get("http://selenium.dev")

driver.quit()

# from selenium import webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# import time
# import os
# # Set up Chrome options for headless mode
# options = Options()

# # if on my mac, do nothing, if on the server, set the binary location
# #
# # if the location of home is /home/runner, then it is on the server
# if os.path.expanduser('~') == '/home/carlo': 
#     print('On the server')
#     options.binary_location = '/usr/bin/chromium-browser'  # or '/snap/bin/chromium' if the other doesn't work
# else:
#     pass


# options.add_argument("--headless")  # Ensure headless mode is activated
# options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
# options.add_argument("--no-sandbox")  # Bypass OS security model, required on many systems
# options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
# options.add_argument("enable-automation")  # Avoid popup about automated software
# options.add_argument("--disable-infobars")  # Disable info bars from Chrome
# options.add_argument("--disable-extensions")  # Disable extensions
# options.add_argument("--window-size=1920,1080")  # Specify browser resolution

# # Initialize WebDriver
# try:
#     service = Service(ChromeDriverManager().install())
# except:
#     print('Failed to install the driver, trying with a specific version')
#     service = Service(ChromeDriverManager('123.0.6312.105').install())


# driver = webdriver.Chrome(service=service, options=options)

# # Load the webpage
# driver.get('https://www.google.com')

# # Wait for JavaScript to load and for the page to be fully rendered
# time.sleep(2)  # Adjust sleep time based on the specific needs and response times of the website

# # Now you can scrape the content
# content = driver.page_source
# print(content)  # Output the page content or process it as needed

# # Clean up
# driver.quit()
