import allure
import url

from locators.FeedPageLocators import FeedLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FeedPage(BasePage):
    @allure.step("клик на кнопку «Конструктор»")
    def click_constructor_button(self):
        self.click_on_element(FeedLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Поиск заказа в ленте заказов по ID {order_id} и клик по нему")
    def find_and_click_order_by_id(self, order_id):
        locator = (By.XPATH, FeedLocators.ORDER_FEED_ITEM_BY_ID[1].format(order_id=order_id))
        return self.click_on_element(locator)

    @allure.step("дождаться всплывающее окно c деталями заказа")
    def wait_for_popup_order_details_window(self):
        return self.is_element_present(FeedLocators.POPUP_ORDER_DETAILS_WINDOW)

    @allure.step("Ожидание появления ID заказа '{expected_order_id}' в разделе 'В работе'")
    def wait_for_order_id_in_ready_list(self, expected_order_id):
        self.wait_for_text_to_be(
            locator=FeedLocators.ORDER_READY_ID,
            expected_text=f'0{expected_order_id}',
            timeout=10
        )

    @allure.step("Получение ID заказа из раздела 'В работе'")
    def get_order_id_from_list_ready(self):
        element = self.find_element_with_wait(FeedLocators.ORDER_READY_ID)
        order_id = element.text.strip()
        return order_id

    @allure.step("Ожидание увеличения счётчика заказов 'Выполнено за все время' на 1")
    def wait_for_order_counter_all_time_to_increase(self, expected_count):
        self.wait_for_text_to_be(
            locator=FeedLocators.ORDER_COUNTER_ALL_TIME,
            expected_text=str(expected_count),
            timeout=15
        )

    @allure.step("Ожидание увеличения счётчика заказов 'Выполнено за сегодня' на 1")
    def wait_for_order_counter_today_to_increase(self, expected_count):
        self.wait_for_text_to_be(
            locator=FeedLocators.ORDER_COUNTER_TODAY,
            expected_text=str(expected_count),
            timeout=15
        )

    @allure.step("зафиксировать колличество заказов в разделе 'Выполнено за все время'")
    def get_number_orders_all_time(self):
        order_counter_text = self.get_text_from_element(FeedLocators.ORDER_COUNTER_ALL_TIME)
        return int(order_counter_text)

    @allure.step("зафиксировать колличество заказов в разделе 'Выполнено за сегодня'")
    def get_number_orders_today(self):
        order_counter_text = self.get_text_from_element(FeedLocators.ORDER_COUNTER_TODAY)
        return int(order_counter_text)

    @allure.step("Поиск заказа по ID {order_id}")
    def find_order_by_id(self, order_id):
        locator = (By.XPATH, f"//p[contains(@class, 'text_type_digits-default') and text()='#0{order_id}']")
        element = self.find_element_with_wait(locator)
        assert element, f"Заказ с ID {order_id} не найден."

    @allure.step("Cкролл до созданного заказа в истории заказов")
    def scroll_order_in_history(self):
        self.scroll_into_view(FeedLocators.LAST_ORDER_IN_HISTORY)

    def click_personal_account_button(self):
        self.click_on_element(FeedLocators.PERSONAL_ACCOUNT)
        self.wait_for_url(url.ACCOUNT_URL)
        return self.get_current_url()
