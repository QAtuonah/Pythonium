from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# Open browser and url
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://jqueryui.com/resizable/"
browser.get(url)

# Identify iframe element
iframe = browser.find_element(By.XPATH,"//iframe[@class='demo-frame']")

# Switch to frame
browser.switch_to.frame(iframe)

# Identify resizeable box element
box = browser.find_element(By.CSS_SELECTOR,"#resizable")

# Identify resizeable box corner element
corner = browser.find_element(By.CSS_SELECTOR,".ui-resizable-handle.ui-resizable-se.ui-icon.ui-icon-gripsmall-diagonal-se")

# Initial box size equation
initial_size = box.size

# Print initial size
print("Initial Size:",initial_size)

time.sleep(2)

# Action function
action_chains = ActionChains(browser)

# Click, hold and move the corner of the box
action_chains.click_and_hold(corner).move_by_offset(100,100).release().perform()

# Resized box equation
resized_box = box.size

# Print resized size
print("Resized Box:",resized_box)

time.sleep(2)

# Click, hold and move the corner of the box
action_chains.click_and_hold(corner).move_by_offset(50,50).release().perform()

# Resized box equation
reresized_box = box.size

# Print reresized size
print("Reresized Box:",reresized_box)

time.sleep(2)

browser.quit()