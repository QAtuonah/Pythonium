from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.saucedemo.com/'

# Open browser and url
driver=webdriver.Chrome()
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

# Explicit wait will put a wait time on a specific element until it is available for a certain action
element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"logout_sidebar_link")))

# Locate and click logout button element
element.click()


driver.quit()