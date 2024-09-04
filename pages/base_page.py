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

    # Найти элемент на странице.
    def find_element_with_wait(self, locator):
        WebDriverWait(
            self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Клик по элементу.
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Скролл до заданного элемента.
    def scroll_into_view(self, locator):
        element = self.find_element_with_wait(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    # Получить текст из элемента.
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    # Проверка наличия элемента на странице.
    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # Проверка отсуствия элемента на странице.
    def is_element_absent(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # Взять и перетащить элемент.
    def drag_and_drop_on_to_element(self, source_locator, target_locator):
        from_element = self.find_element_with_wait(source_locator)
        to_element = self.find_element_with_wait(target_locator)

        # JavaScript для перетаскивания элементов
        # PS НИЧЕГО НЕ СРАБАТЫВАЛО для Firefox кроме JavaScript
        self.driver.execute_script("""
            const [from_element, to_element] = arguments;
            const dataTransfer = new DataTransfer();

            ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
                const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
                (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
            });
        """, from_element, to_element)

    # Ожидает, пока текст элемента не изменится с initial_text на любой другой.
    def wait_for_text_to_change(self, locator, initial_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.find_element_with_wait(locator).text != initial_text)

    # Ожидание, пока текст элемента не станет равен ожидаемому значению
    def wait_for_text_to_be(self, locator, expected_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.find_element_with_wait(locator).text == expected_text)
