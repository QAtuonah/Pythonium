from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select
import time

# Automatic current day date picker dropdown test #

# Open browser and url
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://www.globalsqa.com/demo-site/datepicker/"
browser.get(url)

time.sleep(1)

# Change to the dropdown date picker tab
browser.find_element(By.CSS_SELECTOR,"li[id='DropDown DatePicker']").click()

time.sleep(1)

# Locate warning window and click to close
browser.find_element(By.XPATH,"(//a[@class='close_img'])[2]").click()

time.sleep(1)

# Switch to the date text box frame
frame_date = browser.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(frame_date)

# Identify and click on the date picker text box
browser.find_element(By.CSS_SELECTOR,"#datepicker").click()

time.sleep(1)

# Identify current date
current_date = datetime.now()
print(current_date)

# Identify Next day
next_day = current_date + timedelta(days=1)

# Change Next day value into a string and print
next_day = (str(next_day.day))
print("Next Day",next_day)

# Identify current month and print
current_month = datetime.now().month
print("Current Month", current_month)

# Identify current year and print
current_year = datetime.now().year
print("Current Year",current_year)

# Identify next month and print
next_month = (current_month % 12) + 1
print("Next Month",next_month)

# Depending on the layout of the value in the month dropdown *next_month_year = f"{next_month}/{current_year}"*

# Identify and select value for month dropdown
month_dropdown = browser.find_element(By.CSS_SELECTOR,".ui-datepicker-month")
select = Select(month_dropdown)
select.select_by_value(str(next_month))

# Identify and select value for year dropdown
year_dropdown = browser.find_element(By.CSS_SELECTOR,".ui-datepicker-year")
select = Select(year_dropdown)
select.select_by_value(str(current_year))

# Identify and click on the day
browser.find_element(By.LINK_TEXT,next_day).click()
time.sleep(3)

# Switch back to default content
browser.switch_to.default_content()

# Manual input of date picker dropdown test #

# Date parameters
day = 1
month = "Oct"
year = 2015

# Switch to the date text box frame
frame_date = browser.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(frame_date)

# Identify and click on the date picker text box
browser.find_element(By.CSS_SELECTOR,"#datepicker").click()

# Identify dropdown element and select month
select_month = Select(browser.find_element(By.CLASS_NAME, "ui-datepicker-month"))
select_month.select_by_visible_text(month)

time.sleep(1)

# Identify dropdown element and select year
select_year = Select(browser.find_element(By.CLASS_NAME, "ui-datepicker-year"))
select_year.select_by_value(str(year))

time.sleep(1)

# Identify dropdown element and select day
days = browser.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
for d in days:
    if d.text == str(day):
        d.click()
        break

# Switch back to default content
browser.switch_to.default_content()

time.sleep(3)
browser.quit()