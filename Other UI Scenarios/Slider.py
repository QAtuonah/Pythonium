from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# Open browser and url
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/horizontal_slider"
browser.get(url)

# Identify slider element
slider = browser.find_element(By.CSS_SELECTOR,"input[value='0']")

# Action function
actions = ActionChains(browser)

# Function to click, hold, move and release slider
actions.click_and_hold(slider).move_by_offset(5,0).release().perform()

time.sleep(2)
