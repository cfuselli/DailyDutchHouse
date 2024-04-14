from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.BinaryLocation = "/usr/bin/chromium-browser"

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
driver.get("https://www.google.com")