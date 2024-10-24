import time

import pytest
from Esitetest.source.pages.MyAccountSignedOut import MyAccountSignedOut
from Esitetest.source.helpers.generate_random_email_and_username import random_username

@pytest.mark.usefixtures("init_driver")
@pytest.mark.loginregistration
class TestLoginNegative:

    @pytest.mark.tcid12_c
    def test_login_none_existing_customer_user(self):

        username = random_username()
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username(username)
        my_account.input_login_password('3232ed')
        my_account.click_login_button()

        expected_error = f'Error: The username {username} is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_error)

    @pytest.mark.tcid12_v
    def test_login_valid_user_vendor(self):

        my_account_out = MyAccountSignedOut(self.driver)
        username_v = random_username()
        my_account_out.go_to_my_account()
        my_account_out.input_login_username(username_v)
        my_account_out.input_login_password('1aNddedss!')
        my_account_out.click_login_button()

        expected_error = f'Error: The username {username_v} is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account_out.wait_until_error_is_displayed(expected_error)


    @pytest.mark.tcid15_c
    def test_login_valid_customer_user_wrong_pass(self):

        my_account_out = MyAccountSignedOut(self.driver)
        my_account_out.go_to_my_account()
        username ='nicoletaanghel1998'
        my_account_out.input_login_username(username)
        my_account_out.input_login_password('1aNddedss')
        my_account_out.click_login_button()

        expected_error = f'Error: The password you entered for the username {username} is incorrect. Lost your password?'
        my_account_out.wait_until_error_is_displayed(expected_error)

    @pytest.mark.tcid15_v
    def test_login_valid_vendor_user_wrong_pass(self):

        my_account_out = MyAccountSignedOut(self.driver)
        my_account_out.go_to_my_account()
        username ='nicoletaan'
        my_account_out.input_login_username(username)
        my_account_out.input_login_password('1aNddedss')
        my_account_out.click_login_button()

        expected_error = f'Error: The password you entered for the username {username} is incorrect. Lost your password?'
        my_account_out.wait_until_error_is_displayed(expected_error)

    @pytest.mark.tcid16_c
    def test_login_none_existing_customer_user(self):

        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        username = 'nicoletaanghel98'
        my_account.input_login_username(username)
        my_account.input_login_password('3232ed')
        my_account.click_login_button()

        expected_error = f'Error: The username {username} is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_error)

    @pytest.mark.tcid16_v
    def test_login_valid_user_vendor(self):

        my_account_out = MyAccountSignedOut(self.driver)
        username_v = 'annicoleta'
        my_account_out.go_to_my_account()
        my_account_out.input_login_username(username_v)
        my_account_out.input_login_password('1aNddedss!')
        my_account_out.click_login_button()

        expected_error = f'Error: The username {username_v} is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account_out.wait_until_error_is_displayed(expected_error)

