import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser and url
driver = webdriver.Chrome()
driver.maximize_window()
url = "https://jqueryui.com/"
driver.get(url)

# locate all the links on the page
all_links = driver.find_elements(By.TAG_NAME, 'a')

# Print the total amount of links on the page
print(f"Total number of links on the page: {len(all_links)}")

# Condition to map all the links that present a code greater than 400 (error)
for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken Link: {href}(Status Code: {response.status_code})")

driver.quit()