import random
import time

import pytest

from const import VALUE_FOR_QUANTITY
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

"""
    тест подготовки к закупке:
     -переходим в каталог со смартфонами
     -кликаем на первый смартфон -> переходим на страницу продукта (смартфона)
     !!!проверяем что на странице продукта смартфон соответствует тому на который кликнули
        !!!по описанию
        !!!по цене
     !!!проверяем на странице продукта проверяем что при нажатии +-  
        !!!количество продукта меняется правильно
        !!!цена для измененного количества считается правильно
     -выбираем оплатить полностью
     -жмем купить
     !!!на странице корзины проверяем что смартфон соответствует 
        !!!описанию
        !!!цене
     !!!на странице карнизы проверяем что при нажатии +-
        !!!количество продукта меняется правильно
        !!!цена для измененного количества считается правильно
     -жмем удалить тавра из карнизы без подтверждения
     !!!на странице карнизы проверяем что она не пуста
     -жмем удалить тавра из карнизы с подтверждением
     !!!на странице карнизы проверяем что она пуста
"""


@pytest.fixture(scope='module')
def product_page(a1_main_page: MainPage):
    catalog_page: CatalogPage = a1_main_page.go_to_catalog()
    product_name = catalog_page.get_header_product()
    product_price = catalog_page.get_price_product()
    catalog_page.driver.execute_script("window.scrollTo(0, 200)")
    product_page_: ProductPage = catalog_page.go_to_product()
    product_page_.name = product_name
    product_page_.discounted_price = product_price
    yield product_page_
    a1_main_page.go_to_site()


@pytest.fixture(scope='class')
def product_page_calc_setup(product_page: ProductPage):
    product_page.set_full_payment()
    product_page.full_price = product_page.get_full_price_product()
    yield product_page


@pytest.fixture(scope='function')
def product_page_calc(product_page_calc_setup: ProductPage):
    yield product_page_calc_setup
    product_page_calc_setup.set_initial_value()


@pytest.fixture(scope='class')
def cart_page(product_page_calc_setup: ProductPage):
    cart_page_: CartPage = product_page_calc_setup.go_to_buy()
    cart_page_.name = product_page_calc_setup.name
    cart_page_.full_price = product_page_calc_setup.full_price
    yield cart_page_


@pytest.fixture(scope='function')
def cart_page_calc(cart_page: CartPage):
    yield cart_page
    cart_page.set_initial_value()
    time.sleep(1.5)


class TestPreparationPurchase:
    @staticmethod
    def test_conformity_header(product_page):
        assert product_page.get_header_product() == product_page.name

    @staticmethod
    def test_conformity_discounted_price(product_page):
        product_page.set_discounted_payment()
        assert product_page.get_discounted_price_product() == product_page.discounted_price


class TestCalcFullPrice:

    @staticmethod
    def test_button_quantity_plus(product_page_calc):
        assert product_page_calc.get_input_quantity() == VALUE_FOR_QUANTITY.INITIAL
        count_click_plus = random.randint(VALUE_FOR_QUANTITY.MIN_PLUS, VALUE_FOR_QUANTITY.MAX_PLUS)
        product_page_calc.click_to_button_quantity_plus(count_click_plus)
        time.sleep(0.5)
        assert product_page_calc.get_input_quantity() == VALUE_FOR_QUANTITY.INITIAL + count_click_plus
        assert (product_page_calc.get_full_price_product() ==
                product_page_calc.full_price * (VALUE_FOR_QUANTITY.INITIAL + count_click_plus))

    @staticmethod
    def test_button_quantity_minus(product_page_calc):
        assert product_page_calc.get_input_quantity() == VALUE_FOR_QUANTITY.INITIAL
        count_click_plus = random.randint(VALUE_FOR_QUANTITY.MIN_PLUS, VALUE_FOR_QUANTITY.MAX_PLUS)
        count_click_minus = random.randint(VALUE_FOR_QUANTITY.MIN_MINUS, VALUE_FOR_QUANTITY.MAX_MINUS)
        product_page_calc.click_to_button_quantity_plus(count_click_plus)
        product_page_calc.click_to_button_quantity_minus(count_click_minus)
        time.sleep(0.5)
        assert (product_page_calc.get_input_quantity() ==
                VALUE_FOR_QUANTITY.INITIAL + count_click_plus - count_click_minus)
        assert (product_page_calc.get_full_price_product() ==
                product_page_calc.full_price * (VALUE_FOR_QUANTITY.INITIAL + count_click_plus - count_click_minus))


class TestPurchaseInCart:
    @staticmethod
    def test_conformity_header_in_cart(cart_page):
        assert cart_page.get_header_product() == cart_page.name

    @staticmethod
    def test_conformity_price_in_cart(cart_page):
        assert cart_page.get_full_price_product() == cart_page.full_price

    @staticmethod
    def test_button_quantity_plus_in_cart(cart_page_calc):
        assert cart_page_calc.get_input_quantity() == VALUE_FOR_QUANTITY.INITIAL
        count_click_plus = random.randint(VALUE_FOR_QUANTITY.MIN_PLUS, VALUE_FOR_QUANTITY.MAX_PLUS)
        cart_page_calc.click_to_button_quantity_plus(count_click_plus)
        time.sleep(0.5)
        assert cart_page_calc.get_input_quantity() == VALUE_FOR_QUANTITY.INITIAL + count_click_plus
        assert (cart_page_calc.get_full_price_product() ==
                cart_page_calc.full_price * (VALUE_FOR_QUANTITY.INITIAL + count_click_plus))

    @staticmethod
    def test_button_quantity_minus_in_cart(cart_page_calc):
        assert cart_page_calc.get_input_quantity() == VALUE_FOR_QUANTITY.INITIAL
        count_click_plus = random.randint(VALUE_FOR_QUANTITY.MIN_PLUS, VALUE_FOR_QUANTITY.MAX_PLUS)
        count_click_minus = random.randint(VALUE_FOR_QUANTITY.MIN_MINUS, VALUE_FOR_QUANTITY.MAX_MINUS)
        cart_page_calc.click_to_button_quantity_plus(count_click_plus)
        cart_page_calc.click_to_button_quantity_minus(count_click_minus)
        time.sleep(0.5)
        assert (cart_page_calc.get_input_quantity() ==
                VALUE_FOR_QUANTITY.INITIAL + count_click_plus - count_click_minus)
        assert (cart_page_calc.get_full_price_product() ==
                cart_page_calc.full_price * (VALUE_FOR_QUANTITY.INITIAL + count_click_plus - count_click_minus))

    @staticmethod
    def test_remove_with_cancel(cart_page):
        cart_page.click_to_remove_button_with_cancel()
        assert not cart_page.is_empty_result_placeholder_exists()

    @staticmethod
    def test_remove_with_accept(cart_page):
        cart_page.click_to_remove_button_with_accept()

        assert cart_page.is_empty_result_placeholder_exists()
