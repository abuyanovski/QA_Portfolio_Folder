import pytest
from utils.driver_factory import DriverFactory
from config.config import Config


@pytest.fixture(scope="function")
def driver():
    browser = DriverFactory.get_driver(Config.BROWSER)
    yield browser
    browser.quit()