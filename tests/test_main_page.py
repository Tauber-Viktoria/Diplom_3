import allure
import url


class TestMainPage:
    @allure.feature('Переходы на страницы')
    @allure.story('Переход на страницу "Личный кабинет"')
    @allure.title('Тест перехода на страницу Личного кабинета по клику на кнопку "Личный кабинет" в хедере')
    def test_switch_personal_account_from_main(self, main_page, login_in):
        current_url = main_page.click_personal_account_button()
        assert current_url == url.ACCOUNT_URL, f"Ожидался URL {url.ACCOUNT_URL}, но был {current_url}."

