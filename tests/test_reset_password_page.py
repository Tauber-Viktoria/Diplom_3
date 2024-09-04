import allure


class TestResetPasswordPage:
    @allure.feature('Поля ввода')
    @allure.story('Функционал кнопки "Показать/Скрыть пароль"')
    @allure.title('Тест на проверку подсветки поля ввода пароля после нажатия кнопки "Показать/Скрыть пароль"')
    def test_password_field_highlighted_after_toggle(self, forgot_password_page, reset_password_page):
        email = 'mail@mail.ru'
        forgot_password_page.fill_email_link(email)
        forgot_password_page.click_reset_button()
        reset_password_page.wait_for_password_input()
        reset_password_page.toggle_password_visibility()
        assert reset_password_page.is_password_field_active(), ("Поле ввода пароля не стало активным после нажатия на "
                                                                "кнопку")

