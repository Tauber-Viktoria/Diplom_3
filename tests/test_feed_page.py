import allure


class TestFeedPage:
    @allure.feature('Раздел «Лента заказов»')
    @allure.story('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.title('Тест открытия модального окна по клику на оформленный заказ')
    def test_open_popup_window_with_order_details(self, main_page, feed_page, order_id):
        main_page.click_order_feed_button()
        feed_page.find_and_click_order_by_id(order_id)
        assert feed_page.wait_for_popup_order_details_window(), "Не открылось всплывающее окно с деталями заказа"

    @allure.feature('Раздел «Лента заказов»')
    @allure.story('После оформления заказа его номер появляется в разделе В работе')
    @allure.title('id созданного заказа отображается в разделе "В работе"')
    def test_display_id_order(self, main_page, feed_page, order_id):
        main_page.click_order_feed_button()
        assert feed_page.get_order_id_from_list_ready() == f'0{order_id}', \
            f"Ожидался ID заказа '0{order_id}', но получен {feed_page.get_order_id_from_list_ready()}"

    @allure.feature('Раздел «Лента заказов»')
    @allure.story('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.title('Тест на увеличение счётчика заказов "за все время" после добавления заказа')
    def test_order_counter_all_time_increases(self, main_page, feed_page, login_in):
        main_page.click_order_feed_button() # Переход в ленту заказов
        initial_count = feed_page.get_number_orders_all_time() # Зафиксировать текущее значение счётчика заказов
        main_page.click_constructor_button() # Переход в конструктор
        main_page.create_order() # Создать заказ
        main_page.click_order_feed_button() # Переход в ленту заказов
        new_count = feed_page.get_number_orders_all_time() # Зафиксировать новое значение счётчика
        assert new_count == initial_count + 1, \
            f"Ожидалось, что счётчик увеличится на 1, но он изменился с {initial_count} на {new_count}."

    @allure.feature('Раздел «Лента заказов»')
    @allure.story('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.title('Тест на увеличение счётчика заказов "за сегодня" после добавления заказа')
    def test_order_counter_all_time_increases(self, main_page, feed_page, login_in):
        main_page.click_order_feed_button() # Переход в ленту заказов
        initial_count = feed_page.get_number_orders_today() # Зафиксировать текущее значение счётчика заказов
        main_page.click_constructor_button() # Переход в конструктор
        main_page.create_order() # Создать заказ
        main_page.click_order_feed_button() # Переход в ленту заказов
        new_count = feed_page.get_number_orders_today() # Зафиксировать новое значение счётчика
        assert new_count == initial_count + 1, \
            f"Ожидалось, что счётчик увеличится на 1, но он изменился с {initial_count} на {new_count}."
