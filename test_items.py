import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_language_select(browser):
    browser.implicitly_wait(4)
    select_language = browser.find_element(By.XPATH,'//*[@id="add_to_basket_form"]/button')
    assert select_language is not None, 'Кнопка покупки отсутствует'