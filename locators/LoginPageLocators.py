from selenium.webdriver.common.by import By


# локаторы для страницы активации
class LoginLocators:
    LOGIN_FIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESET_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
