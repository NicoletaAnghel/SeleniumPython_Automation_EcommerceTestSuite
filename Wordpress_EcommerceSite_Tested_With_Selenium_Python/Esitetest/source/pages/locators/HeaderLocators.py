from selenium.webdriver.common.by import By

class HeaderLocator:
    FIRST_PAGE = (By.CSS_SELECTOR, '.nav-menu > li:nth-child(1) > a:nth-child(1)')
    CART_LEFT = (By.CSS_SELECTOR, '.nav-menu li.page-item-8')
    CART_RIGHT = (By.CSS_SELECTOR, 'ul#site-header-cart')
    CHECKOUT =(By.CSS_SELECTOR,'.nav-menu li.page-item-9')
    NO_ITEMS = (By.CSS_SELECTOR, 'ul#site-header-cart span.count')