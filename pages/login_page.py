from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # == PAGE URL ==
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"

    # == PAGE OBJECTS ==
    USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")

    def open(self):
        self.open_url(self.LOGIN_PAGE_URL)

    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_error_message_displayed(self):
        return self.is_element_present(self.ERROR_MESSAGE)

    def get_error_message_text(self):
        return self.get_text(self.ERROR_MESSAGE)