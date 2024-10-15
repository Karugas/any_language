from asyncio import timeout

from pages.locators import BasePageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):
    def cart_empty(self):
        cart_empty_element = self.browser.find_element(*BasePageLocators.CART_EMPTY)
        cart_empty_text = cart_empty_element.text
        assert "Ваша корзина пуста Продолжить покупки" == cart_empty_text, \
            "Cart is not empty, or word changes"

    def check_empty_cart(self):
        assert self.is_not_element_present(*BasePageLocators.CART_WITH_PRODUCT), \
            "Cart is not empty!"
