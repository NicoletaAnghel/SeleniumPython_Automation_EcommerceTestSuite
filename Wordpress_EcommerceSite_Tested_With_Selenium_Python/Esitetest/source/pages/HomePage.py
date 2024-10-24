from Esitetest.source.pages.locators.HomePageLocators import HomePageLocators
from Esitetest.source.selenium_extended import SeleniumExtended
from Esitetest.source.helpers.config_helpers import get_base_url
import logging as logger


class HomePageShop(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_shop(self):

        base_url = get_base_url()
        shop_url = base_url
        logger.info(f'Going to:  {shop_url}')
        self.driver.get(shop_url)

    def add_items_to_cart_album(self):
        self.sl.wait_and_click(self.ITEM1_ALBUM)

    def add_items_to_cart_beanie(self):
        self.sl.wait_and_click(self.ITEM2_BEANIE)

    def add_items_to_cart_beanie_with_logo(self):
        self.sl.wait_and_click(self.ITEM_BEANIE_WITH_LOGO)

    def add_items_to_cart_hoodie_with_logo(self):
        self.sl.wait_and_click(self.ITEM_HOODIE_WITH_LOGO)


