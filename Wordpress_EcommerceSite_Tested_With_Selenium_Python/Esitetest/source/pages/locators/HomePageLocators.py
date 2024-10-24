from selenium.webdriver.common.by import By

class HomePageLocators:
    ITEM1_ALBUM = (By.CSS_SELECTOR, 'li.product.type-product.post-32 a.button')
    ITEM2_BEANIE = (By.CSS_SELECTOR, 'li.product.type-product.post-24 a.button')
    GO_TO_CART = (By.CSS_SELECTOR, 'li.current-menu-item')
    ITEM_BEANIE_WITH_LOGO =(By.CSS_SELECTOR, 'li.product.type-product.post-41 a.button')
    ITEM_HOODIE_WITH_LOGO= (By.CSS_SELECTOR, 'li.product.type-product.post-22 a.button')