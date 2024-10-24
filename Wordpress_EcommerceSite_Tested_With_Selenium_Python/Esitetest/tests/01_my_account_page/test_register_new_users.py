import pytest
from Esitetest.conftest import init_driver
from Esitetest.source.pages.MyAccountSignedOut import MyAccountSignedOut
from Esitetest.source.helpers.generate_random_email_and_username import generate_random_email_and_password
from Esitetest.source.pages.MyAccountSignedIn import MyAccountSignedIn
from Esitetest.source.helpers.fake_names_address_and_other_random_inputs import RandomInputs
from Esitetest.source.helpers.database_helpers import get_user_from_db_by_email

@pytest.mark.usefixtures('init_driver')
@pytest.mark.loginregistration
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):


        my_account_out = MyAccountSignedOut(self.driver)
        my_account_in = MyAccountSignedIn(self.driver)

        # go to my account page
        my_account_out.go_to_my_account()

        # check radio for customer
        my_account_out.cust_radio()

        # complete registration form
        email = generate_random_email_and_password()
        my_account_out.register_email(email['email'])
        password = generate_random_email_and_password()
        my_account_out.register_password(password['password'])

        # click on registration button
        my_account_out.click_register_btn()
        # verify user is logged
        my_account_in.verify_user_is_logged()

    @pytest.mark.tcid13_inv
    def test_register_invalid_user(self):
        my_account_out = MyAccountSignedOut(self.driver)

        email = 'nicoletaanghel1998@gmail.com'
        # go to my account page
        my_account_out.go_to_my_account()

        # check radio box for customer
        my_account_out.cust_radio()

        # insert existing email and pass
        my_account_out.register_email(email)
        my_account_out.register_password('1aNddedss!!')

        # click registration button
        my_account_out.click_register_btn()

        # check error is generated
        expected_error = 'Error: An account is already registered with your email address. Please log in.'
        my_account_out.wait_until_error_is_displayed(expected_error)


    @pytest.mark.tcid17
    def test_register_invalid_new_vendor(self):
        my_account_out = MyAccountSignedOut(self.driver)
        my_account_out.go_to_my_account()
        my_account_out.seller_radio()

        email = "nicoletaan@gmail.com"
        my_account_out.register_email(email)

        password = "1aNddedss!!"
        my_account_out.register_password(password)

        random_inputs = RandomInputs()
        fname, lname = random_inputs.random_names()
        shop = random_inputs.random_shop_name()
        shop_url = shop
        phone_no = random_inputs.random_phone_no()
        my_account_out.fill_vendor_register_form(fname,lname, shop, shop_url, phone_no)
        my_account_out.click_register_btn()
        expected_error = 'Error: An account is already registered with your email address. Please log in.'
        my_account_out.wait_until_error_is_displayed(expected_error)


