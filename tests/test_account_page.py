import allure
import url


class TestAccountPage:
    @allure.feature('Переходы на страницы')
    @allure.story('Переход в раздел "История заказов"')
    @allure.title('Тест перехода в раздел "История заказов" на странице "Личный кабинет"')
    def test_switch_order_history_in_account(self, login_in, account_page):
        current_url = account_page.click_order_history_link()
        assert current_url == url.ACCOUNT_ORDER_HISTORY_URL, (f"Ожидался URL {url.ACCOUNT_ORDER_HISTORY_URL}, "
                                                              f"но был {current_url}.")

    @allure.feature('Переходы на страницы')
    @allure.story('Выход из аккаунта"')
    @allure.title('Тест выхода из аккаунта по клику "Выход" на странице "Личный кабинет"')
    def test_exit_in_account(self, login_in, account_page):
        current_url = account_page.click_exit_button()
        assert current_url == url.LOGIN_URL, f"Ожидался URL {url.LOGIN_URL}, но был {current_url}."