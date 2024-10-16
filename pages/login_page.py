from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.open(), "WRONG url link, don't have login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Don't have login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Don't have register form"

    def register_new_user(self, email, password, repeat_password):
        email = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER).send_keys(email)
        password = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER).send_keys(password)
        repeat_password = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_REGISTER).send_keys(repeat_password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()

