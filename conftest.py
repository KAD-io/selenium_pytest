import time

import pytest
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from const import BASE_URL, BROWSER, BROWSER_NAME, HEADLESS
from pages.main_page import MainPage


def get_browser_classes():
    if BROWSER == BROWSER_NAME.CHROME:
        return Chrome, ChromeService, ChromeOptions, ChromeDriverManager
    elif BROWSER == BROWSER_NAME.FIREFOX:
        return Firefox, FirefoxService, FirefoxOptions, GeckoDriverManager
    else:
        raise Exception(f'Invalid browser name = [{BROWSER}]')


def create_driver():
    webdriver_class, server_class, options_class, manager_class = get_browser_classes()
    manager = manager_class()
    service = server_class(manager.install())
    options = options_class()
    if HEADLESS:
        options.add_argument('--headless')
    driver = webdriver_class(options=options, service=service)
    driver.implicitly_wait(3)
    return driver


@pytest.fixture(scope='session')
def driver():
    driver_ = create_driver()
    yield driver_
    driver_.close()


@pytest.fixture(scope='session')
def a1_main_page(driver):
    main_page = MainPage(driver, BASE_URL)
    main_page.go_to_site()
    main_page.click_to_ru_local_button()
    main_page.kick_bad_bubbles()
    return main_page
