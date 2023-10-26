import pytest
import requests


class URLS:
    BASE_URL = 'https://send-request.me/'
    COMPANIES = f'{BASE_URL}api/companies/'
    USER = f'{BASE_URL}api/users/'
    AUTHORIZE = f'{BASE_URL}api/auth/authorize'


class MSG:
    INVALID_LOGIN = 'ensure this value has at least 3 characters'
    INVALID_PASS = 'Invalid password'


class COMPANY:
    BANKRUPT = {'id': 7, 'status': 'BANKRUPT'}
    CLOSED = {'id': 5, 'status': 'CLOSED'}
    ACTIVE = {'id': 3, 'status': 'ACTIVE'}


class BODY:
    USER_WITH_NOT_ACTIVE_COMPANY = [("James", "Bond", COMPANY.CLOSED['id']), ("James", "Bond", COMPANY.BANKRUPT['id'])]

    USER_WITH_ACTIVE_COMPANY = ("James", "Bond", COMPANY.ACTIVE['id'])

    VALID_AUTH = [('James Bond', 'qwerty12345'), ('Штирлиц', 'qwerty12345')]

    INVALID_AUTH_LOGIN = [('', 'qwerty12345'), ('B', 'qwerty12345'), ('JB', 'qwerty12345')]

    INVALID_AUTH_PASS = [('James Bond', ''), ('James Bond', '007'), ('James Bond', 'qwerty007')]


# @pytest.fixture()     ---!!!  почему то не проходит :(    !!!---
# def create_user(first_name, last_name, company_id):
#     body = {'first_name': first_name, 'last_name': last_name, 'company_id': company_id}
#     return requests.post(URLS.USER, json=body)

@pytest.fixture()
def create_user():
    first_name, last_name, company_id = BODY.USER_WITH_ACTIVE_COMPANY
    body = {'first_name': first_name, 'last_name': last_name, 'company_id': company_id}
    return requests.post(URLS.USER, json=body)

@pytest.fixture()
def create_negative_user():
    first_name, last_name, company_id = BODY.USER_WITH_NOT_ACTIVE_COMPANY[0]
    body = {'first_name': first_name, 'last_name': last_name, 'company_id': company_id}
    return requests.post(URLS.USER, json=body)

@pytest.fixture()
def authorize(login, password):
    body = {"login": login, "password": password}
    return requests.post(URLS.AUTHORIZE, json=body)


def test_is_request_companies_ok():
    assert requests.get(URLS.COMPANIES).status_code == 200


def test_is_request_companies_active():
    companies = requests.get(f'{URLS.COMPANIES}?status={COMPANY.ACTIVE["status"]}').json()['data']
    assert (all(company['company_status'] == COMPANY.ACTIVE["status"] for company in companies))


def test_is_request_companies_bankrupt():
    companies = requests.get(f'{URLS.COMPANIES}?status={COMPANY.BANKRUPT["status"]}').json()['data']
    assert (all(company['company_status'] == COMPANY.BANKRUPT["status"] for company in companies))


def test_is_request_companies_closed():
    companies = requests.get(f'{URLS.COMPANIES}?status={COMPANY.CLOSED["status"]}').json()['data']
    assert (all(company['company_status'] == COMPANY.CLOSED["status"] for company in companies))


def test_is_request_users_ok():
    assert requests.get(URLS.USER).status_code == 200


def test_code_create_negative_user(create_negative_user):
    assert create_negative_user.status_code == 400


def test_response_create_negative_user(create_negative_user):
    response = create_negative_user.json()
    assert str(response['detail']['reason']).find('Because it is not active') != -1


def test_code_create_user(create_user):
    assert create_user.status_code == 201


def test_response_create_user(create_user):
    response = create_user.json()
    created_user = requests.get(f'{URLS.USER}{response["user_id"]}').json()
    assert response == created_user


@pytest.mark.parametrize("login, password", BODY.VALID_AUTH)
def test_code_valid_auth(authorize):
    assert authorize.status_code == 200


@pytest.mark.parametrize("login, password", BODY.VALID_AUTH)
def test_response_valid_auth(authorize):
    assert authorize.json()['token']


@pytest.mark.parametrize("login, password", BODY.INVALID_AUTH_LOGIN)
def test_code_invalid_login_auth(authorize):
    assert authorize.status_code == 422


@pytest.mark.parametrize("login, password", BODY.INVALID_AUTH_LOGIN)
def test_response_invalid_login_auth(authorize):
    assert authorize.json()['detail'][0]['msg'] == MSG.INVALID_LOGIN


@pytest.mark.parametrize("login, password", BODY.INVALID_AUTH_PASS)
def test_code_invalid_pass_auth(authorize):
    assert authorize.status_code == 403


@pytest.mark.parametrize("login, password", BODY.INVALID_AUTH_PASS)
def test_response_invalid_pass_auth(authorize):
    assert authorize.json()['detail']['reason'] == MSG.INVALID_PASS
