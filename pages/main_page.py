import allure

import url
from locators.MainPageLocators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("клик на «Личный кабинет»")
    def click_personal_account_button(self):
        self.click_on_element(MainLocators.PERSONAL_ACCOUNT)
        self.wait_for_url(url.ACCOUNT_URL)
        return self.get_current_url()

    @allure.step("клик на «Конструктор»")
    def click_constructor_button(self):
        self.click_on_element(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("дождаться заголовка «Соберите бургер»")
    def wait_for_title_burger(self):
        return self.is_element_present(MainLocators.ASSEMBLE_BURGER_TITLE)

    @allure.step("клик на «Личный кабинет»")
    def click_order_feed_button(self):
        self.click_on_element(MainLocators.ORDER_FEED_BUTTON)
        self.wait_for_url(url.FEED_URL)
        return self.get_current_url()

    @allure.step("дождаться заголовка «Лента заказов»")
    def wait_for_title_order_feed(self):
        return self.is_element_present(MainLocators.ORDER_FEED_TITLE)
