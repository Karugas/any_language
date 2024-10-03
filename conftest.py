import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    language_sel= request.config.getoption('--language')
    if language_sel == 'en-gb':
        browser.get(f'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/')
    elif language_sel == 'ru':
        browser.get(f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    elif language_sel == 'ar':
        browser.get(f'http://selenium1py.pythonanywhere.com/ar/catalogue/coders-at-work_207/')
    elif language_sel == 'ca':
        browser.get(f'http://selenium1py.pythonanywhere.com/ca/catalogue/coders-at-work_207/')
    elif language_sel == 'cs':
        browser.get(f'http://selenium1py.pythonanywhere.com/cs/catalogue/coders-at-work_207/')
    elif language_sel == 'da':
        browser.get(f'http://selenium1py.pythonanywhere.com/da/catalogue/coders-at-work_207/')
    elif language_sel == 'de':
        browser.get(f'http://selenium1py.pythonanywhere.com/de/catalogue/coders-at-work_207/')
    elif language_sel == 'el':
        browser.get(f'http://selenium1py.pythonanywhere.com/el/catalogue/coders-at-work_207/')
    elif language_sel == 'es':
        browser.get(f'http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/')
    elif language_sel == 'fi':
        browser.get(f'http://selenium1py.pythonanywhere.com/fi/catalogue/coders-at-work_207/')
    elif language_sel == 'fr':
        browser.get(f'http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/')
    elif language_sel == 'ko':
        browser.get(f'http://selenium1py.pythonanywhere.com/ko/catalogue/coders-at-work_207/')
    elif language_sel == 'nl':
        browser.get(f'http://selenium1py.pythonanywhere.com/nl/catalogue/coders-at-work_207/')
    elif language_sel == 'pl':
        browser.get(f'http://selenium1py.pythonanywhere.com/pl/catalogue/coders-at-work_207/')
    elif language_sel == 'pt':
        browser.get(f'http://selenium1py.pythonanywhere.com/pt/catalogue/coders-at-work_207/')
    elif language_sel == 'pt-br':
        browser.get(f'http://selenium1py.pythonanywhere.com/pt-br/catalogue/coders-at-work_207/')
    elif language_sel == 'ro':
        browser.get(f'http://selenium1py.pythonanywhere.com/ro/catalogue/coders-at-work_207/')
    elif language_sel == 'sk':
        browser.get(f'http://selenium1py.pythonanywhere.com/sk/catalogue/coders-at-work_207/')
    elif language_sel == 'uk':
        browser.get(f'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/')
    elif language_sel == 'zh-cn':
        browser.get(f'http://selenium1py.pythonanywhere.com/zh-cn/catalogue/coders-at-work_207/')
    yield browser
    browser.quit()
