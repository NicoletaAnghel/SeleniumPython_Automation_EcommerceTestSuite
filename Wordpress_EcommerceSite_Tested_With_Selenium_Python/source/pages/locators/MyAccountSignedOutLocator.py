from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:

    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_USER_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.woocommerce-form button.woocommerce-form-login__submit')

    ERRORS_UL =(By.CSS_SELECTOR, 'ul.woocommerce-error')

    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASS = (By.ID, 'reg_password')
    REGISTER_BTN = (By.NAME, 'register')
    CUST_BTN = (By.CSS_SELECTOR, '.dokan-role-customer' )
    SELL_BTN = (By.CSS_SELECTOR, '.dokan-role-seller')
    LOG_OUT_MY_ACC = (By.LINK_TEXT, 'Log out')
    VENDOR_REG_EMAIL = (By.ID, 'reg_email')
    VENDOR_REG_PASS = (By.ID, 'reg_password')
    VENDOR_REG_FNAME= (By.ID, 'first-name')
    VENDOR_REG_LNAME = (By.ID, 'last-name')
    VENDOR_REG_SHOP = (By.ID, 'company-name')
    VENDOR_RED_SHOP_URL = (By.ID, 'seller-url')
    VENDOR_REG_PHONE_NO= (By.ID, 'shop-phone')