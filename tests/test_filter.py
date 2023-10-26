import pytest

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from const import PRICE_RANGE


@pytest.fixture(scope='module')
def catalog_page_setup(a1_main_page: MainPage):
    """
     тест фильтров в каталоге:
     setup:
     -переходим в каталог со смартфонами
     -дожидаемся рекламного банера и закрываем его
    """
    catalog_page_: CatalogPage = a1_main_page.go_to_catalog()
    catalog_page_.click_to_close_spam()
    yield catalog_page_
    a1_main_page.go_to_site()


@pytest.fixture(scope='function')
def catalog_page(catalog_page_setup):
    """
    teardown:
    -сбрасываем фильтр
    """
    yield catalog_page_setup
    catalog_page_setup.click_to_button_clear_filters()

def test_filter_price(catalog_page):
    """
    -задаем в фильтре диапазон цен
    !!!проверяем что на странице каталога цены товара представлены в заданном диапазоне цен
    """
    catalog_page.set_filter_price_range(PRICE_RANGE.MIN_PRICE, PRICE_RANGE.MAX_PRICE)
    prices_products: list[float] = catalog_page.get_prices_products()
    assert all(float(PRICE_RANGE.MIN_PRICE) <= price_product <= float(PRICE_RANGE.MAX_PRICE)
               for price_product in prices_products)


def test_filter_brand(catalog_page):
    """
    !!!проверяем что на странице каталога фильтр по бренду не задан
    -задаем в фильтре определенный бренд
    !!!проверяем что на странице каталога фильтр по бренду задан
    !!!проверяем что на странице каталога бренд товара представлен в соответствии фильтру
    """
    catalog_page.driver.execute_script("window.scrollTo(0, 150)")
    assert not catalog_page.is_filter_brand_checked()
    brand_name = catalog_page.click_to_filter_brand()
    assert catalog_page.is_filter_brand_checked()
    headers_products: list[str] = catalog_page.get_headers_products()
    assert all(header_product.find(brand_name) != -1 for header_product in headers_products)


def test_filter_storage(catalog_page):
    """
    !!!проверяем что на странице каталога фильтр по паияти не задан
     -задаем в фильтре внутреннею память
    !!!проверяем что на странице каталога фильтр по паияти задан
    !!!проверяем что на странице каталога внутренняя память товара представлены в соответствии фильтру
    """
    catalog_page.driver.execute_script("window.scrollTo(0, 1500)")
    assert not catalog_page.is_filter_storage_checked()
    storage = catalog_page.click_to_filter_storage()
    assert catalog_page.is_filter_storage_checked()
    headers_products: list[str] = catalog_page.get_headers_products()
    assert all(header_product.find(storage) != -1 for header_product in headers_products)

