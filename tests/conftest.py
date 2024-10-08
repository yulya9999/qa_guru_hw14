import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from zoolandia_project_tests.utils import attach

DEFAULT_BROWSER_VERSION = '100.0'
BASE_URL = "https://xn----7sbbogiefyveeau2v.xn--p1ai"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        default="100.0"
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def setup_browser(request):
    browser.config.base_url = "https://xn----7sbbogiefyveeau2v.xn--p1ai"
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    browser_version = request.config.getoption("--browser_version")
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {"enableVideo": True, "enableVNC": True}
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@selenoid.autotests.cloud/wd/hub",
        options=options,
    )
    browser.config.driver = driver

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
