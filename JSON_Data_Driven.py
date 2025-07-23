from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import json

url = 'https://www.saucedemo.com/'

# Open and load json file
with open('testdata.json') as file:
    test_data = json.load(file)

# Condition to Open browser and url and run each combination of logins
for data in test_data['users']:
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    # Locate and type in username box element
    driver.find_element(By.ID, "user-name").send_keys(data['username'])

    # Locate and type in password box element
    driver.find_element(By.ID, "password").send_keys(data['password'])

    # Locate and click login button element
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

driver.quit()