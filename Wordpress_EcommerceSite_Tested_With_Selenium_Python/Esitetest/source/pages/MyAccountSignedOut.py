
from Esitetest.source.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from Esitetest.source.selenium_extended import SeleniumExtended
from Esitetest.source.helpers.config_helpers import get_base_url
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint = '/my-account/'
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):

        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info('Going to:  {my_account_url}')
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username,)

    def find_login_username_field(self):
        self.sl.wait_until_element_is_visible(self.LOGIN_USER_NAME)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_USER_PASSWORD, password)

    def find_login_password_field(self):
        self.sl.wait_until_element_is_visible(self.LOGIN_USER_PASSWORD)

    def click_login_button(self):
        logger.debug('Clicking on "login" button.')
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def wait_until_error_is_displayed(self, exp_error):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_error)

    def register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def find_register_email_field(self):
        self.sl.wait_until_element_is_visible(self.REGISTER_EMAIL)

    def register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASS, password)

    def find_register_pass_field(self):
        self.sl.wait_until_element_is_visible(self.REGISTER_PASS)

    def click_register_btn(self):
        logger.debug('Clicking on "registration" button.')
        self.sl.wait_and_click(self.REGISTER_BTN)

    def cust_radio(self):
        self.sl.wait_and_click(self.CUST_BTN)

    def seller_radio(self):
        self.sl.wait_and_click(self.SELL_BTN)

    def vendor_register_email(self, email):
        self.sl.wait_and_input_text(self.VENDOR_REG_EMAIL, email)

    def vendor_register_password(self, password):
        self.sl.wait_and_input_text(self.VENDOR_REG_PASS, password)

    def fill_vendor_register_form(self, fname, lname, shop_name, shop_url, phone_no):
        self.sl.wait_and_input_text(self.VENDOR_REG_FNAME, fname)
        self.sl.wait_and_input_text(self.VENDOR_REG_LNAME, lname)
        self.sl.wait_and_input_text(self.VENDOR_REG_SHOP, shop_name)
        self.sl.wait_and_input_text(self.VENDOR_RED_SHOP_URL, shop_url)
        self.sl.wait_and_input_text(self.VENDOR_REG_PHONE_NO, phone_no)

    def find_vendor_register_fields(self):
        self.sl.wait_and_get_elements(self.VENDOR_REG_FNAME)
        self.sl.wait_and_get_elements(self.VENDOR_REG_LNAME)
        self.sl.wait_and_get_elements(self.VENDOR_REG_SHOP)
        self.sl.wait_and_get_elements(self.VENDOR_RED_SHOP_URL)
        self.sl.wait_and_get_elements(self.VENDOR_REG_PHONE_NO)

    def find_login_section(self,timeout):
        self.sl.wait_and_get_elements(self.LOGIN_USER_SECTION, timeout)

    def find_registration_section(self,timeout):
        self.sl.wait_and_get_elements(self.REGISTRATION_SECTION, timeout)






