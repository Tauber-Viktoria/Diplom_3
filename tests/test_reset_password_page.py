import allure

from locators.ResetPasswordLocators import ResetPasswordLocators


class TestResetPasswordPage:
    @allure.feature('Поля ввода')
    @allure.story('Функционал кнопки "Показать/Скрыть пароль"')
    @allure.title('Тест на проверку подсветки поля ввода пароля после нажатия кнопки "Показать/Скрыть пароль"')
    def test_password_field_highlighted_after_toggle(self, forgot_password_page, reset_password_page):
        forgot_password_page.fill_email_link()
        forgot_password_page.click_reset_button()
        assert reset_password_page.is_element_present(ResetPasswordLocators.PASSWORD_INPUT_BEFORE), ("Поле ввода "
                                                                                                     "пароля не "
                                                                                                     "найдено")

        reset_password_page.toggle_password_visibility()
        assert reset_password_page.is_password_field_active(), ("Поле ввода пароля не стало активным после нажатия на "
                                                                "кнопку")

