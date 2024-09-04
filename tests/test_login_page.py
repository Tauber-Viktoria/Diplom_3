import allure
import url


class TestLoginPage:
    @allure.feature('Переходы на страницы')
    @allure.story('Переход на первую страницу восстановления пароля')
    @allure.title('Тест перехода на первую страницу восстановления пароля по клику на "Восстановить пароль" на странице'
                  'активации')
    def test_switch_forgot_password_in_login(self, login_page):
        current_url = login_page.click_reset_password_link()
        assert current_url == url.FORGOT_PASSWORD_URL, (f"Ожидался URL {url.FORGOT_PASSWORD_URL}, "
                                                        f"но был {current_url}.")

