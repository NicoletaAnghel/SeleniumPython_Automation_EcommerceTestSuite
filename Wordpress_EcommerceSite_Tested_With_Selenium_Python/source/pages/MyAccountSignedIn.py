from Esitetest.source.pages.locators.MyAccountSignedInLocator import MyAccountSignedInLocator
from Esitetest.source.selenium_extended import SeleniumExtended

class MyAccountSignedIn(MyAccountSignedInLocator):
        def __init__(self, driver):
            self.driver = driver
            self.sl = SeleniumExtended(self.driver)

        def verify_user_is_logged(self):
            self.sl.wait_until_element_is_visible(self.LOG_OUT_MY_ACC)

        def verity_vendor_is_logged(self, welcome):
            self.sl.wait_until_element_contains_text(self.VENDOR_WELCOME_MESSAGE, welcome)
