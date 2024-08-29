import time

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
    @allure.story('Переход на страницу "Лента заказов"')
    @allure.title('Тест перехода на страницу "Лента заказов" по клику на кнопку "Лента заказов" в хедере')
    def test_switch_from_main_to_order_feed(self, main_page, login_in):
        current_url = main_page.click_order_feed_button()
        assert current_url == url.FEED_URL and main_page.wait_for_title_order_feed, \
            f"Ожидался URL {url.FEED_URL}, но был {current_url}."

    @allure.feature('Функционал сборки заказа')
    @allure.story('Открытие всплывающего окна с деталями ингридиента')
    @allure.title('Тест если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_popup_window_with_ingredient_details(self, main_page, login_in):
        main_page.click_ingredient()
        assert main_page.wait_for_popup_ingredient_details_window(), "Не открылось всплывающее окно с деталями"

    @allure.feature('Функционал сборки заказа')
    @allure.story('Закрытие всплывающего окна с заголовком "Детали ингредиента"')
    @allure.title('Тест всплывающее окно закрывается кликом по крестику')
    def test_close_popup_window_with_ingredient_details(self, main_page, login_in):
        main_page.click_ingredient()
        main_page.wait_for_popup_ingredient_details_window()
        main_page.click_cross_in_popup_window()
        assert main_page.is_popup_window_closed(), "Всплывающее окно не закрылось после клика по крестику."

    @allure.feature('Функционал сборки заказа')
    @allure.story('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.title('Тест на проверку увеличения каунтера у ингредиента который добавили в заказ')
    def test_add_ingredient_to_order(self, main_page, login_in):
        main_page.drag_and_drop_ingredient_bun()
        assert main_page.check_counter_num() == '2', "Всплывающее окно не закрылось после клика по крестику."

    @allure.feature('Функционал сборки заказа')
    @allure.story('Залогиненный пользователь может оформить заказ')
    @allure.title('Тест на проверку оформления заказа залогиненным пользователем')
    def test_place_order_as_logged_user(self, main_page, login_in):
        main_page.drag_and_drop_ingredient_bun()
        main_page.drag_and_drop_ingredient_souses()
        main_page.click_constructor_button()
        assert main_page.wait_for_popup_order_id_window(), "Не открылось всплывающее окно с индификатором заказа"
