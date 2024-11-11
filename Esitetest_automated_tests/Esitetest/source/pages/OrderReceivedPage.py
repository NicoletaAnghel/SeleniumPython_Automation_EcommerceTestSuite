from Esitetest.source.pages.locators.OrderReceivedPageLocators import OrderReceivedPageLocators
from Esitetest.source.selenium_extended import SeleniumExtended
from Esitetest.source.helpers.config_helpers import get_base_url
import logging as logger


class OrderReceivedPage(OrderReceivedPageLocators):

    endpoint = '/checkout/order-received/'
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_order_received(self):

        base_url = get_base_url()
        order_received_url = base_url + self.endpoint
        logger.info(f'Going to:  {order_received_url}')
        self.driver.get(order_received_url)

    def check_page_title(self,text, timeout):
        self.sl.wait_until_element_contains_text(self.PAGE_HEADER, text, timeout)

    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NUMBER)
