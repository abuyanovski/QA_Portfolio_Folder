from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#                                           ==COMMON PAGE ACTIONS ==
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
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



    #
    # click()
    # type_text()
    # wait_for_visibility()
    # wait_for_clickable()
    # is_element_present()
    # get_current_url()






