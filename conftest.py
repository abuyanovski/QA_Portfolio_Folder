import pytest

from api.base_api_client import BaseApiClient
from config.config import Config
from utils.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def driver():
    browser = DriverFactory.get_driver(Config.BROWSER)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def api_client():
    client = BaseApiClient()
    yield client
    client.close_session()


@pytest.fixture(scope="function")
def setup(request, driver):
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
