from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser and url
browser = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)
browser.maximize_window()

# Identify and click button (I am a JS Alert) element
alert_button = browser.find_element(By.CSS_SELECTOR,"button[onclick='jsAlert()']")
alert_button.click()

time.sleep(2)

# Switch to the alert prompt
alert = browser.switch_to.alert
alert_text = alert.text

# Print and accept (Ok) the alert
print(alert_text)
alert.accept()

time.sleep(2)

# Identify and click button (I am a JS Confirm) element
alert_button_2 = browser.find_element(By.CSS_SELECTOR,"button[onclick='jsConfirm()']")
alert_button_2.click()

time.sleep(2)

# Switch to the alert prompt
alert_2 = browser.switch_to.alert
alert_text_2 = alert_2.text

# Print and dismiss (Cancel) the alert         *Use 'accept' for the 'Ok' button
print(alert_text_2)
alert_2.dismiss()

time.sleep(2)

# Identify and click button (I am a JS prompt) element
alert_button_3 = browser.find_element(By.CSS_SELECTOR,"button[onclick='jsPrompt()']")
alert_button_3.click()

time.sleep(2)

# Switch to the alert prompt
alert_3 = browser.switch_to.alert
alert_text_3 = alert_3.text

# Print the alert text
print(alert_text_3)

# Type in the required text in the alert text box
alert.send_keys("Handling JavaScript Alerts Test")

time.sleep(2)

# Accept (Ok) the alert                    *Use 'dismiss' for the 'Cancel' button
alert_3.accept()

time.sleep(2)