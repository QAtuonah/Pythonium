from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser and url
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.selenium.dev/')

# Open and switch to new tab
browser.switch_to.new_window()

# Enter new tab url
browser.get('https://www.playwright.dev/')

# Count the number of tabs
number_of_tabs = len(browser.window_handles)
print(number_of_tabs)

# Identify the value of each tab
tabs_value = browser.window_handles
print(tabs_value)

# Identify the tab currently on
Current_tab = browser.current_window_handle
print(Current_tab)

# Locate and click on the element
browser.find_element(By.CSS_SELECTOR,".getStarted_Sjon").click()

# Identify the first tab
FirstTab = browser.window_handles[0]

# Condition to switch or stay on the first tab
if Current_tab != FirstTab:
    browser.switch_to.window(FirstTab)

# Locate and click on the element
browser.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()