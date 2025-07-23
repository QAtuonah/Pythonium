import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Input parameters
url = "https://www.google.com/"

# Set incognito parameters
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Open browser in incognito mode
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Open url
driver.get(url)

time.sleep(3)