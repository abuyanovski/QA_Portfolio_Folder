import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
class TestInventory:
    def test_products_can_be_sorted_by_price_low_to_high_TC_INV_001(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_loaded(), \
            "Inventory page did not load after login."

        item_count_before = inventory_page.get_inventory_items_count()

        inventory_page.sort_by_price_low_to_high()

        prices = inventory_page.get_displayed_product_prices()
        item_count_after = inventory_page.get_inventory_items_count()

        assert prices == sorted(prices), \
            f"Products are not sorted in ascending price order. Actual order: {prices}"

        assert item_count_after == item_count_before, \
            "Product count changed after sorting."

        assert item_count_after > 0, \
            "No products are displayed after sorting."