from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    #                                        ==PAGE URLs==
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"


    #                                       ==PAGE OBJECTS==
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



