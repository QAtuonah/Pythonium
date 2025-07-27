# Selenium + Python Glossary for Web Test Automation

🔹 Setup & Browser Control
-----------------------------------------
webdriver.Chrome()              → Starts Chrome browser
webdriver.Firefox()             → Starts Firefox browser
driver.get("url")               → Opens a URL
driver.quit()                   → Closes all browser windows and ends the session
driver.close()                  → Closes the current tab only
driver.refresh()                → Refreshes the current page

🔹 Locating Elements
-----------------------------------------
driver.find_element(By.ID, "id")
driver.find_element(By.NAME, "name")
driver.find_element(By.CLASS_NAME, "class")
driver.find_element(By.TAG_NAME, "tag")
driver.find_element(By.LINK_TEXT, "text")
driver.find_element(By.PARTIAL_LINK_TEXT, "partial")
driver.find_element(By.XPATH, "//tag[@attr='value']")
driver.find_element(By.CSS_SELECTOR, "css")

🔹 Interacting with Elements
-----------------------------------------
element.click()                 → Clicks on element
element.send_keys("text")       → Inputs text
element.clear()                 → Clears input field
element.text                    → Gets the inner text of element
element.get_attribute("attr")   → Gets attribute value

🔹 Assertions & Validations
-----------------------------------------
assert "Expected" in element.text
assert element.is_displayed()
assert driver.title == "Expected Title"

🔹 Waits & Timing
-----------------------------------------
time.sleep(2)                   → Static wait (not recommended)
WebDriverWait(driver, 10).until(...) → Explicit wait
driver.implicitly_wait(10)      → Implicit wait (applies to all finds)

🔹 Window & Tabs
-----------------------------------------
driver.window_handles           → List of open windows
driver.switch_to.window(handle) → Switches to another tab/window

🔹 Frames & Alerts
-----------------------------------------
driver.switch_to.frame("id")
driver.switch_to.default_content()
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()

🔹 Viewport & Screen Size
-----------------------------------------
driver.set_window_size(1920, 1080)
driver.maximize_window()

🔹 Screenshots & Logs
-----------------------------------------
driver.save_screenshot("name.png")
print(driver.page_source)       → Prints full HTML source of page

🔹 Common Imports
-----------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# End of Glossary
