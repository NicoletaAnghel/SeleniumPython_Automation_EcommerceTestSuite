from venv import logger

from Esitetest.source.pages.locators.CheckOutPageLocators import CheckOutPAgeLocator
from Esitetest.source.selenium_extended import SeleniumExtended
from Esitetest.source.helpers.config_helpers import get_base_url
import logging as logger


class CheckOutPage(CheckOutPAgeLocator):

    endpoint = '/?page_id=9'
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_checkout(self):

        base_url = get_base_url()
        checkout_url = base_url + self.endpoint
        logger.info(f'Going to:  {checkout_url}')
        self.driver.get(checkout_url)

    def insert_email(self, email):
        self.sl.wait_and_input_text(self.CHECKOUT_EMAIL, email)

    def fill_biilling_address(self, fname, lname, address, city,postalcode, phone):
        self.sl.wait_and_input_text(self.CHECKOUT_FIRSTNAME,fname)
        self.sl.wait_and_input_text(self.CHECKOUT_LASTNAME, lname)
        self.sl.wait_and_input_text(self.CHECKOUT_ADDRESS, address)
        self.sl.wait_and_input_text(self.CHECKOUT_CITY, city)
        self.sl.wait_and_input_text(self.CHECKOUT_POSTALCODE, postalcode)
        self.sl.wait_and_input_text(self.CHECKOUT_PHONE_NO, phone)
    def make_cash_payment(self):
        self.sl.wait_and_click(self.CHECKOUT_PAYMENT_CASH)
    def make_direct_payment(self):
        self.sl.wait_and_click(self.CHECKOUT_PAYMENT_DIRECT)
    def add_note_checkbox(self):
        self.sl.wait_and_click(self.CHECKOUT_NOTE_CHECKBOX)
    def add_note_text(self, note):
        self.sl.wait_and_input_text(self.CHECKOUT_ORDER_NOTE, note)
    def click_outside_form(self):
        self.sl.wait_and_click(self.CHECKOUT_OUT_OF_FORM)
    def place_order(self,timeout):
        self.sl.wait_element_to_be_visible_and_clickable(self.CHECKOUT_PLACE_ORDER,timeout)

    def error_for_not_providing_email_as_guest(self, error_expected):
        self.sl.wait_until_element_contains_text(self.CHECKOUT_ERROR, error_expected)

    def click_on_create_acc_at_checkout(self):
        self.sl.wait_and_click(self.CHECKOUT_CREATE_ACC)

    def input_password_at_checkout(self, password):
        self.sl.wait_and_input_text(self.CHECKOUT_PASSWORD, password)


