
from selenium.webdriver.common.by import By

class OrderReceivedPageLocators:
    PAGE_HEADER = (By.CSS_SELECTOR, '.entry-header')
    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.order strong')