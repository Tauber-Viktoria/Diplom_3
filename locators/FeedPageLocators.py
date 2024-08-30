from selenium.webdriver.common.by import By


# локаторы для страницы Лента заказов
class FeedLocators:
    # Локатор для кнопки "Конструктор" в хеддере
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Локатор для поиска элемента заказа в ленте заказов по ID
    ORDER_FEED_ITEM_BY_ID = (By.XPATH,
                             "//p[contains(@class, 'text_type_digits-default') and contains(text(), '{order_id}')]")

    # Локатор для всплывающего окна с деталями заказа
    POPUP_ORDER_DETAILS_WINDOW = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")

    # Локатор для списка заказов "В работе"
    ORDER_READY_LIST = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi")

    # Локатор для ID заказа, содержащегося в списке заказов "В работе"
    ORDER_READY_ID = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text_type_digits-default")

    # Локатор для счётчика "Выполнено за все время"
    ORDER_COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']"
                                        "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")

    # Локатор для счётчика "Выполнено за сегодня"
    ORDER_COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']"
                                     "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")

    # Локатор последнего выполненного заказа в истории заказов
    LAST_ORDER_IN_HISTORY = (By.XPATH, f"(//p[contains(@class, 'text_type_digits-default')])[last()]")
