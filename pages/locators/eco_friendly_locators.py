from selenium.webdriver.common.by import By


button_to_change_table = (By.ID, 'mode-list')
list_of_elements = (By.CSS_SELECTOR, '.item.product')
add_to_card_button = (By.CSS_SELECTOR, 'button[type="submit"][title="Add to Cart"]')
size_button = (By.ID, 'option-label-size-143-item-171')
color = (By.ID, 'option-label-color-93-item-49')
expected_element_added = (By.CSS_SELECTOR, '.messages[role="alert"]')
expected_element = (By.CSS_SELECTOR, '.action.add')
