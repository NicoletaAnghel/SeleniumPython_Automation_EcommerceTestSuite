from Esitetest.source.selenium_extended import SeleniumExtended
from Esitetest.source.pages.locators.HeaderLocators import HeaderLocator


class Header(HeaderLocator):

    def __init__(self, driver):

        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_on_cart_on_left_header(self):
        self.sl.wait_and_click(self.CART_RIGHT)

    def wait_until_cart_item_count(self, count):
        expected_text = str(count) + ' items'
        self.sl.wait_until_element_contains_text(self.NO_ITEMS, expected_text)


