import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Open browser and url
browser = webdriver.Chrome()
browser.get('https://faculty.washington.edu/chudler/java/boxes.html')

# Maximize window
browser.maximize_window()
time.sleep(3)

# Scroll page
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Find checkbox
checkboxes = browser.find_elements(By.XPATH,"//input[@type='checkbox']")

# Check checkboxes
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

# Condition to verify amount of checkboxes checked
checked_count =0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1

expected_checked_count = 100

if checked_count == expected_checked_count:
    print('Checkbox count verified')
else:
    print('Checkbox count mismatch')
time.sleep(3)

browser.close()