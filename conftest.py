from selenium import webdriver
import pytest
from pages.create_customer_page import CreateCustomerPage
from pages.eco_friendly_page import EcoFriendlyPage
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def customer_page(driver):
    return CreateCustomerPage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
