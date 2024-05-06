from pages.base_page import BasePage
from pages.locators import create_customer_locators as loc
from faker import Faker


class CreateCustomerPage(BasePage):
    page_url = '/customer/account/create/'

    def fill_create_form(self):
        fake = Faker()
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()
        fake_password = fake.password()

        first_name_input = self.find(loc.first_name_input_locator)
        last_name_input = self.find(loc.last_name_input_locator)
        email_input = self.find(loc.email_input_locator)
        password_input = self.find(loc.password_input_locator)
        confirm_password_input = self.find(loc.confirm_password_input_locator)
        create_button = self.find(loc.create_button_locator)

        first_name_input.send_keys(fake_first_name)
        last_name_input.send_keys(fake_last_name)
        email_input.send_keys(fake_email)
        password_input.send_keys(fake_password)
        confirm_password_input.send_keys(fake_password)
        create_button.click()

    def check_thank_you_text(self, text):
        thank_you = self.waiting(loc.thank_you)
        assert thank_you.text == text

    def check_header_title(self, text):
        header_title = self.find(loc.header_title)
        assert header_title.text == text

    def check_pass_for_strong(self, text):
        fake = Faker()
        fake_password = fake.password()
        password_input = self.find(loc.password_input_locator)
        password_input.send_keys(fake_password)
        strong_password_text = self.find(loc.password_text_strong)
        assert strong_password_text.text == text
