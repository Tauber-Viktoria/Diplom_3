import pytest
import allure
import url


class TestMainPage:
    @allure.feature('Переходы на страницы')
    @allure.story('Переход на страницу "Личный кабинет"')
    @allure.title('Тест перехода на страницу Личного кабинета по клику на кнопку "Личный кабинет" в хедере')
    def test_switch_personal_account_from_main(self, main_page, login_in):
        main_page.click_personal_account_button()
        current_url = main_page.click_personal_account_button()
        assert current_url == url.ACCOUNT_URL, "не произошел переход на главную страницу «Личный кабинет»."

