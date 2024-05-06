from selenium.webdriver.common.by import By


first_name_input_locator = (By.ID, 'firstname')
last_name_input_locator = (By.ID, 'lastname')
email_input_locator = (By.ID, 'email_address')
password_input_locator = (By.CSS_SELECTOR, '#password[title="Password"]')
confirm_password_input_locator = (By.ID, 'password-confirmation')
create_button_locator = (By.CSS_SELECTOR, '.action.submit')
password_text_strong = (By.ID, 'password-strength-meter-label')
thank_you = (By.CSS_SELECTOR, '[role="alert"]')
header_title = (By.CLASS_NAME, 'base')
