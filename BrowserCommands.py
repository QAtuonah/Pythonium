from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser and access url
driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')

# Maximize window
driver.maximize_window()
time.sleep(5)

# Search and click element
driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(5)

# Go back on page
driver.back();
time.sleep(5)

# Go forward on page
driver.forward();
time.sleep(5)

# Refresh page
driver.refresh();

# Close window
driver.close()
