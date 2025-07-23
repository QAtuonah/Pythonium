from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# Open browser and url
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://www.globalsqa.com/demo-site/datepicker/"
browser.get(url)

# Hover mouse function
actions = ActionChains(browser)

# Button to be hovered element
hover_element = browser.find_element(By.XPATH,"//a[@class='no_border'][normalize-space()='Free Ebooks']")
time.sleep(2)

# Function to hover over the intended button
actions.move_to_element(hover_element).perform()

# Identify and click on the button below the hovered button
browser.find_element(By.XPATH,"//span[normalize-space()='Free Tensorflow eBooks']").click()
time.sleep(5)