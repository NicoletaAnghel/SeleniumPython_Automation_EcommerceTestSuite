import pytest
from Esitetest.conftest import init_driver
from Esitetest.source.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures('init_driver')
@pytest.mark.loginregistration
class TestLoginRegistrationSectionAndForms:

    @pytest.mark.tcid10_c
    def test_login_section_and_fields(self):

        my_account_out = MyAccountSignedOut(self.driver)
        my_account_out.go_to_my_account()
        # find log in section

        my_account_out.find_login_section(15)
        # find log in form fields
        my_account_out.find_login_username_field()
        my_account_out.find_login_password_field()

    @pytest.mark.tcid10_v
    def test_registration_section_and_fields(self):

        my_account_out = MyAccountSignedOut(self.driver)
        my_account_out.go_to_my_account()
        # registration section
        my_account_out.find_registration_section(15)
        # registration fields as customer
        my_account_out.cust_radio()
        my_account_out.find_register_email_field()
        my_account_out.find_register_pass_field()
        # registration fields as vendor
        my_account_out.seller_radio()
        my_account_out.find_register_email_field()
        my_account_out.find_register_pass_field()
        my_account_out.find_vendor_register_fields()
