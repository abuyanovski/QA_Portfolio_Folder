from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    CART_ITEM_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
    CART_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    CART_PAGE_TITLE = (By.CSS_SELECTOR, ".title")

    def is_loaded(self):
        title = self.get_text(self.CART_PAGE_TITLE)
        return title == "Your Cart"

    def get_cart_items_count(self):
        items = self.find_elements(self.CART_ITEMS)
        return len(items)

    def get_first_cart_item_data(self):
        items = self.find_elements(self.CART_ITEMS)
        first_item = items[0]

        return {
            "name": first_item.find_element(*self.CART_ITEM_NAME).text,
            "description": first_item.find_element(*self.CART_ITEM_DESC).text,
            "price": first_item.find_element(*self.CART_ITEM_PRICE).text,
        }