import allure
import url
from locators.MainPageLocators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("клик на кнопку «Личный кабинет»")
    def click_personal_account_button(self):
        self.click_on_element(MainLocators.PERSONAL_ACCOUNT)
        self.wait_for_url(url.ACCOUNT_URL)
        return self.get_current_url()

    @allure.step("клик на кнопку «Конструктор»")
    def click_constructor_button(self):
        self.click_on_element(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("дождаться заголовка «Соберите бургер»")
    def wait_for_title_burger(self):
        return self.is_element_present(MainLocators.ASSEMBLE_BURGER_TITLE)

    @allure.step("клик на кнопку «Лента заказов»")
    def click_order_feed_button(self):
        self.click_on_element(MainLocators.ORDER_FEED_BUTTON)
        self.wait_for_url(url.FEED_URL)
        return self.get_current_url()

    @allure.step("дождаться заголовка «Лента заказов»")
    def wait_for_title_order_feed(self):
        return self.is_element_present(MainLocators.ORDER_FEED_TITLE)

    @allure.step("клик на ингредиент")
    def click_ingredient(self):
        self.click_on_element(MainLocators.BURGER_INGREDIENT_BUN)

    @allure.step("дождаться всплывающее окно ингредиента")
    def wait_for_popup_ingredient_details_window(self):
        return self.is_element_present(MainLocators.POPUP_INGREDIENT_DETAILS_WINDOW)

    @allure.step("клик на крестик во всплывающем окне ингредиентв")
    def click_cross_in_popup_window(self):
        self.click_on_element(MainLocators.CLOSE_BUTTON)

    @allure.step("Проверка, что всплывающее окно ингредиента закрыто")
    def is_popup_window_closed(self):
        return self.is_element_absent(MainLocators.POPUP_INGREDIENT_DETAILS_WINDOW)

    @allure.step("Добавление ингредиента Булки в заказ")
    def drag_and_drop_ingredient_bun(self):
        return self.drag_and_drop_on_to_element(MainLocators.BURGER_INGREDIENT_BUN,
                                                MainLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step("Проверка каунтера ингридиента")
    def check_counter_num(self):
        return self.get_text_from_element(MainLocators.COUNTER_BUN)

    @allure.step("Добавление ингредиента Соусы в заказ")
    def drag_and_drop_ingredient_souses(self):
        return self.drag_and_drop_on_to_element(MainLocators.BURGER_INGREDIENT_SOUSES,
                                                MainLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step("клик на кнопку «Оформить заказ»")
    def click_place_order_button(self):
        self.click_on_element(MainLocators.ORDER_BUTTON)

    @allure.step("дождаться всплывающее окно c заказом")
    def wait_for_popup_order_id_window(self):
        return self.is_element_present(MainLocators.POPUP_ORDER_ID_WINDOW)

    # Метод для получения ID заказа из всплывающего окна
    @allure.step("Получение ID заказа из всплывающего окна")
    def get_order_id_from_popup(self):
        self.wait_for_text_to_change(
            MainLocators.ORDER_ID_TITLE,
            initial_text="9999",
            timeout=10
        )
        element = self.find_element_with_wait(MainLocators.ORDER_ID_TITLE)
        order_id = element.text
        return order_id

    def create_order(self):
        self.drag_and_drop_ingredient_bun()
        self.drag_and_drop_ingredient_souses()
        self.click_place_order_button()  # нажать на оформление заказа
        self.get_order_id_from_popup()
        self.click_cross_in_popup_window()  # нажать на крестик

