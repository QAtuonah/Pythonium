from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser and url
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://autotest.how/demo/tinymce")

# Locate and switch to iframe
iframe = browser.find_element(By.ID,"tinymce_ifr")
browser.switch_to.frame(iframe)

# Locate text box
Text_Editor = browser.find_element(By.ID,"tinymce")

# Clear text
Text_Editor.clear()

# Type in requested text
Text_Editor.send_keys("This is Selenium with Python Iframe Tutorial")
time.sleep(2)

# Switch back to from iframe into default
browser.switch_to.default_content()

# Locate element and click
tiny_link = browser.find_element(By.XPATH,"//a[normalize-space()='Build with']//*[name()='svg']")
tiny_link.click()
time.sleep(2)