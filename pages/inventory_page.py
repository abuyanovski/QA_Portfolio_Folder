from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #                                       ==PAGE URLs==
    INVENTORY_PAGE_URL = "https://www.saucedemo.com/inventory.html"

    #                                       ==PAGE OBJECTS==
    INVENTORY_CONTAINER = (By.XPATH, "//div[@id='inventory_container']//div//div[@id='inventory_container']")
    INVENTORY_PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CART_BUTTON = (By.CSS_SELECTOR, ".shopping_cart_link")
    BURGER_MENU_BUTTON = (By.CSS_SELECTOR, ".shopping_cart_link")





