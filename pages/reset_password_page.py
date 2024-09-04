import allure

from locators.ResetPasswordLocators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step("клик на кнопку 'Показать/Скрыть пароль'")
    def toggle_password_visibility(self):
        self.click_on_element(ResetPasswordLocators.TOGGLE_PASSWORD_BUTTON)

    @allure.step("дождаться поля ввода пароля")
    def wait_for_password_input(self):
        return self.is_element_present(ResetPasswordLocators.PASSWORD_INPUT_BEFORE)

    @allure.step('проверка активации кнопки "показать/скрыть пароль"')
    def is_password_field_active(self):
        return self.is_element_present(ResetPasswordLocators.PASSWORD_INPUT_AFTER)
