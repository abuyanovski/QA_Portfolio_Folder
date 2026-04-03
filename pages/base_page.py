from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from config.config import Config


#                                           == COMMON PAGE ACTIONS ==
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    #                                          == WAIT ACTIONS ==
    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_invisibility(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
            )

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def type_text(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_for_visibility(locator)
        return element.text

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_to_element(self, locator):
        element = self.wait_for_visibility(locator)
        ActionChains(self.driver).move_to_element(element).perform()


