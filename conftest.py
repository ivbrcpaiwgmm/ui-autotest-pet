from enum import Enum

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Driver(Enum):
    CHROME = "Google Chrome"
    EDGE = "Microsoft Edge"
    FIREFOX = "Mozilla Firefox"


SUPPORTED_BROWSERS = [Driver.CHROME, Driver.FIREFOX]


@pytest.fixture(params=SUPPORTED_BROWSERS)
def driver(request):
    match request.param:
        case Driver.CHROME:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        case Driver.EDGE:
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        case Driver.FIREFOX:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        case _:
            raise ValueError(f"Unsupported browser: {request.param.value}")

    yield driver
    driver.quit()
