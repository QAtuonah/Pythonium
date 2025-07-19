from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Open browser and url
driver = webdriver.Chrome()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)

# Get the dropdown element
dropdown_element = driver.find_element(By.ID, "dropdown")

# Set the target option
target_value = "Option 3"

select = Select(dropdown_element)

# Set conditions in case of successful or unsuccessful outcomes
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"Option '{target_value}' not found")


# How to Interact with Dropdown
# How to use Select Class
# How to use 3 Different methods
# Select by Visible text
# Select by Value
# Select by Index
# How to count the dropdown values
# Loop the dropdown values and if the desired value found select that value