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
