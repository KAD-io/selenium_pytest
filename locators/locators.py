from selenium.webdriver.common.by import By


class Locators:
    RU_LOCAL_BUTTON = (By.XPATH, '//a[@href="#" and text()="RU"]')

    SHOP_BUTTON = (By.XPATH, '//a[@href="/ru/c/shop"]/span')
    CATALOG_PHONE_BUTTON = (By.XPATH, '//a/span[text()="Телефоны"]')

    SEARCH_BUTTON = (By.XPATH, '//button[@id="dropdownGlobalSearch"]')
    SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Что будем искать?"]')
    EMPTY_SEARCH_RESULTS = (By.XPATH, '//p[contains(text(), "ничего такого нет. Проверьте свой запрос")]')

    SORT_OPTION_SELECTED_BUTTON = (By.XPATH, '//span[@class="select2-selection__arrow"]')

    FILTER_BRAND_CHECKBUTTON = (By.XPATH, '//label[@for="i-brand-collapsed-0"]/span[@class="input-indicator"]')
    FILTER_BRAND_NAME = (By.XPATH, '//label[@for="i-brand-collapsed-0"]/span[@class="input-text"]')
    FILTER_BRAND_CHECK = (By.XPATH, '//input[@id="i-brand-collapsed-0"]')

    FILTER_MIN_PRICE_INPUT = (By.XPATH, '//input[@id = "i-range-box-from-0"]')
    FILTER_MAX_PRICE_INPUT = (By.XPATH, '//input[@id = "i-range-box-to-0"]')

    FILTER_STORAGE_CHECKBUTTON = (By.XPATH, '//label[@for="i-Обьем_встроенной_памяти_телефоны-collapsed-2"]/span[@class="input-indicator"]')
    FILTER_STORAGE_NAME = (By.XPATH, '//label[@for="i-Обьем_встроенной_памяти_телефоны-collapsed-2"]/span[@class="input-text"]')
    FILTER_STORAGE_CHECK = (By.XPATH, '//input[@id="i-Обьем_встроенной_памяти_телефоны-collapsed-2"]')

    CLEAR_ALL_FILTER_BUTTON = (By.XPATH, '//button[@class=" button chips-btn chips-btn--reset"]')

    DELIVERY_UNLOCK_INPUT_CITY = (By.XPATH, '//label[@id="radr_i-city_0"]//span[@class="select2-selection select2-selection--single"]')
    DELIVERY_INPUT_CITY = (By.XPATH, '//input[@tabindex="0"]')
    DELIVERY_INVALID_INPUT_CITY = (By.XPATH, '//li[text()="По Вашему запросу ничего не найдено"]')

    CATALOG_GO_TO_PURCHASE = (By.XPATH, '//a[@id="product-tile-button_0"]')

    CATALOG_GET_PRODUCTS = (By.XPATH, '//div[@data-product-code]')
    CATALOG_GET_HEADER_CATALOG = (By.XPATH, '//h1[@class="h h--2 "]')

    CATALOG_PRICE_PRODUCT = (By.XPATH, '//span[@id="one-time-price_0"]')
    CATALOG_PRICES_PRODUCTS = (By.XPATH, '//span[@class="price "]/span[@id]')

    CATALOG_HEADER_PRODUCT = (By.XPATH, '//div[@class="product-listing-body"]/div[1]//div[@class="product-search-item-title"]')
    CATALOG_HEADERS_PRODUCTS = (By.XPATH, '//div[@class="product-search-item-title"]')

    PRODUCT_HEADER_PRODUCT = (By.XPATH, '//h1[@class="h h--1 pdp-header-heading"]')
    PRODUCT_DISCOUNTED_PRICE = (By.XPATH, '//span[@class="price price"]/span[@class="price-value "]')
    PRODUCT_FULL_PRICE = (By.XPATH, '//div[@id="final-price-id-for-ajaxCURRENT_CONTRACT"]//span')
    PRODUCT_OPEN_SELECTOR_PAYMENT_OPTION = (By.XPATH, '//span[@class="select2-selection__arrow"]')
    PRODUCT_INPUT_SELECTOR_PAYMENT_OPTION = (By.XPATH, '//input[@class="select2-search__field"]')
    PRODUCT_BUTTON_QUANTITY_PLUS = (By.XPATH, '//button[@class="quantity-selector-button--plus quantity-selector-button btn js-qty-selector-plus "]')
    PRODUCT_BUTTON_QUANTITY_MINUS = (By.XPATH, '//button[@class="quantity-selector-button--minus quantity-selector-button btn js-qty-selector-minus "]')
    PRODUCT_INPUT_QUANTITY = (By.XPATH, '//input[@name="quantity"]')

    PRODUCT_BUTTON_BUY = (By.XPATH, '//form[@id="command"]//button[@data-product-offer]')

    CART_BUTTON_QUANTITY_PLUS = (By.XPATH, '//button[@class="quantity-selector-button--plus quantity-selector-button btn js-qty-selector-plus quantity-selector-card"]')
    CART_BUTTON_QUANTITY_MINUS = (By.XPATH, '//button[@class="quantity-selector-button--minus quantity-selector-button btn js-qty-selector-minus quantity-selector-card"]')
    CART_INPUT_QUANTITY = (By.XPATH, '//input[@id="i-qty0"]')

    CART_FULL_PRICE_PRODUCT = (By.XPATH, '//span[@id="card-total-price"]')
    CART_HEADER_PRODUCT = (By.XPATH, '//div[@class="review-item-main-info-card"]//span[@class="link-label"]')

    REMOVE_FROM_CART_BUTTON = (By.XPATH, '//button[@aria-label="Удалить"]')
    ACCEPT_REMOVE_BUTTON = (By.XPATH, '//button[@data-action-button="accept"]')
    CANCEL_REMOVE_BUTTON = (By.XPATH, '//button[@data-action-button="cancel"]')

    EMPTY_CART = (By.XPATH, '//p[text()="Корзина пуста. Перейдите в интернет-магазин, чтобы начать покупки."]')

    CLOSE_BUTTON_ONLINE_CONSULTANT = (By.XPATH, '//div[@class="wb-button__close ng-tns-c3-0 ng-trigger ng-trigger-displayButton ng-star-inserted"]')
    CLOSE_BUTTON_COOKIE_PANEL = (By.XPATH, '//button[@class="button button--primary cookie-panel-button"]')
    CLOSE_BUTTON_SPAM_PANEL = (By.XPATH, '//button[@class="popup__close-button--enpop"]')



