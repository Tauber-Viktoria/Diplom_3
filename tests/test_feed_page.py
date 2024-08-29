import allure


class TestFeedPage:
    @allure.feature('Раздел «Лента заказов»')
    @allure.story('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.title('Тест открытия модального окна по клику на оформленный заказ')
    def test_open_popup_window_with_order_details(self, main_page, feed_page, create_order):
        order_id = create_order
        main_page.click_order_feed_button()
        feed_page.find_and_click_order_by_id(order_id)
        assert feed_page.wait_for_popup_order_details_window(), "Не открылось всплывающее окно с деталями заказа"

    @allure.feature('Раздел «Лента заказов»')
    @allure.story('После оформления заказа его номер появляется в разделе В работе')
    @allure.title('id созданного заказа отображается в разделе "В работе"')
    def test_display_id_order(self, main_page, feed_page, create_order):
        order_id = create_order
        main_page.click_order_feed_button()
        assert feed_page.get_order_id_from_list_ready() == f'0{order_id}', \
            f"Ожидался ID заказа '0{order_id}', но получен {feed_page.get_order_id_from_list_ready()}"

    @allure.feature('Раздел «Лента заказов»')
    @allure.story('Количество заказов увеличивается после добавления нового заказа')
    @allure.title('Тест на увеличение счётчика заказов после добавления заказа')
    def test_order_counter_increases(self, main_page, feed_page, login_in):
        main_page.click_order_feed_button()
        # Зафиксировать текущее значение счётчика заказов
        initial_count = feed_page.get_number_orders_all_time()
        feed_page.click_constructor_button()
        main_page.drag_and_drop_ingredient_bun()
        main_page.drag_and_drop_ingredient_souses()
        main_page.click_place_order_button() # нажать на оформление заказа
        main_page.get_order_id_from_popup()
        main_page.click_cross_in_popup_window() # нажать на крестик

        main_page.click_order_feed_button() # нажать на ленту заказов

        # Проверить, что заказ был добавлен и зафиксировать новое значение счётчика
        new_count = feed_page.get_number_orders_all_time()

        # Проверить, что счётчик увеличился на 1
        assert new_count == initial_count + 1, \
            f"Ожидалось, что счётчик увеличится на 1, но он изменился с {initial_count} на {new_count}."
