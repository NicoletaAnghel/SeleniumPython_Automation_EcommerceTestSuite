from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else  self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else  self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else  self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else  self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def wait_and_get_elements(self, locator, timeout=None, err=None ):
        timeout = timeout if timeout else  self.default_timeout
        err = err if err else (f'unable to find elements located by"{locator}",'
                               f'after timeout of {timeout}')
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            raise TimeoutException(err)

    def wait_and_get_element(self, locator, timeout=None, err=None ):
        timeout = timeout if timeout else  self.default_timeout
        err = err if err else (f'unable to find element located by"{locator}",'
                               f'after timeout of {timeout}')
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return self.driver.find_element(*locator)
        except TimeoutException:
            raise TimeoutException(err)

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else  self.default_timeout

        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = elm.text
        return element_text

    def wait_element_to_be_visible_and_clickable(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        try:

            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

