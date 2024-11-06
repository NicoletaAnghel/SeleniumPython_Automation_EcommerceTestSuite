
import pytest

from Esitetest.conftest import init_driver
from Esitetest.source.pages.CartPage import CartPage
from Esitetest.source.pages.HomePage import HomePageShop
from Esitetest.source.pages.Header import Header
from Esitetest.source.pages.CheckOutPage import CheckOutPage

from Esitetest.source.configs.generic_configs import GenericConfigs
from Esitetest.source.helpers.fake_names_address_and_other_random_inputs import RandomInputs


@pytest.mark.usefixtures('init_driver')
@pytest.mark.endtoend
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid29
    def test_end_to_end_checkout_guest_user_no_email(self):

        my_shop = HomePageShop(self.driver)
        header = Header(self.driver)
        my_cart = CartPage(self.driver)
        checkout_page = CheckOutPage(self.driver)
        my_shop.go_to_shop()
        my_shop.add_items_to_cart_beanie_with_logo()
        my_shop.add_items_to_cart_hoodie_with_logo()
        header.wait_until_cart_item_count(2, 20)
        header.click_on_cart_on_left_header()
        product_names = my_cart.get_all_items_names_in_cart()
        assert len(product_names) == 2, f'Expected 2 items in cart but found{len(product_names)}'
        my_cart.go_to_coupon()
        coupon_code =GenericConfigs.FREE_COUPON
        my_cart.add_coupon(coupon_code)
        my_cart.click_apply_coupon()
        expected_text =f'Coupon code "{coupon_code}" has been applied to your cart.'
        my_cart.check_apply_coupon_message(expected_text)
        my_cart.check_cart_total_amount('0,00 lei')
        my_cart.go_to_checkout(20)
        random_inputs = RandomInputs()
        fname, lname = random_inputs.random_names()
        address = random_inputs.random_address()
        city = random_inputs.random_city()
        postal_code = random_inputs.random_postcode()
        phone_no = random_inputs.random_phone_no()
        checkout_page.fill_biilling_address(fname,lname, address, city, postal_code, phone_no)
        checkout_page.make_cash_payment()
        checkout_page.make_direct_payment()
        checkout_page.add_note_checkbox()
        time = random_inputs.time_of_testing()
        note = f'This order was placed at {time}'
        checkout_page.add_note_text(note)
        checkout_page.click_outside_form()
        checkout_page.place_order(40)
        expected_error ='Please enter a valid email address'
        checkout_page.error_for_not_providing_email_as_guest(expected_error)


