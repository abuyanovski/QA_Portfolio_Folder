import os
import shutil
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.config import Config


class DriverFactory:
    @staticmethod
    def _version_key(version):
        return tuple(int(part) for part in version.split("."))

    @staticmethod
    def _latest_cached_driver_path(driver_name, executable_name):
        cache_root = Path.home() / ".wdm" / "drivers" / driver_name / "win64"
        if not cache_root.exists():
            return None

        candidates = sorted(
            cache_root.glob(f"*/**/{executable_name}"),
            key=lambda candidate: DriverFactory._version_key(candidate.parents[1].name),
            reverse=True,
        )
        return str(candidates[0]) if candidates else None

    @staticmethod
    def _resolve_chrome_service():
        configured_path = os.getenv("CHROMEDRIVER_PATH")
        if configured_path and Path(configured_path).is_file():
            return ChromeService(configured_path)

        path_driver = shutil.which("chromedriver")
        if path_driver:
            return ChromeService(path_driver)

        cached_driver = DriverFactory._latest_cached_driver_path("chromedriver", "chromedriver.exe")
        if cached_driver:
            return ChromeService(cached_driver)

        return ChromeService(ChromeDriverManager().install())

    @staticmethod
    def _resolve_firefox_service():
        configured_path = os.getenv("GECKODRIVER_PATH")
        if configured_path and Path(configured_path).is_file():
            return FirefoxService(configured_path)

        path_driver = shutil.which("geckodriver")
        if path_driver:
            return FirefoxService(path_driver)

        cached_driver = DriverFactory._latest_cached_driver_path("geckodriver", "geckodriver.exe")
        if cached_driver:
            return FirefoxService(cached_driver)

        return FirefoxService(GeckoDriverManager().install())

    @staticmethod
    def get_driver(browser):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            if Config.HEADLESS:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
            service = DriverFactory._resolve_chrome_service()
            driver = webdriver.Chrome(service=service, options=options)
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            if Config.HEADLESS:
                options.add_argument('-headless')
            service = DriverFactory._resolve_firefox_service()
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise Exception(f'Browser {browser} is not supported')

        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        if Config.HEADLESS:
            driver.set_window_size(1920, 1080)
        else:
            driver.maximize_window()
        return driver
