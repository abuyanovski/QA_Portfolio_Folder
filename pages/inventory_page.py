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

    # is_loaded()
    # get_inventory_items_count()


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


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
