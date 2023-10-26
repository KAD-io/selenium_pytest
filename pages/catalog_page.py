import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.locators import Locators
from pages.base_page import BasePage
from pages.product_page import ProductPage


class CatalogPage(BasePage):

    def get_products(self) -> list[WebElement]:
        return self.find_elements(Locators.CATALOG_GET_PRODUCTS)

    def get_headers_products(self) -> list[str]:
        headers = self.find_elements(Locators.CATALOG_HEADERS_PRODUCTS)
        return [header.text for header in headers]

    def get_header_product(self) -> str:
        header = self.find_element(Locators.CATALOG_HEADER_PRODUCT)
        return header.text

    def get_header_catalog(self) -> str:
        header = self.find_element(Locators.CATALOG_GET_HEADER_CATALOG)
        return header.text

    def get_prices_products(self) -> list[float]:
        prices = self.find_elements(Locators.CATALOG_PRICES_PRODUCTS)
        return [float(price.text.replace(',', '.').replace(' ', '')) for price in prices]

    def get_price_product(self) -> float:
        price = self.find_element(Locators.CATALOG_PRICE_PRODUCT)
        return float(price.text.replace(',', '.').replace(' ', ''))

    def go_to_product(self):
        #time.sleep(2)
        self.click_to(Locators.CATALOG_GO_TO_PURCHASE)
        return ProductPage(self.driver, self.driver.current_url)

    """
    for sort
    """

    def click_to_sort_option(self, option: str):
        self.click_to(Locators.SORT_OPTION_SELECTED_BUTTON)
        self.click_to((By.XPATH, f'//div[text()="{option}"]'))

    """
    for filter
    """

    def click_to_filter_brand(self) -> str:
        self.click_to(Locators.FILTER_BRAND_CHECKBUTTON)
        #time.sleep(1.5)
        brand_name = self.find_element(Locators.FILTER_BRAND_NAME)
        return brand_name.text

    def is_filter_brand_checked(self):
        checkbox = self.find_element(Locators.FILTER_BRAND_CHECK)
        return checkbox.is_selected()

    def set_filter_price_range(self, min_price, max_price):
        price_input = self.click_to(Locators.FILTER_MIN_PRICE_INPUT)
        price_input.send_keys(min_price)
        price_input.send_keys(Keys.ENTER)
        time.sleep(3)
        price_input = self.click_to(Locators.FILTER_MAX_PRICE_INPUT)
        price_input.send_keys(max_price)
        price_input.send_keys(Keys.ENTER)
        time.sleep(3)

    def click_to_filter_storage(self) -> str:
        self.click_to(Locators.FILTER_STORAGE_CHECKBUTTON)
        #time.sleep(1.5)
        storage_name = self.find_element(Locators.FILTER_STORAGE_NAME)
        return storage_name.text.split()[0]

    def is_filter_storage_checked(self):
        checkbox = self.find_element(Locators.FILTER_STORAGE_CHECK)
        return checkbox.is_selected()

    def click_to_button_clear_filters(self):
        self.click_to(Locators.CLEAR_ALL_FILTER_BUTTON)
        #time.sleep(1.5)
