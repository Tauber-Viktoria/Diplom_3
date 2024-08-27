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
