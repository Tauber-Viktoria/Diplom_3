import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


from pages.account_page import AccountPage
from pages.feed_page import FeedPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from register_user import register_new_user, delete_new_user

from url import MAIN_URL, ACCOUNT_URL, LOGIN_URL, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL, FEED_URL


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)

    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.get_url(MAIN_URL)
    return page


@pytest.fixture()
def account_page(driver):
    page = AccountPage(driver)
    page.get_url(ACCOUNT_URL)
    return page


@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver)
    page.get_url(LOGIN_URL)
    return page


@pytest.fixture()
def forgot_password_page(driver):
    page = ForgotPasswordPage(driver)
    page.get_url(FORGOT_PASSWORD_URL)
    return page


@pytest.fixture()
def reset_password_page(driver):
    page = ResetPasswordPage(driver)
    page.get_url(RESET_PASSWORD_URL)
    return page


@pytest.fixture()
def feed_page(driver):
    page = FeedPage(driver)
    page.get_url(FEED_URL)
    return page


# Создание заказа и получение ID заказа
@pytest.fixture()
def order_id(main_page, login_in):
    main_page.drag_and_drop_ingredient_bun()
    main_page.drag_and_drop_ingredient_souses()
    main_page.click_place_order_button()
    order_id = main_page.get_order_id_from_popup()
    main_page.click_cross_in_popup_window()
    return order_id


@pytest.fixture
def login():
    user_data, response = register_new_user() # Регистрация нового пользователя
    yield user_data
    access_token = user_data.get('access_token')
    delete_new_user(access_token)  # Вызов функции удаления пользователя


@pytest.fixture
def login_in(login, login_page):

    email = login['email']
    password = login['password']

    login_page.set_email(email)
    login_page.set_password(password)
    login_page.click_login_button()
