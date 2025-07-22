from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# Open browser and url
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/drag_and_drop"
browser.get(url)

# Identify dragging element
source_element = browser.find_element(By.ID,"column-a")

# Identify element where will be dragged
destination_element = browser.find_element(By.ID,"column-b")

# Action function
action = ActionChains(browser)

# Drag and drop action function
action.drag_and_drop(source_element,destination_element).perform()

time.sleep(4)
