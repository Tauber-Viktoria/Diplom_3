import allure
import url

from locators.AccountPageLocators import AccountLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step("клик на «История заказов»")
    def click_order_history_link(self):
        self.click_on_element(AccountLocators.ORDER_HISTORY_LINK)
        self.wait_for_url(url.ACCOUNT_ORDER_HISTORY_URL)
        return self.get_current_url()

    @allure.step("Клик на кнопку «Выход»")
    def click_exit_button(self):
        self.click_on_element(AccountLocators.EXIT_BUTTON)
        self.wait_for_url(url.LOGIN_URL)
        return self.get_current_url()
