import allure
import url

from locators.LoginPageLocators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("клик на «Восстановить пароль")
    def click_reset_password_link(self):
        self.click_on_element(LoginLocators.RESET_PASSWORD_LINK)
        self.wait_for_url(url.FORGOT_PASSWORD_URL)
        return self.get_current_url()

    @allure.step("заполнить поле «Email")
    def set_email(self, login):
        self.find_element_with_wait(LoginLocators.LOGIN_FIELD).send_keys(login)

    @allure.step("заполнить поле «Пароль")
    def set_password(self, password):
        self.find_element_with_wait(LoginLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step("клик на «Войти")
    def click_login_button(self):
        self.click_on_element(LoginLocators.LOGIN_BUTTON)
        self.wait_for_url(url.MAIN_URL)
        return self.get_current_url()
