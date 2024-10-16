from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')
    ADD_TO_CART = (By.XPATH, '//button[@value="Добавить в корзину"]')
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alertinner ']")
    EMAIL_REGISTER = (By.XPATH, "//input[@name='registration-email']")
    PASSWORD_REGISTER = (By.XPATH, "//input[@name='registration-password1']")
    REPEAT_PASSWORD_REGISTER = (By.XPATH, "//input[@name='registration-password2']")
    BUTTON_REGISTRATION = (By.XPATH, "//button[@name='registration_submit']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_IN_HEAD = (By.XPATH, '//a[@class="btn btn-default"]')
    CART_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    CART_WITH_PRODUCT = (By.XPATH, '//form[@class="basket_summary"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

