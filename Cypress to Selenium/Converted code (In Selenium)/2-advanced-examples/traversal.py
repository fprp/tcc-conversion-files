from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Define a function to perform the test cases
def run_tests():
    # Visit the webpage
    driver.get("https://example.cypress.io/commands/traversal")

    # .children() - get child DOM elements
    breadcrumb = driver.find_element(By.CLASS_NAME, 'traversal-breadcrumb')
    active_child = breadcrumb.find_element(By.CLASS_NAME, 'active')
    assert 'Data' in active_child.text

    # .closest() - get closest ancestor DOM element
    badge = driver.find_element(By.CLASS_NAME, 'traversal-badge')
    closest_ul = badge.find_element(By.XPATH, './ancestor::ul')
    assert 'list-group' in closest_ul.get_attribute('class')

    # .eq() - get a DOM element at a specific index
    list_items = driver.find_elements(By.CSS_SELECTOR, '.traversal-list>li')
    assert 'siamese' in list_items[1].text

    # .filter() - get DOM elements that match the selector
    nav_items = driver.find_elements(By.CSS_SELECTOR, '.traversal-nav>li')
    active_nav_item = [item for item in nav_items if 'active' in item.get_attribute('class')]
    assert 'About' in active_nav_item[0].text

    # .find() - get descendant DOM elements of the selector
    pagination = driver.find_element(By.CLASS_NAME, 'traversal-pagination')
    links = pagination.find_elements(By.TAG_NAME, 'a')
    assert len(links) == 7

    # .first() - get first DOM element
    table_cells = driver.find_elements(By.CSS_SELECTOR, '.traversal-table td')
    assert '1' in table_cells[0].text

    # .last() - get last DOM element
    buttons = driver.find_elements(By.CSS_SELECTOR, '.traversal-buttons .btn')
    assert 'Submit' in buttons[-1].text

    # .next() - get next sibling DOM element
    apples = driver.find_element(By.XPATH, "//*[contains(text(), 'apples')]")
    next_sibling = apples.find_element(By.XPATH, './following-sibling::*')
    assert 'oranges' in next_sibling.text

    # .nextAll() - get all next sibling DOM elements
    oranges = driver.find_element(By.XPATH, "//*[contains(text(), 'oranges')]")
    next_all = oranges.find_elements(By.XPATH, './following-sibling::*')
    assert len(next_all) == 3

    # .nextUntil() - get next sibling DOM elements until next el
    veggies = driver.find_element(By.ID, 'veggies')
    next_until = veggies.find_elements(By.XPATH, './following-sibling::*[preceding-sibling::#veggies and following-sibling::#nuts]')
    assert len(next_until) == 3

    # .not() - remove DOM elements from set of DOM elements
    buttons = driver.find_elements(By.CSS_SELECTOR, '.traversal-disabled .btn')
    enabled_buttons = [btn for btn in buttons if 'disabled' not in btn.get_attribute('class')]
    assert all('Disabled' not in btn.text for btn in enabled_buttons)

    # .parent() - get parent DOM element from DOM elements
    mark = driver.find_element(By.CLASS_NAME, 'traversal-mark')
    parent = mark.find_element(By.XPATH, './..')
    assert 'Morbi leo risus' in parent.text

    # .parents() - get parent DOM elements from DOM elements
    cite = driver.find_element(By.CLASS_NAME, 'traversal-cite')
    blockquote = cite.find_element(By.XPATH, './ancestor::blockquote')
    assert blockquote is not None

    # .parentsUntil() - get parent DOM elements from DOM elements until el
    active = driver.find_element(By.CSS_SELECTOR, '.clothes-nav .active')
    parents_until = active.find_elements(By.XPATH, './ancestor::*[not(contains(@class, "clothes-nav"))]')
    assert len(parents_until) == 2

    # .prev() - get previous sibling DOM element
    active_bird = driver.find_element(By.CSS_SELECTOR, '.birds .active')
    prev_sibling = active_bird.find_element(By.XPATH, './preceding-sibling::*')
    assert 'Lorikeets' in prev_sibling.text

    # .prevAll() - get all previous sibling DOM elements
    third_fruit = driver.find_element(By.CSS_SELECTOR, '.fruits-list .third')
    prev_all_fruits = third_fruit.find_elements(By.XPATH, './preceding-sibling::*')
    assert len(prev_all_fruits) == 2

    # .prevUntil() - get all previous sibling DOM elements until el
    nuts = driver.find_element(By.ID, 'nuts')
    prev_until = nuts.find_elements(By.XPATH, './preceding-sibling::*[preceding-sibling::#veggies]')
    assert len(prev_until) == 3

    # .siblings() - get all sibling DOM elements
    active_pill = driver.find_element(By.CSS_SELECTOR, '.traversal-pills .active')
    siblings = active_pill.find_elements(By.XPATH, './following-sibling::*')
    assert len(siblings) == 2

# Run the tests
try:
    run_tests()
    print("All tests passed!")
finally:
    driver.quit()
