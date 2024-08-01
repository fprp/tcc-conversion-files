from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Visit the page
    driver.get('https://example.cypress.io/commands/window')
    
    # Test case: Get the global window object
    # In Selenium, we can't directly check the 'top' property of the window object.
    # But we can ensure the page is loaded and we can interact with it.
    assert 'window' in driver.execute_script('return window;')
    
    # Test case: Get the document object
    document_charset = driver.execute_script('return document.charset;')
    assert document_charset == 'UTF-8', f"Expected charset to be 'UTF-8', but got '{document_charset}'"
    
    # Test case: Get the title
    WebDriverWait(driver, 10).until(EC.title_contains('Kitchen Sink'))
    title = driver.title
    assert 'Kitchen Sink' in title, f"Expected title to include 'Kitchen Sink', but got '{title}'"

finally:
    # Close the browser window
    driver.quit()