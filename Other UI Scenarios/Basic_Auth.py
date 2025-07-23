from selenium import webdriver
import time

# login information
username = "admin"
password = "admin"

# url information. For Basic Auth, the url needs to be arranged in the following format: https://username:password@domain/path
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"  # <---- https://username:password@domain/path

# Open browser and url
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(3)

driver.quit()