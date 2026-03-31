from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class InventoryPage(BasePage):

    #                                         ==PAGE URLs==
    INVENTORY_PAGE_URL = "https://www.saucedemo.com/inventory.html"

    #                                       ==PAGE OBJECTS==
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    INVENTORY_PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    SORT_DROPDOWN = (By.CSS_SELECTOR, ".product_sort_container")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")

    #                                       ==PAGE ACTIONS==
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




