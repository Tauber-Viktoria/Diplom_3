import allure
import url


class TestForgotPasswordPage:
    @allure.feature('Переходы на страницы')
    @allure.story('Переход на вторую страницу восстановления пароля')
    @allure.title('Тест перехода на вторую страницу восстановления пароля по клику на "Восстановить" на первой странице'
                  'восстановления пароля')
    def test_switch_from_forgot_password_to_reset_password(self, forgot_password_page):
        forgot_password_page.fill_email_link()
        current_url = forgot_password_page.click_reset_button()
        assert current_url == url.RESET_PASSWORD_URL, (f"Ожидался URL {url.RESET_PASSWORD_URL}, "
                                                       f"но был {current_url}.")
