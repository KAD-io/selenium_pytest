from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.catalog_page import CatalogPage
from pages.search_page import SearchPage
from locators.locators import Locators


import time


class MainPage(BasePage):
    TITLE = 'A1 - провайдер телеком-, ИКТ- и контент-услуг'

    def search(self, request_string: str):
        self.click_to(Locators.SEARCH_BUTTON)
        search_input = self.click_to(Locators.SEARCH_INPUT)
        search_input.send_keys(request_string)
        search_input.send_keys(Keys.ENTER)
        return SearchPage(self.driver, self.driver.current_url)

    def go_to_catalog(self):
        shop_button = self.find_element(Locators.SHOP_BUTTON)
        ActionChains(self.driver).move_to_element(shop_button).perform()
        self.click_to(Locators.CATALOG_PHONE_BUTTON)
        return CatalogPage(self.driver, self.driver.current_url)

    def click_to_ru_local_button(self):
        self.click_to(Locators.RU_LOCAL_BUTTON)

    def kick_bad_bubbles(self):

        self.click_to(Locators.CLOSE_BUTTON_COOKIE_PANEL)
