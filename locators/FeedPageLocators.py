from selenium.webdriver.common.by import By


# локаторы для страницы Лента заказов
class FeedLocators:
    # Локатор для поиска элемента заказа в ленте заказов по ID
    ORDER_FEED_ITEM_BY_ID = (By.XPATH,
                             "//p[contains(@class, 'text_type_digits-default') and contains(text(), '{order_id}')]")

    # Локатор для всплывающего окна с деталями заказа
    POPUP_ORDER_DETAILS_WINDOW = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")

    # Локатор для списка заказов "В работе"
    ORDER_READY_LIST = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi")

    # Локатор для ID заказа, содержащегося в списке заказов "В работе"
    ORDER_READY_ID = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text_type_digits-default")

    # Локатор для счётчика заказов за все время
    ORDER_COUNTER_ALL_TIME = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ.text.text_type_digits-large")

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

