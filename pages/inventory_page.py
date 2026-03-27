from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    #                                         ==PAGE URLs==
    INVENTORY_PAGE_URL = "https://www.saucedemo.com/inventory.html"

    #                                       ==PAGE OBJECTS==
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    INVENTORY_PAGE_TITLE = (By.CSS_SELECTOR, ".title")

    def get_inventory_items_count(self):
        items = self.find_elements(self.INVENTORY_ITEMS)
        return len(items)

    def is_loaded(self):
        title = self.get_text(self.INVENTORY_PAGE_TITLE)
        return title == "Products" and self.get_inventory_items_count() > 0





