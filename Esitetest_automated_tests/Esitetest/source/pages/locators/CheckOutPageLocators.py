
from selenium.webdriver.common.by import By

class CheckOutPAgeLocator:
    CHECKOUT_EMAIL = (By.CSS_SELECTOR, '#email')
    CHECKOUT_PASSWORD =(By.CSS_SELECTOR, '.wc-block-components-text-input #textinput-7')
    CHECKOUT_FIRSTNAME = (By.CSS_SELECTOR, '#billing-first_name')
    CHECKOUT_LASTNAME = (By.CSS_SELECTOR, '#billing-last_name')
    CHECKOUT_ADDRESS =(By.CSS_SELECTOR, '#billing-address_1')
    CHECKOUT_COUNTRY =(By.ID, 'id="billing-country"')
    CHECKOUT_CITY = (By.CSS_SELECTOR, '#billing-city')
    CHECKOUT_STATE = (By.ID, 'billing-state')
    CHECKOUT_POSTALCODE =(By.CSS_SELECTOR, '#billing-postcode')
    CHECKOUT_PHONE_NO = (By.CSS_SELECTOR, '#billing-phone')
    CHECKOUT_NOTE_CHECKBOX = (By.CSS_SELECTOR, '#order-notes #checkbox-control-1')
    CHECKOUT_ORDER_NOTE = (By.CSS_SELECTOR, '.wc-block-components-textarea')
    CHECKOUT_CREATE_ACC = (By.CSS_SELECTOR, '#contact-fields #checkbox-control-0')
    CHECKOUT_PLACE_ORDER = (By.CSS_SELECTOR, '.wc-block-checkout__actions_row .wc-block-components-button__text')
    CHECKOUT_OUT_OF_FORM = (By.CSS_SELECTOR, '.wc-block-components-sidebar-layout')
    CHECKOUT_PAYMENT_DIRECT = (By.CSS_SELECTOR, '#payment-method #radio-control-wc-payment-method-options-bacs')
    CHECKOUT_PAYMENT_CASH = (By.CSS_SELECTOR, '#payment-method #radio-control-wc-payment-method-options-cod')
    CHECKOUT_ERROR = (By.CSS_SELECTOR, '#contact .wc-block-components-text-input')
