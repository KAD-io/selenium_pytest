import os

BASE_URL = 'https://a1.by'
MASK_DATETIME = "%Y-%m-%dT%H:%M:%S.%fZ"
REQUEST_STRING = 'Samsung'


class ADDRESS:
    INVALID_CITY = 'Вашингтон'
    VALID_CITY = 'Париж'
    FULL_ADDRESS_CITY = 'аг. Париж, Козловщинский с/с, Поставский р-н, Витебская обл.'
    INVALID_STREET = 'Ленина'
    VALID_STREET = 'Молодежная'
    FULL_ADDRESS_STREET = 'ул. Молодёжная'


class VALUE_FOR_QUANTITY:
    MIN_PLUS = 9
    MAX_PLUS = 15
    MIN_MINUS = 2
    MAX_MINUS = 8
    INITIAL = 1

class TIMEOUTS:
    GET_URL = 30
    FIND_ELEMENT = 15


class PRICE_RANGE:
    MIN_PRICE = '2000'
    MAX_PRICE = '4000'


HEADLESS = os.getenv('HEADLESS', 1)


BROWSER = os.getenv('BROWSER', 'firefox')


class BROWSER_NAME:
    FIREFOX = 'firefox'
    CHROME = 'chrome'
