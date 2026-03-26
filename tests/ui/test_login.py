
import pytest
from pages.login_page import LoginPage
from config.config import Config

@pytest.mark.usefixtures("setup")
class TestLogin:
    # def test_successful_login(self):
    #     self.driver.get(Config.BASE_URL + "/login")
    #     login_page = LoginPage(self.driver)
    #     login_page.login("testuser", "testpassword")
    #     # Assert successful login (e.g., check for a welcome message or URL change)
    #     assert "dashboard" in self.driver.current_url
    #
    # def test_invalid_login(self):
    #     self.driver.get(Config.BASE_URL + "/login")
    #     login_page = LoginPage(self.driver)
    #     login_page.login("invaliduser", "invalidpassword")
    #     error_message = login_page.get_error_message()
    #     assert "Invalid credentials" in error_message

        # open_the_page()
        # enter_username()
        # enter_password()
        # click_login()
        # login()
        # is_inventory_page_loaded()
        # is_error_message_displayed()

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
