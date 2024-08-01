from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Function to open the webpage before each test
def open_page():
    driver.get('https://example.cypress.io/commands/actions')

def test_type():
    open_page()
    email_input = driver.find_element(By.CSS_SELECTOR, '.action-email')
    email_input.send_keys('fake@email.com')
    assert email_input.get_attribute('value') == 'fake@email.com'

    email_input.send_keys(Keys.ARROW_LEFT + Keys.ARROW_RIGHT + Keys.ARROW_UP + Keys.ARROW_DOWN)
    email_input.send_keys(Keys.DELETE + Keys.CONTROL + 'a' + Keys.BACKSPACE)

    email_input.send_keys(Keys.ALT + Keys.CONTROL + Keys.META + Keys.SHIFT)

    for char in 'slow.typing@email.com':
        email_input.send_keys(char)
        time.sleep(0.1)
    assert email_input.get_attribute('value') == 'slow.typing@email.com'

    disabled_input = driver.find_element(By.CSS_SELECTOR, '.action-disabled')
    driver.execute_script("arguments[0].removeAttribute('disabled')", disabled_input)
    disabled_input.send_keys('disabled error checking')
    assert disabled_input.get_attribute('value') == 'disabled error checking'

def test_focus():
    open_page()
    focus_input = driver.find_element(By.CSS_SELECTOR, '.action-focus')
    focus_input.click()
    assert 'focus' in focus_input.get_attribute('class')
    prev_element = focus_input.find_element(By.XPATH, 'preceding-sibling::*[1]')
    assert 'color: orange;' in prev_element.get_attribute('style')

def test_blur():
    open_page()
    blur_input = driver.find_element(By.CSS_SELECTOR, '.action-blur')
    blur_input.send_keys('About to blur')
    blur_input.send_keys(Keys.TAB)
    assert 'error' in blur_input.get_attribute('class')
    prev_element = blur_input.find_element(By.XPATH, 'preceding-sibling::*[1]')
    assert 'color: red;' in prev_element.get_attribute('style')

def test_clear():
    open_page()
    clear_input = driver.find_element(By.CSS_SELECTOR, '.action-clear')
    clear_input.send_keys('Clear this text')
    assert clear_input.get_attribute('value') == 'Clear this text'
    clear_input.clear()
    assert clear_input.get_attribute('value') == ''

def test_submit():
    open_page()
    form = driver.find_element(By.CSS_SELECTOR, '.action-form')
    text_input = form.find_element(By.CSS_SELECTOR, '[type="text"]')
    text_input.send_keys('HALFOFF')
    form.submit()
    next_element = form.find_element(By.XPATH, 'following-sibling::*[1]')
    assert 'Your form has been submitted!' in next_element.text

def test_click():
    open_page()
    button = driver.find_element(By.CSS_SELECTOR, '.action-btn')
    button.click()

    canvas = driver.find_element(By.ID, 'action-canvas')
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(canvas, 80, 75).click().perform()
    actions.move_to_element_with_offset(canvas, 170, 75).click().perform()
    actions.move_to_element_with_offset(canvas, 80, 165).click().perform()
    actions.move_to_element_with_offset(canvas, 100, 185).click().perform()
    actions.move_to_element_with_offset(canvas, 125, 190).click().perform()
    actions.move_to_element_with_offset(canvas, 150, 185).click().perform()
    actions.move_to_element_with_offset(canvas, 170, 165).click().perform()

    labels = driver.find_elements(By.CSS_SELECTOR, '.action-labels>.label')
    for label in labels:
        label.click()

    opacity_button = driver.find_element(By.CSS_SELECTOR, '.action-opacity>.btn')
    driver.execute_script("arguments[0].click();", opacity_button)

def test_dblclick():
    open_page()
    div = driver.find_element(By.CSS_SELECTOR, '.action-div')
    actions = ActionChains(driver)
    actions.double_click(div).perform()
    assert not div.is_displayed()
    hidden_input = driver.find_element(By.CSS_SELECTOR, '.action-input-hidden')
    assert hidden_input.is_displayed()

def test_rightclick():
    open_page()
    div = driver.find_element(By.CSS_SELECTOR, '.rightclick-action-div')
    actions = ActionChains(driver)
    actions.context_click(div).perform()
    assert not div.is_displayed()
    hidden_input = driver.find_element(By.CSS_SELECTOR, '.rightclick-action-input-hidden')
    assert hidden_input.is_displayed()

def test_check():
    open_page()
    checkboxes = driver.find_elements(By.CSS_SELECTOR, '.action-checkboxes [type="checkbox"]:not([disabled])')
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
    for checkbox in checkboxes:
        assert checkbox.is_selected()

    radios = driver.find_elements(By.CSS_SELECTOR, '.action-radios [type="radio"]:not([disabled])')
    for radio in radios:
        if not radio.is_selected():
            radio.click()
    for radio in radios:
        assert radio.is_selected()

    radio1 = driver.find_element(By.CSS_SELECTOR, '.action-radios [type="radio"][value="radio1"]')
    radio1.click()
    assert radio1.is_selected()

    checkboxes_to_check = driver.find_elements(By.CSS_SELECTOR, '.action-multiple-checkboxes [type="checkbox"]')
    for checkbox in checkboxes_to_check:
        if checkbox.get_attribute('value') in ['checkbox1', 'checkbox2']:
            if not checkbox.is_selected():
                checkbox.click()
    for checkbox in checkboxes_to_check:
        if checkbox.get_attribute('value') in ['checkbox1', 'checkbox2']:
            assert checkbox.is_selected()

    disabled_checkbox = driver.find_element(By.CSS_SELECTOR, '.action-checkboxes [disabled]')
    driver.execute_script("arguments[0].click();", disabled_checkbox)
    assert disabled_checkbox.is_selected()

    radio3 = driver.find_element(By.CSS_SELECTOR, '.action-radios [type="radio"][value="radio3"]')
    driver.execute_script("arguments[0].click();", radio3)
    assert radio3.is_selected()

def test_uncheck():
    open_page()
    checkboxes = driver.find_elements(By.CSS_SELECTOR, '.action-check [type="checkbox"]:not([disabled])')
    for checkbox in checkboxes:
        if checkbox.is_selected():
            checkbox.click()
    for checkbox in checkboxes:
        assert not checkbox.is_selected()

    checkbox1 = driver.find_element(By.CSS_SELECTOR, '.action-check [type="checkbox"][value="checkbox1"]')
    checkbox1.click()
    checkbox1.click()
    assert not checkbox1.is_selected()

    checkboxes_to_uncheck = driver.find_elements(By.CSS_SELECTOR, '.action-check [type="checkbox"]')
    for checkbox in checkboxes_to_uncheck:
        if checkbox.get_attribute('value') in ['checkbox1', 'checkbox3']:
            if checkbox.is_selected():
                checkbox.click()
    for checkbox in checkboxes_to_uncheck:
        if checkbox.get_attribute('value') in ['checkbox1', 'checkbox3']:
            assert not checkbox.is_selected()

    disabled_checkbox = driver.find_element(By.CSS_SELECTOR, '.action-check [disabled]')
    driver.execute_script("arguments[0].click();", disabled_checkbox)
    assert not disabled_checkbox.is_selected()

# Call each test function
test_type()
test_focus()
test_blur()
test_clear()
test_submit()
test_click()
test_dblclick()
test_rightclick()
test_check()
test_uncheck()

# Quit the browser
driver.quit()
