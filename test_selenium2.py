from selenium.webdriver.chrome.options import Options
opts = Options()
opts.binary_location = '/usr/bin/chromium-browser'
driver = webdriver.Chrome(chrome_options=opts)