
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.config import Config

class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            if Config.HEADLESS:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            if Config.HEADLESS:
                options.add_argument('-headless')
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise Exception(f'Browser {browser} is not supported')

        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.maximize_window()
        return driver
