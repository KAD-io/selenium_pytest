from selenium.webdriver import Keys, ActionChains

from const import VALUE_FOR_QUANTITY
from locators.locators import Locators
from pages.base_page import BasePage
from pages.cart_page import CartPage


class ProductPage(BasePage):
    name = None
    discounted_price = None
    full_price = None

    def get_header_product(self) -> str:
        header = self.find_element(Locators.PRODUCT_HEADER_PRODUCT)
        return header.text

    def get_discounted_price_product(self) -> float:
        price = self.find_element(Locators.PRODUCT_DISCOUNTED_PRICE)
        return float(price.text.replace(',', '.').replace(' ', ''))

    def get_full_price_product(self) -> float:
        price_element = self.find_element(Locators.PRODUCT_FULL_PRICE)
        price_str = price_element.text
        return float(price_str[0:len(price_str)-3].replace(',', '.').replace(' ', ''))

    def set_discounted_payment(self):
        self.click_to(Locators.PRODUCT_OPEN_SELECTOR_PAYMENT_OPTION)
        option_input = self.click_to(Locators.PRODUCT_INPUT_SELECTOR_PAYMENT_OPTION)
        for press_key in range(3):
            option_input.send_keys(Keys.DOWN)
        option_input.send_keys(Keys.ENTER)

    def set_full_payment(self):
        self.click_to(Locators.PRODUCT_OPEN_SELECTOR_PAYMENT_OPTION)
        option_input = self.click_to(Locators.PRODUCT_INPUT_SELECTOR_PAYMENT_OPTION)
        for press_key in range(4):
            option_input.send_keys(Keys.DOWN)
        option_input.send_keys(Keys.ENTER)

    def click_to_button_quantity_plus(self, count_click: int):
        for click in range(count_click):
            self.click_to(Locators.PRODUCT_BUTTON_QUANTITY_PLUS)

    def click_to_button_quantity_minus(self, count_click: int):
        for click in range(count_click):
            self.click_to(Locators.PRODUCT_BUTTON_QUANTITY_MINUS)

    def get_input_quantity(self) -> int:
        quantity = self.find_element(Locators.PRODUCT_INPUT_QUANTITY).get_attribute('value')
        return int(quantity)

    def set_initial_value(self):
        self.click_to(Locators.PRODUCT_INPUT_QUANTITY)
        ActionChains(self.driver)\
            .send_keys(Keys.LEFT).send_keys(Keys.LEFT).key_down(Keys.SHIFT)\
            .send_keys(Keys.RIGHT).send_keys(Keys.RIGHT).send_keys(Keys.RIGHT)\
            .key_up(Keys.SHIFT).send_keys(Keys.DELETE)\
            .send_keys(VALUE_FOR_QUANTITY.INITIAL).send_keys(Keys.ENTER).perform()

    def go_to_buy(self):
        self.click_to(Locators.PRODUCT_BUTTON_BUY)
        return CartPage(self.driver, self.driver.current_url)
