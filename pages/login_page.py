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


