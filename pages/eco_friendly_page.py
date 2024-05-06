from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def change_table_to_list(self, text):
        button_to_change_table = self.find(loc.button_to_change_table)
        button_to_change_table.click()
        expected_element = self.waiting(loc.expected_element)
        assert expected_element.text == text

    def len_of_elements(self):
        list_of_elements = self.find_all(loc.list_of_elements)
        print(len(list_of_elements))
        assert len(list_of_elements) == 12

    def adding_to_card(self, text):
        list_of_elements = self.find_all(loc.list_of_elements)
        actions = ActionChains(self.driver)
        add_to_card_button = self.find_all(loc.add_to_card_button)
        size_button = self.find_all(loc.size_button)
        color = self.find_all(loc.color)
        actions.move_to_element(list_of_elements[0])
        actions.click(size_button[0])
        actions.click(color[0])
        actions.click(add_to_card_button[0])
        actions.perform()
        expected_element = self.waiting(loc.expected_element_added)
        assert expected_element.text == text
