from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Открыть страницу по URL.
    def get_url(self, url):
        self.driver.get(url)

    # Получить текущий URL.
    def get_current_url(self):
        return self.driver.current_url

    # Ждать, пока текущий URL не станет равен ожидаемому.
    def wait_for_url(self, url, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))

    def find_element_with_wait(self, locator):
        WebDriverWait(
            self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def scroll_into_view(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    # Проверка наличия элемента на странице
    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # Проверка отсуствия элемента на странице
    def is_element_absent(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def drag_and_drop_on_to_element(self, element_from, element_to):
        element_from = self.find_element_with_wait(element_from)
        element_to = self.find_element_with_wait(element_to)
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()

    # Ожидает, пока текст элемента не изменится с initial_text на любой другой
    def wait_for_text_to_change(self, locator, initial_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.find_element_with_wait(locator).text != initial_text
        )
