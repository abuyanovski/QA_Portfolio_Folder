import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
class TestInventory:
    def test_products_can_be_sorted_by_price_low_to_high_TC_INV_001(self, driver, progress_step):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        progress_step("Open the login page and sign in as the standard user.")
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_loaded(), \
            "Inventory page did not load after login."

        progress_step("Capture the current inventory count before sorting.")
        item_count_before = inventory_page.get_inventory_items_count()

        progress_step("Sort the inventory by price from low to high.")
        inventory_page.sort_by_price_low_to_high()

        prices = inventory_page.get_displayed_product_prices()
        item_count_after = inventory_page.get_inventory_items_count()

        progress_step("Verify the prices are sorted and the item count is unchanged.")
        assert prices == sorted(prices), \
            f"Products are not sorted in ascending price order. Actual order: {prices}"

        assert item_count_after == item_count_before, \
            "Product count changed after sorting."

        assert item_count_after > 0, \
            "No products are displayed after sorting."

    def test_product_details_page_shows_matching_item_information_TC_INV_002(self, driver, progress_step):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        progress_step("Open the login page and sign in as the standard user.")
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_loaded(), \
            "Inventory page did not load after login."

        progress_step("Capture the first inventory item details.")
        expected_item = inventory_page.get_first_inventory_item_data()

        progress_step("Open the first product details page.")
        inventory_page.click_first_product_name()

        actual_item = inventory_page.get_product_details_data()

        progress_step("Verify the product details match and navigate back to inventory.")
        assert actual_item["name"] == expected_item["name"], \
            "Product name on details page does not match inventory page."

        assert actual_item["description"] == expected_item["description"], \
            "Product description on details page does not match inventory page."

        assert actual_item["price"] == expected_item["price"], \
            "Product price on details page does not match inventory page."

        inventory_page.click_back_to_products()

        assert inventory_page.is_loaded(), \
            "User was not returned to the inventory page after clicking Back to products."
