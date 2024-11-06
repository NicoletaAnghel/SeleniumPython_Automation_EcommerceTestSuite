
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChService
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
import os
import pytest_html
import allure


@pytest.fixture(scope='class')
def init_driver(request):
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception('The environment variable "BROWSER" must be set.')

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f'Provided browser "{browser}" is not one of the supported. '
                        f'Supported are: {supported_browsers}')

    driver = None  # Initialize driver to None

    if browser in ('chrome', 'ch'):
        chrome_options = ChOptions()
        driver = webdriver.Chrome()
        chrome_prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        chrome_options.add_experimental_option("prefs", chrome_prefs)

    elif browser in ('firefox', 'ff'):
        firefox_options = FFOptions()
        firefox_profile = webdriver.FirefoxProfile()
        driver = webdriver.Firefox()
        firefox_profile.set_preference("dom.webnotifications.enabled", False)
        firefox_profile.set_preference("signon.rememberSignons", False)

    elif browser in ('headlesschrome'):
        chrome_options= ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service = ChService(), options = chrome_options)

    elif browser in ('headlessfirefox'):
        firefox_options= FFOptions()
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('no-sandbox')
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(service = FFService(), options = firefox_options)

    if driver is not None:
        driver.maximize_window()

    request.cls.driver = driver
    yield driver

    driver.quit()

### FOR GENERATING ALLURE REPORTS
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report

        xfail = hasattr(report, "wasxfail")
        # check if test failed
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False

            if is_frontend_test:
                results_dir = os.environ.get("RESULTS_DIR", r"C:\Users\nicol\PycharmProjects\Esitetest\Esitetest\reports")
                if not results_dir:
                    raise Exception("Environment variable 'RESULTS_DIR' must be set.")

                screen_shot_path = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs['request']
                allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
                              name='screenshot',
                              attachment_type=allure.attachment_type.PNG)


# ### FOR GENERATING ONLY PYTEST-HTML REPORT
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call":
#         # always add url to report
#
#         xfail = hasattr(report, "wasxfail")
#         # check if test failed
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             is_frontend_test = True if 'init_driver' in item.fixturenames else False
#
#             if is_frontend_test:
#                 results_dir = os.environ.get("RESULTS_DIR", r"C:\Users\nicol\PycharmProjects\Esitetest\Esitetest\reports")
#                 if not results_dir:
#                     raise Exception("Environment variable 'RESULTS_DIR' must be set.")
#
#                 screen_shot_path = os.path.join(results_dir, item.name + '.png')
#                 driver_fixture = item.funcargs['request']
#                 driver_fixture.cls.driver.save_screenshot(screen_shot_path)
#                 # only add additional html on failure
#                 # extras.append(pytest_html.extras.html('<div style ="background: orange;">Additional HTML</div>'))
#                 extras.append(pytest_html.extras.image(screen_shot_path))
#         report.extras = extras



