from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DisablePrompt:
    def __init__(self):
        chrome_options = Options()
        # Disable save address prompts
        chrome_options.add_experimental_option("prefs", {
            "profile.password_manager_enabled": False,
            "credentials_enable_service": False,
            "profile.autofill_address_enabled": False
        })

        self.driver = webdriver.Chrome(options=chrome_options)

    def get_driver(self):
        return self.driver