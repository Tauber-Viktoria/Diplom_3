import allure
import url

from locators.ForgotPasswordLocators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step("Заполнить поле email")
    def fill_email_link(self, email):
        self.find_element_with_wait(ForgotPasswordLocators.EMAIL_FIELD).send_keys(email)

    @allure.step("клик на кнопку 'Восстановить'")
    def click_reset_button(self):
        self.click_on_element(ForgotPasswordLocators.RESET_BUTTON)
        self.wait_for_url(url.RESET_PASSWORD_URL)
        return self.get_current_url()
