from selenium.webdriver.common.by import By


# локаторы для страницы личного кабинета
class AccountLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
