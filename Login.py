from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Browser and Website
driver = webdriver.Chrome()
driver.get("http://www.saucedemo.com/")
driver.maximize_window()

# User access
username = "standard_user"
password = "secret_sauce"

# Website login
login_url = "http://www.saucedemo.com/"
driver.get(login_url)

# Identify username and password text spaces
username_field = driver.find_element(By.ID,"user-name")
password_field = driver.find_element(By.ID,"password")

# Type in the username and password
username_field.send_keys(username)
password_field.send_keys(password)

# Find and click the login button
login_button = driver.find_element(By.ID,"login-button")
assert not login_button.get_attribute("disabled")
login_button.click()

# Verify if login was successful
success_element = driver.find_element(By.CSS_SELECTOR,".title")
assert success_element.text == "Products"
print (success_element)