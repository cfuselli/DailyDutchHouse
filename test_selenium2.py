from selenium.webdriver.chrome.options import Options
opts = Options()
opts.binary_location = chromium_path
driver = webdriver.Chrome(chrome_options=opts)