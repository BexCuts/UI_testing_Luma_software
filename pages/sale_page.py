from pages.base_page import BasePage
from pages.locators import sale_locators as loc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class SalePage(BasePage):
    page_url = '/sale.html'

    def new_tab_and_check_header(self, text):
        tees = self.find(loc.tees)
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).click(tees).perform()
        self.driver.switch_to.window(self.driver.window_handles[1])
        tees_header = self.waiting(loc.tees_header)
        assert tees_header.text == text
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()

    def select_women(self, text):
        select_head = self.find(loc.women)
        select_top = self.find(loc.select_tops)
        select_jackets = self.find(loc.select_jackets)
        action = ActionChains(self.driver)
        action.move_to_element(select_head).perform()
        action.move_to_element(select_top).perform()
        action.move_to_element(select_jackets).perform()
        action.click(select_jackets).perform()
        expected_jacket = self.waiting(loc.jacket_header)
        assert expected_jacket.text == text

    def go_to_logo(self, text):
        logo = self.find(loc.logo)
        logo.click()
        yoga = self.waiting(loc.yoga)
        assert yoga.text == text
