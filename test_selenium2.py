from selenium.webdriver.chrome.options import Options
from selenium import webdriver

opts = Options()
opts.binary_location = '/usr/bin/chromium-browser'
driver = webdriver.Chrome(chrome_options=opts)