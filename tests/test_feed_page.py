import allure
import pytest


class TestFeedPage:
    @allure.feature('Раздел «Лента заказов»')
    @allure.story('После оформления заказа его номер появляется в разделе В работе')
    @allure.title('Тест на отображение id созданного заказа в разделе "В работе"')
    def test_display_id_order(self, main_page, feed_page, order_id):
        main_page.click_order_feed_button()
        feed_page.wait_for_order_id_in_ready_list(order_id)
        assert feed_page.get_order_id_from_list_ready() == f'0{order_id}', \
            f"Ожидался ID заказа '0{order_id}', но получен {feed_page.get_order_id_from_list_ready()}"

    @allure.feature('Раздел «Лента заказов»')
    @allure.story('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.title('Тест на отображение собранного заказа в ленте заказов и открытия модального окна по клику на заказ')
    def test_open_popup_window_with_order_details(self, main_page, feed_page, order_id):
        main_page.click_order_feed_button()
        feed_page.find_and_click_order_by_id(order_id)
        assert feed_page.wait_for_popup_order_details_window(), "Не открылось всплывающее окно с деталями заказа"

    @pytest.mark.parametrize(
        "counter_name, get_initial_count, get_new_count, story, title",
        [
            (
                    "за все время",
                    lambda feed_page: feed_page.get_number_orders_all_time(),
                    lambda feed_page: feed_page.get_number_orders_all_time(),
                    "При создании нового заказа счётчик Выполнено за всё время увеличивается",
                    'Тест на увеличение счётчика заказов "за все время" после добавления заказа',
            ),
            (
                    "за сегодня",
                    lambda feed_page: feed_page.get_number_orders_today(),
                    lambda feed_page: feed_page.get_number_orders_today(),
                    "При создании нового заказа счётчик Выполнено за сегодня увеличивается",
                    'Тест на увеличение счётчика заказов "за сегодня" после добавления заказа',
            ),
        ],
    )
    @allure.feature('Раздел «Лента заказов»')
    def test_order_counter_increases(self, main_page, feed_page, login_in,
                                     counter_name, get_initial_count, get_new_count, story, title):
        allure.dynamic.story(story)
        allure.dynamic.title(title)

        main_page.click_order_feed_button()  # Переход в ленту заказов
        initial_count = get_initial_count(feed_page)  # Зафиксировать текущее значение счётчика заказов
        main_page.click_constructor_button()  # Переход в конструктор
        main_page.create_order()  # Создать заказ
        main_page.click_order_feed_button()  # Переход в ленту заказов
        new_count = get_new_count(feed_page)  # Зафиксировать новое значение счётчика
        assert new_count == initial_count + 1, \
            f"Ожидалось, что счётчик увеличится на 1, но он изменился с {initial_count} на {new_count}."

    @allure.feature('Раздел «Лента заказов»')
    @allure.story('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.title('Тест на отображение заказа из раздела "История заказов" на странице «Лента заказов»')
    def test_display_id_order_from_order_history(self, main_page, feed_page, account_page, order_id):
        main_page.click_order_feed_button()
        order_id_in_feed = feed_page.find_order_by_id(order_id)
        feed_page.click_personal_account_button()
        account_page.click_order_history_link()
        feed_page.scroll_order_in_history()
        order_id_in_history = feed_page.find_order_by_id(order_id)
        assert order_id_in_feed == order_id_in_history
