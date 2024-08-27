from selenium.webdriver.common.by import By


# локаторы для первой страницы восстановления пароля
class ForgotPasswordLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

