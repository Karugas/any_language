from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')
    ADD_TO_CART = (By.XPATH, '//button[@value="Добавить в корзину"]')
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alertinner ']")
