import time

from selenium import webdriver

# Viewport options
vierports = [(1024,768),(768,1024),(375,667),(414,896)]

# Open browser and url
driver = webdriver.Chrome()
driver.get('https://www.google.com/')

# Condition to check each option
try:
    for width,height in vierports:
        driver.set_window_size(width, height)
        time.sleep(3)

# Close browser
finally:
    driver.close()