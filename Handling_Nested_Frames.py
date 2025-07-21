from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser and url
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/nested_frames')

# Switching to TOP Frame
browser.switch_to.frame("frame-top")

# Switching to Middle Frame
browser.switch_to.frame("frame-middle")

# Locate element and print frame text
content = browser.find_element(By.ID,"content").text
print("Content in middle frame", content)

# Switch to Default Content
browser.switch_to.default_content()

# Switch to Bottom Frame
browser.switch_to.frame("frame-bottom")

# Locate element and print frame text
content_2 = browser.find_element(By.CSS_SELECTOR,"body").text
print("Content in bottom frame", content_2)