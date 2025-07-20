from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser and url
browser = webdriver.Chrome()
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.maximize_window()
time.sleep(2)

# *Type "window.pageYOffset" on the DevTool's console to find the position of the scroll*
# Scroll down window until table is visible
browser.execute_script("window.scrollTo(0,736)")

# Identify tables element
table = browser.find_element(By.ID,"countries")

# Identify rows elements
rows = table.find_elements(By.TAG_NAME,"tr")

# Count and state the amount of rows
rows_count = len(rows)
print(rows_count)

# Identify target country
target_value = "Australia"

# Stating the value has not been found
found = False

# Condition to search for the value
for row in rows:
    cells = row.find_elements(By.TAG_NAME,"td")
    for cell in cells:
        if target_value == cell.text:
            print(f"Found Value '{target_value}'")
            found = True
            break
    if found:
        break
if not found:
    print(f"Target Value '{target_value}' not found")