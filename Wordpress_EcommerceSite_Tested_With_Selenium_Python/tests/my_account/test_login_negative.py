
import pytest
from Esitetest.source.pages.MyAccountSignedOut import MyAccountSignedOut
from Esitetest.source.helpers.generate_random_email_and_username import random_username

@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        self.driver.maximize_window()
        username = random_username()
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username(username)
        my_account.input_login_password('3232ed')
        my_account.click_login_button()

        # verify error message
        expected_error = f'Error: The username {username} is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_error)

