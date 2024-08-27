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
