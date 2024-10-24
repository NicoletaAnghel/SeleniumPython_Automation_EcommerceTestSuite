from symtable import Class

from selenium.webdriver.common.by import By

class CartPageLocators:

    ITEM_IN_CART =  (By.CSS_SELECTOR, 'tr.wc-block-cart-items__row .wc-block-components-product-name' )
    ACTIVATE_COUPON_FIELD = (By.CSS_SELECTOR, 'div.wc-block-components-totals-coupon')
    COUPON_FIELD = (By.ID, 'wc-block-components-totals-coupon__input-0')
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, 'button.wc-block-components-button')
    CART_PAGE_MESSAGE_COUPON = (By.CSS_SELECTOR, 'div.wc-block-components-notices__snackbar')
    CART_TOTAL = (By.CSS_SELECTOR, 'div.wc-block-components-totals-item__value')
    CHECK_OUT_BTN =(By.CSS_SELECTOR, '.wc-block-components-button__text')
    ITEM_PRICE_IN_CART = (By.CSS_SELECTOR, '.wc-block-cart-item__prices')
    CART_COUPON_ERROR =(By.CSS_SELECTOR, '.wc-block-components-panel__content .wc-block-components-validation-error')
    REMOVE_COUPON_BTN =(By.CSS_SELECTOR,'.wc-block-components-chip__remove')