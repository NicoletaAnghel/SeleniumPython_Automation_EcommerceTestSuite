from selenium.webdriver.common.by import By

class MyAccountSignedInLocator:
    LOG_OUT_MY_ACC = (By.LINK_TEXT, 'Log out')
    VENDOR_WELCOME_MESSAGE = (By.CSS_SELECTOR, '.wc-setup-content')
    VENDOR_DASH_PAGE_TITLE = (By.CSS_SELECTOR, '.entry-header .entry-title')