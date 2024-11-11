from Esitetest.source.pages.locators.MyAccountSignedInLocator import MyAccountSignedInLocator
from Esitetest.source.selenium_extended import SeleniumExtended

class MyAccountSignedIn(MyAccountSignedInLocator):
        
        endpoint = '/my-account/'
        def __init__(self, driver):
            self.driver = driver
            self.sl = SeleniumExtended(self.driver)

        def verify_user_is_logged(self):
            self.sl.wait_until_element_is_visible(self.LOG_OUT_MY_ACC)

        def verify_vendor_account_is_created(self, welcome):
            self.sl.wait_until_element_contains_text(self.VENDOR_WELCOME_MESSAGE, welcome)

        def verify_vendor_is_logged(self, welcome):
            self.sl.wait_until_element_contains_text(self.VENDOR_DASH_PAGE_TITLE, welcome)

