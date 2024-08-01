from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Visit the page
    driver.get('https://example.cypress.io/commands/waiting')

    # Test case 1: Wait for a specific amount of time
    input1 = driver.find_element(By.CSS_SELECTOR, '.wait-input1')
    input1.send_keys('Wait 1000ms after typing')
    time.sleep(1)  # Wait for 1000ms

    input2 = driver.find_element(By.CSS_SELECTOR, '.wait-input2')
    input2.send_keys('Wait 1000ms after typing')
    time.sleep(1)  # Wait for 1000ms

    input3 = driver.find_element(By.CSS_SELECTOR, '.wait-input3')
    input3.send_keys('Wait 1000ms after typing')
    time.sleep(1)  # Wait for 1000ms

    # Test case 2: Wait for a specific route
    # Note: Selenium does not support intercepting network requests directly.
    # You would need to use a proxy tool like BrowserMob-Proxy or a similar tool.
    # Here, we will simulate clicking the button and a sleep to wait for the network call.
    
    network_btn = driver.find_element(By.CSS_SELECTOR, '.network-btn')
    network_btn.click()
    time.sleep(5)  # Simulate waiting for the network request

    # Check if the response status code is 200 or 304
    # This part cannot be done directly in Selenium. You would need to combine Selenium with a proxy tool.

finally:
    # Close the driver
    driver.quit()
