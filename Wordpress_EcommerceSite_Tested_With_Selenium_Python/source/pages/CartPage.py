from itertools import product

from Esitetest.source.selenium_extended import SeleniumExtended
from Esitetest.source.pages.locators.CartPageLocators import CartPageLocators
from Esitetest.source.helpers.config_helpers import get_base_url
import logging as logger


class CartPage(CartPageLocators):

    endpoint = '/cart/'
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart(self):

        base_url = get_base_url()
        cart_url = base_url + self.endpoint
        logger.info(f'Going to:  {cart_url}')
        self.driver.get(cart_url)

    def get_all_items_names_in_cart(self):
        product_name_elements = self.sl.wait_and_get_elements(self.ITEM_IN_CART)
        if product_name_elements:
            product_names =[i.text for i in product_name_elements]
        else:
            product_names =[]
        return product_names


    def go_to_coupon(self):
        self.sl.wait_and_click(self.ACTIVATE_COUPON_FIELD)

    def add_coupon(self, coupon):
        self.sl.wait_and_input_text(self.COUPON_FIELD,coupon)

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def check_cart_total_amount(self, text):
        self.sl.wait_until_element_contains_text(self.CART_TOTAL, text)

    def check_apply_coupon_message(self, expected_text):
        self.sl.wait_until_element_contains_text(self.CART_PAGE_MESSAGE_COUPON, expected_text)


    def go_to_checkout(self, timeout):
        self.sl.wait_and_click(self.CHECK_OUT_BTN, timeout)
