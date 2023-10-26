from selenium.webdriver import ActionChains, Keys

from const import VALUE_FOR_QUANTITY
from locators.locators import Locators
from pages.base_page import BasePage


class CartPage(BasePage):

    name = None
    full_price = None

    def get_header_product(self) -> str:
        header = self.find_element(Locators.CART_HEADER_PRODUCT)
        return header.text

    def get_full_price_product(self) -> float:
        price_element = self.find_element(Locators.CART_FULL_PRICE_PRODUCT)
        price_str = price_element.text
        return float(price_str[0:len(price_str)-3].replace(',', '.').replace(' ', ''))

    def click_to_button_quantity_plus(self, count_click: int):
        for click in range(count_click):
            self.click_to(Locators.CART_BUTTON_QUANTITY_PLUS)

    def click_to_button_quantity_minus(self, count_click: int):
        for click in range(count_click):
            self.click_to(Locators.CART_BUTTON_QUANTITY_MINUS)

    def get_input_quantity(self) -> int:
        quantity = self.find_element(Locators.CART_INPUT_QUANTITY).get_attribute('value')
        return int(quantity)

    def set_initial_value(self):
        self.click_to(Locators.CART_INPUT_QUANTITY)
        ActionChains(self.driver)\
            .send_keys(Keys.LEFT).send_keys(Keys.LEFT).key_down(Keys.SHIFT)\
            .send_keys(Keys.RIGHT).send_keys(Keys.RIGHT).send_keys(Keys.RIGHT)\
            .key_up(Keys.SHIFT).send_keys(Keys.DELETE)\
            .send_keys(VALUE_FOR_QUANTITY.INITIAL).send_keys(Keys.ENTER).perform()

    def click_to_remove_button_with_accept(self):
        self.click_to(Locators.REMOVE_FROM_CART_BUTTON)
        self.click_to(Locators.ACCEPT_REMOVE_BUTTON)

    def click_to_remove_button_with_cancel(self):
        self.click_to(Locators.REMOVE_FROM_CART_BUTTON)
        self.click_to(Locators.CANCEL_REMOVE_BUTTON)

    def is_empty_result_placeholder_exists(self) -> bool:
        return self.is_exists(Locators.EMPTY_CART)
