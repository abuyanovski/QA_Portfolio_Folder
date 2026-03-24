from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#                                           ==COMMON PAGE ACTIONS ==
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    def wait_for_clickable(self, locator):
            return self.wait.until(
                EC.element_to_be_clickable(locator)
            )

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def type_text(self, locator):
            element = self.wait_for_visibility(locator)
            element.clear()
            element.send_keys(locator)



    #
    # click()
    # type_text()
    # wait_for_visibility()
    # wait_for_clickable()
    # is_element_present()
    # get_current_url()







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
