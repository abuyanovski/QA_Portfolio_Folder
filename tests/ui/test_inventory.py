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

    def test_product_details_page_shows_matching_item_information_TC_INV_002(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_loaded(), \
            "Inventory page did not load after login."

        expected_item = inventory_page.get_first_inventory_item_data()

        inventory_page.click_first_product_name()

        actual_item = inventory_page.get_product_details_data()

        assert actual_item["name"] == expected_item["name"], \
            "Product name on details page does not match inventory page."

        assert actual_item["description"] == expected_item["description"], \
            "Product description on details page does not match inventory page."

        assert actual_item["price"] == expected_item["price"], \
            "Product price on details page does not match inventory page."

        inventory_page.click_back_to_products()

        assert inventory_page.is_loaded(), \
            "User was not returned to the inventory page after clicking Back to products."