from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class ProductPage(BasePage):
    def add_item_to_cart(self):
        item = self.browser.find_element(*LoginPageLocators.ADD_TO_CART)
        item.click()
