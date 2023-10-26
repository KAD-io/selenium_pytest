import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from const import REQUEST_STRING

import time


@pytest.fixture(scope='module')
def product_search(a1_main_page: MainPage):
    """
     тест поиска:
     -кликаем в поле поиска, вводим запрос, жмем Enter -> переходим на страницу поиска
    """
    search_page: SearchPage = a1_main_page.search(REQUEST_STRING)
    yield search_page
    a1_main_page.go_to_site()


def test_search_result_not_empty(product_search):
    """
     !!!проверяем что на странице поиска есть какой то результат и она не пуста
    """
    assert product_search.is_empty_result_placeholder_not_exists()
    assert product_search.get_products()


def test_relevant_header(product_search):
    """
    !!!проверяем что заголовок страницы поиска соответствует запросу
    """
    header_searched: str = product_search.get_header_catalog()
    assert header_searched == f'Результаты поиска для «{REQUEST_STRING}»'


def test_relevant_searched(product_search):
    """
    !!!проверяем что результат поиска соответствует запросу
    """
    all_headers_searched: list[str] = product_search.get_headers_products()
    assert all(searched.find(REQUEST_STRING) != -1 for searched in all_headers_searched)


class TestSearchResultsSort:
    """
    -кликаем на сортировку по убыванию (возрастанию) цены
     !!!проверяем что искомый товар отсортирован по убыванию (возрастанию) цены
    """
    def test_time(self, product_search):
        product_search.click_to_sort_option("цена ↑")
        #time.sleep(2)
        increasing_prices = product_search.get_prices_products()
        assert self.is_sort(increasing_prices)

    def test_ratings(self, product_search):
        product_search.click_to_sort_option("цена ↓")
        #time.sleep(2)
        decreasing_prices = product_search.get_prices_products()
        assert self.is_sort(decreasing_prices[::-1])

    @staticmethod
    def is_sort(arr: list) -> bool:
        ref_element = arr[0]
        for element in arr:
            if ref_element > element:
                return False
            ref_element = element
        return True
