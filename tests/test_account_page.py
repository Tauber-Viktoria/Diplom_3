import allure
import url


class TestAccountPage:
    @allure.feature('Переходы на страницы')
    @allure.story('Переход в раздел "История заказов"')
    @allure.title('Тест перехода в раздел "История заказов" на странице "Личный кабинет"')
    def test_switch_order_history_in_account(self, login_in, account_page):
        account_page.click_order_history_link()
        current_url = account_page.click_order_history_link()
        assert current_url == url.ACCOUNT_ORDER_HISTORY_URL, "не произошел переход в раздел «История заказов»."

