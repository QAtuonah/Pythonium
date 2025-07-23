from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Open browser and url
browser = webdriver.Chrome()
browser. get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()

# Locate common image tag
images = browser.find_elements(By.TAG_NAME, 'img')
broken_images = []

# Condition to search for broken images
for image in images:
    src = image.get_attribute('src')
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken Image Found")

# Condition to map each broken image
if broken_images:
    print("list of broken images:")
    for broken_image in broken_images:
        print(broken_image)

# Condition in case no broken image is found
else:
    print("No broken images found")