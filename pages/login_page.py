
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    ERROR_MESSAGE = (By.ID, "errorMessage")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/login"

    def enter_username(self, username):
        self.type_into(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.type_into(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
