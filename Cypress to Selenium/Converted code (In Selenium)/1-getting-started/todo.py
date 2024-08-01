from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Visit the web page
driver.get('https://example.cypress.io/todo')

def test_displays_two_todo_items_by_default():
    todo_list_items = driver.find_elements(By.CSS_SELECTOR, '.todo-list li')
    assert len(todo_list_items) == 2
    assert todo_list_items[0].text == 'Pay electric bill'
    assert todo_list_items[1].text == 'Walk the dog'

def test_can_add_new_todo_items():
    new_item = 'Feed the cat'
    input_box = driver.find_element(By.CSS_SELECTOR, '[data-test=new-todo]')
    input_box.send_keys(new_item + Keys.ENTER)
    todo_list_items = driver.find_elements(By.CSS_SELECTOR, '.todo-list li')
    assert len(todo_list_items) == 3
    assert todo_list_items[-1].text == new_item

def test_can_check_off_an_item_as_completed():
    pay_electric_bill = driver.find_element(By.XPATH, "//li[contains(text(), 'Pay electric bill')]")
    checkbox = pay_electric_bill.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
    checkbox.click()
    completed_item = driver.find_element(By.XPATH, "//li[contains(text(), 'Pay electric bill')]")
    assert 'completed' in completed_item.get_attribute('class')

def setup_with_checked_task():
    pay_electric_bill = driver.find_element(By.XPATH, "//li[contains(text(), 'Pay electric bill')]")
    checkbox = pay_electric_bill.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
    checkbox.click()

def test_can_filter_for_uncompleted_tasks():
    setup_with_checked_task()
    active_filter = driver.find_element(By.XPATH, "//a[contains(text(), 'Active')]")
    active_filter.click()
    todo_list_items = driver.find_elements(By.CSS_SELECTOR, '.todo-list li')
    assert len(todo_list_items) == 1
    assert todo_list_items[0].text == 'Walk the dog'
    assert not any('Pay electric bill' in item.text for item in todo_list_items)

def test_can_filter_for_completed_tasks():
    setup_with_checked_task()
    completed_filter = driver.find_element(By.XPATH, "//a[contains(text(), 'Completed')]")
    completed_filter.click()
    todo_list_items = driver.find_elements(By.CSS_SELECTOR, '.todo-list li')
    assert len(todo_list_items) == 1
    assert todo_list_items[0].text == 'Pay electric bill'
    assert not any('Walk the dog' in item.text for item in todo_list_items)

def test_can_delete_all_completed_tasks():
    setup_with_checked_task()
    clear_completed_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Clear completed')]")
    clear_completed_button.click()
    todo_list_items = driver.find_elements(By.CSS_SELECTOR, '.todo-list li')
    assert len(todo_list_items) == 1
    assert not any('Pay electric bill' in item.text for item in todo_list_items)
    assert not clear_completed_button.is_displayed()

# Run the tests
try:
    test_displays_two_todo_items_by_default()
    test_can_add_new_todo_items()
    test_can_check_off_an_item_as_completed()
    test_can_filter_for_uncompleted_tasks()
    test_can_filter_for_completed_tasks()
    test_can_delete_all_completed_tasks()
finally:
    # Close the browser window
    driver.quit()
