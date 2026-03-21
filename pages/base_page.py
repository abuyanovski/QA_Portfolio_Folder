
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from config.config import Config

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def find_elements(self, by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))

    def click(self, by_locator):
        self.find_element(by_locator).click()

    def type_into(self, by_locator, text):
        self.find_element(by_locator).send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_text(self, by_locator):
        return self.find_element(by_locator).text
