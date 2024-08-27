import allure

from locators.AccountPageLocators import AccountLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step("клик на «История заказов»")
    def click_order_history_link(self):
        self.click_on_element(AccountLocators.ORDER_HISTORY_LINK)
        return self.get_current_url()

