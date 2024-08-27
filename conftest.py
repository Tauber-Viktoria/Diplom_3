import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import password, login
from locators.LoginPageLocators import LoginLocators
from locators.MainPageLocators import MainLocators
from pages.account_page import AccountPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage

from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from url import MAIN_URL, ACCOUNT_URL, LOGIN_URL, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
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


@pytest.fixture
def login_in(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*MainLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginLocators.LOGIN_FIELD).send_keys(login)
    driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))
