from selenium import webdriver
import csv
import time
from selenium.webdriver.common.by import By

url = 'https://www.saucedemo.com/'
csv_file= 'testdata.csv'

test_data = []

# Open csv file
with open(csv_file,'r') as file:
    reader = csv.DictReader(file)

# Append the row indo into test data
    for row in reader:
        test_data.append(row)
print(test_data)

# Condition to Open browser and url and run each combination of logins
for data in test_data:
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