import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.ui
class TestCart:
    def test_add_one_item_to_cart_and_verify_badge_and_contents_TC_CART_001(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_loaded(), \
            "Inventory page did not load after login."

        expected_item = inventory_page.get_first_inventory_item_data()

        inventory_page.add_first_item_to_cart()

        assert inventory_page.get_cart_badge_count() == "1", \
            "Cart badge did not update to 1 after adding an item."

        inventory_page.open_cart()

        assert cart_page.is_loaded(), \
            "Cart page did not load."

        assert cart_page.get_cart_items_count() == 1, \
            "Cart does not contain exactly one item."

        actual_item = cart_page.get_first_cart_item_data()

        assert actual_item["name"] == expected_item["name"], \
            "Cart item name does not match selected inventory item."

        assert actual_item["description"] == expected_item["description"], \
            "Cart item description does not match selected inventory item."

        assert actual_item["price"] == expected_item["price"], \
            "Cart item price does not match selected inventory item."