from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup the Chrome driver
options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the page
    driver.get('https://example.cypress.io/commands/viewport')

    # Initial assertion to check if the navbar is visible
    navbar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'navbar'))
    )

    # Set the viewport size to 320x480
    driver.set_window_size(320, 480)
    time.sleep(1)

    # Check if the navbar is not visible and navbar toggle is visible
    navbar = driver.find_element(By.ID, 'navbar')
    assert not navbar.is_displayed()

    navbar_toggle = driver.find_element(By.CLASS_NAME, 'navbar-toggle')
    assert navbar_toggle.is_displayed()
    navbar_toggle.click()

    nav_links = driver.find_elements(By.CSS_SELECTOR, '.nav a')
    for link in nav_links:
        assert link.is_displayed()

    # Set the viewport size to 2999x2999
    driver.set_window_size(2999, 2999)
    time.sleep(1)

    # Set the viewport to preset device sizes
    device_sizes = [
        ('macbook-15', 1440, 900),
        ('macbook-13', 1280, 800),
        ('macbook-11', 1366, 768),
        ('ipad-2', 768, 1024),
        ('ipad-mini', 768, 1024),
        ('iphone-6+', 414, 736),
        ('iphone-6', 375, 667),
        ('iphone-5', 320, 568),
        ('iphone-4', 320, 480),
        ('iphone-3', 320, 480)
    ]

    for device, width, height in device_sizes:
        driver.set_window_size(width, height)
        time.sleep(0.2)

    # Set the viewport to iPad 2 in portrait mode
    driver.set_window_size(768, 1024)
    time.sleep(0.2)

    # Set the viewport to iPhone 4 in landscape mode
    driver.set_window_size(480, 320)
    time.sleep(0.2)

finally:
    # Close the driver
    driver.quit()
