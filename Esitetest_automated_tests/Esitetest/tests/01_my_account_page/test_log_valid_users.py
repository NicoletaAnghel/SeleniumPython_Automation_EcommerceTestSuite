
import pytest
from Esitetest.conftest import init_driver
from Esitetest.source.pages.MyAccountSignedOut import MyAccountSignedOut
from Esitetest.source.pages.MyAccountSignedIn import MyAccountSignedIn

@pytest.mark.usefixtures('init_driver')
@pytest.mark.loginregistration
class TestLoginPositiveFlow:

    @pytest.mark.tcid11_c
    def test_login_valid_user_customer(self):

        my_account_out = MyAccountSignedOut(self.driver)
        my_account_in = MyAccountSignedIn(self.driver)
        my_account_out.go_to_my_account()
        my_account_out.input_login_username('nicoletaanghel1998')
        my_account_out.input_login_password('1aNddedss!!')
        my_account_out.click_login_button()
        my_account_in.verify_user_is_logged()

    @pytest.mark.tcid11_v
    def test_login_valid_user_vendor(self):

        my_account_out = MyAccountSignedOut(self.driver)
        my_account_in = MyAccountSignedIn(self.driver)
        my_account_out.go_to_my_account()
        my_account_out.input_login_username('nicoletaan')
        my_account_out.input_login_password('1aNddedss!!')
        my_account_out.click_login_button()
        my_account_in.verify_vendor_is_logged('Dash')