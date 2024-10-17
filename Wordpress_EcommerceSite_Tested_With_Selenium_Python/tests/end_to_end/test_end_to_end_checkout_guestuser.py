
import pytest

from Esitetest.conftest import init_driver
from Esitetest.source.pages.CartPage import CartPage
from Esitetest.source.pages.HomePage import HomePageShop
from Esitetest.source.pages.Header import Header
from Esitetest.source.pages.CheckOutPage import CheckOutPage
import time
from Esitetest.source.configs.generic_configs import GenericConfigs
from Esitetest.source.helpers.generate_random_email_and_username import generate_random_email_and_password
from Esitetest.source.helpers.fake_names_address_and_other_random_inputs import RandomInputs
from Esitetest.source.pages.OrderReceivedPage import OrderReceivedPage
from Esitetest.source.helpers.disable_save_pass_and_autofill import DisablePrompt
from Esitetest.source.helpers.database_helpers import get_order_from_db_by_order_no


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):

        disable_prompt = DisablePrompt()
        self.driver = disable_prompt.driver
        self.driver.maximize_window()

        my_shop = HomePageShop(self.driver)
        header = Header(self.driver)
        my_cart = CartPage(self.driver)
        checkout_page = CheckOutPage(self.driver)
        order_conf_page = OrderReceivedPage(self.driver)
        # go to home page
        my_shop.go_to_shop()

        # add item to cart
        my_shop.add_items_to_cart_album()
        my_shop.add_items_to_cart_beanie()

       #  go to cart
        header.wait_until_cart_item_count(2)
        header.click_on_cart_on_left_header()
        product_names = my_cart.get_all_items_names_in_cart()
        assert len(product_names) == 2, f'Expected 2 items in cart but found{len(product_names)}'

       #  go & apply coupon
        my_cart.go_to_coupon()

        coupon_code =GenericConfigs.FREE_COUPON
        my_cart.add_coupon(coupon_code)
        my_cart.click_apply_coupon()
        expected_text =f'Coupon code "{coupon_code}" has been applied to your cart.'
        my_cart.check_apply_coupon_message(expected_text)
        my_cart.check_cart_total_amount('0,00 lei')

        # free shipping - I made it without shipping tax

        # go to check out
        my_cart.go_to_checkout(15)

        # fill billing details form
        email = generate_random_email_and_password()
        checkout_page.insert_email(email['email'])
        random_inputs = RandomInputs()
        fname, lname = random_inputs.random_names()
        address = random_inputs.random_address()
        city = random_inputs.random_city()
        postal_code = random_inputs.random_postcode()
        phone_no = random_inputs.random_phone_no()

        checkout_page.fill_biilling_address(fname,lname, address, city, postal_code, phone_no)

        # choose payment method
        checkout_page.make_cash_payment()
            # change payment method
        checkout_page.make_direct_payment()

        # proceed checkout
        checkout_page.add_note_checkbox()
        time = random_inputs.time_of_testing()
        note = f'This order was placed at {time}'
        checkout_page.add_note_text(note)

        # place order
        checkout_page.click_outside_form()
        checkout_page.place_order()

        # verify order details / is received
        order_conf_page.check_page_title('Order received', 15)

        # check order in DB (via sql or API)
        order_number = order_conf_page.get_order_number()
        print('****')
        print(order_number)
        print('****')
        db_order = get_order_from_db_by_order_no(order_number)
        assert db_order, f"After creating order with FE, not find in DB." \
                         f"Order no: {order_number}"

