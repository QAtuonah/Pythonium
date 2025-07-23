from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.saucedemo.com/'


driver=webdriver.Chrome()
# Implicitly wait will be the maximum time that the automation run will wait to find an element
driver.implicitly_wait(3)
driver.maximize_window()
driver.get(url)

# Locate and type in username box element
driver.find_element(By.ID,"user-name").send_keys("standard_user")

# Locate and type in password box element
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Locate and click login button element
driver.find_element(By.ID, "login-button").click()


# Locate and click menu button element
driver.find_element(By.ID,"react-burger-menu-btn").click()

# Locate and click logout button element
driver.find_element(By.ID,"logout_sidebar_link").click()


driver.quit()