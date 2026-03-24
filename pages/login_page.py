from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #                                       ==PAGE URLs==
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"


    #                                       ==PAGE OBJECTS==
    USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")


    # INVENTORY_PAGE_ITEMS =

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


        # open()
        # enter_username()
        # enter_password()
        # click_login()
        # login()
        # is_error_message_displayed()
        #     def __init__(self, driver: WebDriver):
        #         self.driver = driver
        #         self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        #
        #     def go_to_url(self, url):
        #         self.driver.get(url)
        #
        #     def find_element(self, by_locator):
        #         return self.wait.until(EC.visibility_of_element_located(by_locator))
        #
        #     def find_elements(self, by_locator):
        #         return self.wait.until(EC.visibility_of_all_elements_located(by_locator))
        #
        #     def click(self, by_locator):
        #         self.find_element(by_locator).click()
        #
        #     def type_into(self, by_locator, text):
        #         self.find_element(by_locator).send_keys(text)
        #
        #     def get_title(self):
        #         return self.driver.title
        #
        #     def get_text(self, by_locator):
        #         return self.find_element(by_locator).text
