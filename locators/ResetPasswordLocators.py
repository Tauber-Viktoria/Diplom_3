from selenium.webdriver.common.by import By


# локаторы для второй страницы восстановления пароля
class ResetPasswordLocators:
    PASSWORD_INPUT_BEFORE = (By.CSS_SELECTOR, "div.input.input_type_password")
    PASSWORD_INPUT_AFTER = (By.CSS_SELECTOR, "div.input.input_type_text.input_status_active")
    TOGGLE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon.input__icon-action")
