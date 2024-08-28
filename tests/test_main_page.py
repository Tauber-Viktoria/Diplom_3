import allure
import url


class TestMainPage:
    @allure.feature('Переходы на страницы')
    @allure.story('Переход на страницу "Личный кабинет"')
    @allure.title('Тест перехода на страницу Личного кабинета по клику на кнопку "Личный кабинет" в хедере')
    def test_switch_from_main_to_personal_account(self, main_page, login_in):
        current_url = main_page.click_personal_account_button()
        assert current_url == url.ACCOUNT_URL, f"Ожидался URL {url.ACCOUNT_URL}, но был {current_url}."

    @allure.feature('Переходы на страницы')
    @allure.story('Переход на страницу "Конструктор"')
    @allure.title('Тест перехода на страницу Конструктора по клику на кнопку "Конструктор" в хедере')
    def test_switch_from_main_to_constructor(self, main_page, login_in):
        main_page.click_constructor_button()
        assert main_page.wait_for_title_burger(), "Заголовок 'Соберите бургер' не отобразился на экране"

    @allure.feature('Переходы на страницы')
    @allure.story('Переход на страницу "Личный кабинет"')
    @allure.title('Тест перехода на страницу Личного кабинета по клику на кнопку "Личный кабинет" в хедере')
    def test_switch_from_main_to_order_feed(self, main_page, login_in):
        current_url = main_page.click_personal_account_button()
        assert current_url == url.ACCOUNT_URL and main_page.wait_for_title_order_feed, \
            f"Ожидался URL {url.ACCOUNT_URL}, но был {current_url}."
