import pytest
from utils.driver_factory import DriverFactory
from config.config import Config

@pytest.fixture(scope="function")
def setup(request):
    driver = DriverFactory.get_driver(Config.BROWSER)
    request.cls.driver = driver
    yield driver
    driver.quit()