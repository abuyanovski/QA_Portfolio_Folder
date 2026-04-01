from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class InventoryPage(BasePage):

    # == PAGE URLs ==
    INVENTORY_PAGE_URL = "https://www.saucedemo.com/inventory.html"

    # == PAGE OBJECTS ==
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    INVENTORY_PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    SORT_DROPDOWN = (By.CSS_SELECTOR, ".product_sort_container")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")

    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
    ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")

    DETAILS_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_details_name")
    DETAILS_ITEM_DESC = (By.CSS_SELECTOR, ".inventory_details_desc")
    DETAILS_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_details_price")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    BACK_TO_PRODUCTS_BUTTON = (By.ID, "back-to-products")

    # == PAGE ACTIONS ==
    def get_inventory_items_count(self):
        items = self.find_elements(self.INVENTORY_ITEMS)
        return len(items)

    def is_loaded(self):
        title = self.get_text(self.INVENTORY_PAGE_TITLE)
        return title == "Products" and self.get_inventory_items_count() > 0

    def sort_by_price_low_to_high(self):
        dropdown = self.wait_for_visibility(self.SORT_DROPDOWN)
        Select(dropdown).select_by_visible_text("Price (low to high)")

    def get_displayed_product_prices(self):
        price_elements = self.find_elements(self.ITEM_PRICES)
        prices = []

        for element in price_elements:
            price_text = element.text.replace("$", "").strip()
            prices.append(float(price_text))

        return prices

    def get_first_inventory_item_data(self):
        items = self.find_elements(self.INVENTORY_ITEMS)
        first_item = items[0]

        return {
            "name": first_item.find_element(*self.ITEM_NAME).text,
            "description": first_item.find_element(*self.ITEM_DESC).text,
            "price": first_item.find_element(*self.ITEM_PRICE).text,
        }

    def click_first_product_name(self):
        items = self.find_elements(self.INVENTORY_ITEMS)
        first_item = items[0]
        first_item.find_element(*self.ITEM_NAME).click()

    def get_product_details_data(self):
        return {
            "name": self.get_text(self.DETAILS_ITEM_NAME),
            "description": self.get_text(self.DETAILS_ITEM_DESC),
            "price": self.get_text(self.DETAILS_ITEM_PRICE),
        }

    def click_back_to_products(self):
        self.click(self.BACK_TO_PRODUCTS_BUTTON)

    def add_first_item_to_cart(self):
        items = self.find_elements(self.INVENTORY_ITEMS)
        first_item = items[0]
        first_item.find_element(*self.ADD_TO_CART_BUTTON).click()

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)