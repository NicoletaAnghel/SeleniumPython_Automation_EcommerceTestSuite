from fileinput import close

import pytest
from pytest_selenium import driver

from Esitetest.conftest import init_driver
from Esitetest.source.pages.CartPage import CartPage
from Esitetest.source.pages.HomePage import HomePageShop
from Esitetest.source.pages.Header import Header
from Esitetest.source.pages.CheckOutPage import CheckOutPage
from Esitetest.source.configs.generic_configs import GenericConfigs
from Esitetest.source.pages.OrderReceivedPage import OrderReceivedPage



@pytest.mark.usefixtures('init_driver')
@pytest.mark.tccartpage
class TestCartPageContent:

    @pytest.mark.tcid44
    def test_50_discount_applied_correctly(self):

        my_shop = HomePageShop(self.driver)
        header = Header(self.driver)
        my_cart = CartPage(self.driver)
        checkout_page = CheckOutPage(self.driver)
        order_conf_page = OrderReceivedPage(self.driver)
        my_shop.go_to_shop()
        my_shop.add_items_to_cart_album()
        header.wait_until_cart_1item_count(1, 30)
        header.click_on_cart_on_left_header()
        my_cart.go_to_coupon()
        coupon_code =GenericConfigs.COUPON_50
        my_cart.add_coupon(coupon_code)
        my_cart.click_apply_coupon()
        expected_text =f'Coupon code "{coupon_code}" has been applied to your cart.'
        my_cart.check_apply_coupon_message(expected_text)
        item_price_text = my_cart.item_price_in_cart()
        item_price = float(item_price_text.replace(' lei', '').replace(',', '.').strip())
        discounted_price = item_price * 0.50
        discounted_price_str = f"{discounted_price:.2f}".replace('.', ',') + " lei"
        my_cart.check_cart_total_amount_discounted(discounted_price_str, 30)
        my_cart.remove_coupon_applied_on_cart()


    @pytest.mark.tcid45
    def test_non_existing_coupon_code(self):
        my_shop = HomePageShop(self.driver)
        header = Header(self.driver)
        my_cart = CartPage(self.driver)
        my_shop.go_to_shop()
        my_shop.add_items_to_cart_album()
        header.wait_until_cart_1item_count(1, 30)
        header.click_on_cart_on_left_header()
        my_cart.go_to_coupon()
        coupon_code_wrong = 'esite'
        my_cart.add_coupon(coupon_code_wrong)
        my_cart.click_apply_coupon()
        expected_text =f'Coupon "{coupon_code_wrong}" does not exist!'
        my_cart.check_error_message_for_coupon_(expected_text,30)


    @pytest.mark.tcid46
    def test_verify_success_coupon_applied_message(self):
        my_shop = HomePageShop(self.driver)
        header = Header(self.driver)
        my_cart = CartPage(self.driver)
        my_shop.go_to_shop()
        my_shop.add_items_to_cart_album()
        header.wait_until_cart_1item_count(1, 30)
        header.click_on_cart_on_left_header()
        my_cart.go_to_coupon()
        coupon_code =GenericConfigs.FREE_COUPON
        my_cart.add_coupon(coupon_code)
        my_cart.click_apply_coupon()
        expected_text =f'Coupon code "{coupon_code}" has been applied to your cart.'
        my_cart.check_apply_coupon_message(expected_text)
        my_cart.remove_coupon_applied_on_cart()

    @pytest.mark.tcid47
    def test_remove_applied_coupon(self):
        my_shop = HomePageShop(self.driver)
        header = Header(self.driver)
        my_cart = CartPage(self.driver)
        my_shop.go_to_shop()
        my_shop.add_items_to_cart_hoodie_with_logo()
        header.wait_until_cart_1item_count(1, 30)
        header.click_on_cart_on_left_header()
        my_cart.go_to_coupon()
        coupon_code =GenericConfigs.COUPON_25
        my_cart.add_coupon(coupon_code)
        my_cart.click_apply_coupon()
        expected_text =f'Coupon code "{coupon_code}" has been applied to your cart.'
        my_cart.check_apply_coupon_message(expected_text)
        my_cart.remove_coupon_applied_on_cart()
