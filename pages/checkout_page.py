from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_TITLE = (By.CSS_SELECTOR, ".title")

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    OVERVIEW_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    OVERVIEW_ITEM_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
    OVERVIEW_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")

    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    COMPLETE_TEXT = (By.CSS_SELECTOR, ".complete-text")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def is_information_step_loaded(self):
        return self.get_text(self.CHECKOUT_TITLE) == "Checkout: Your Information"

    def is_overview_step_loaded(self):
        return self.get_text(self.CHECKOUT_TITLE) == "Checkout: Overview"

    def is_complete_step_loaded(self):
        return self.get_text(self.CHECKOUT_TITLE) == "Checkout: Complete!"

    def enter_first_name(self, first_name):
        self.type_text(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.type_text(self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code):
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def complete_checkout_information(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def get_overview_item_data(self):
        return {
            "name": self.get_text(self.OVERVIEW_ITEM_NAME),
            "description": self.get_text(self.OVERVIEW_ITEM_DESC),
            "price": self.get_text(self.OVERVIEW_ITEM_PRICE),
        }

    def get_complete_header_text(self):
        return self.get_text(self.COMPLETE_HEADER)

    def get_complete_text(self):
        return self.get_text(self.COMPLETE_TEXT)

    def is_error_message_displayed (self):
        return self.is_element_present (self.ERROR_MESSAGE)

    def get_error_message_text (self):
        return self.get_text (self.ERROR_MESSAGE)

    def get_checkout_title_text (self):
        return self.get_text (self.CHECKOUT_TITLE)