from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time

# Open browser and url
browser = webdriver.Chrome()
browser.maximize_window()
url = ("https://www.globalsqa.com/demo-site/datepicker")
browser.get(url)

# Locate warning window and click to close
browser.find_element(By.XPATH,"(//a[@class='close_img'])[1]").click()

time.sleep(2)

# Locate and switch to frame
frame_date = browser.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(frame_date)

time.sleep(2)

# Locate and click date text box
browser.find_element(By.CSS_SELECTOR,"#datepicker").click()

time.sleep(2)

# Define current date and time
current_date = datetime.now()
print(current_date)

time.sleep(2)

# Define desired date
next_date = current_date + timedelta(days=-1)
print(next_date)

time.sleep(2)

# Format text as required in date box
formatted_date = next_date.strftime("%m/%d/%Y")
print(formatted_date)

# Enter the date on the date text box then confirm on the calendar
browser.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(formatted_date + Keys.TAB)

time.sleep(2)

browser.quit()
