from locators.locators import Locators
from pages.catalog_page import CatalogPage


class SearchPage(CatalogPage):

    def is_empty_result_placeholder_not_exists(self) -> bool:
        return self.is_not_exists(Locators.EMPTY_SEARCH_RESULTS)
