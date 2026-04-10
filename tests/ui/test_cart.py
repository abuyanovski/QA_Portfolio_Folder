import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.ui
class TestCart:
    def test_add_one_item_to_cart_and_verify_badge_and_contents_TC_CART_001(self, driver, progress_step):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        progress_step("Open the login page and sign in as the standard user.")
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_loaded(), \
            "Inventory page did not load after login."

        progress_step("Capture the first inventory item details for later validation.")
        expected_item = inventory_page.get_first_inventory_item_data()

        progress_step("Add the first item to the cart and verify the badge count.")
        inventory_page.add_first_item_to_cart()

        assert inventory_page.get_cart_badge_count() == "1", \
            "Cart badge did not update to 1 after adding an item."

        progress_step("Open the cart and confirm the selected item details.")
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

    def test_remove_item_from_cart_and_verify_state_is_synchronized_TC_CART_002(self, driver, progress_step):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        progress_step("Open the login page and sign in as the standard user.")
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_loaded(), \
            "Inventory page did not load after login."

        progress_step("Capture the first inventory item details before removing it from the cart.")
        expected_item = inventory_page.get_first_inventory_item_data()

        progress_step("Add the first item to the cart and verify the badge count.")
        inventory_page.add_first_item_to_cart()

        assert inventory_page.get_cart_badge_count() == "1", \
            "Cart badge did not update to 1 after adding an item."

        progress_step("Open the cart and confirm the selected item is present before removal.")
        inventory_page.open_cart()

        assert cart_page.is_loaded(), \
            "Cart page did not load."

        assert cart_page.get_cart_items_count() == 1, \
            "Cart should contain exactly one item before removal."

        progress_step("Remove the cart item and verify the cart state is synchronized.")
        cart_page.remove_first_cart_item()

        assert cart_page.get_cart_items_count() == 0, \
            "Cart item was not removed successfully."

        assert not cart_page.is_cart_badge_displayed(), \
            "Cart badge should disappear after removing the only item."

        assert expected_item["name"] not in cart_page.get_cart_item_names(), \
            "Removed item is still displayed in the cart."

    def test_reset_app_state_clears_cart_related_state_TC_CART_003 (self, driver, progress_step):
        login_page = LoginPage (driver)
        inventory_page = InventoryPage (driver)
        cart_page = CartPage (driver)

        progress_step ("Open the login page and sign in as the standard user.")
        login_page.open ()
        login_page.login ("standard_user", "secret_sauce")

        assert inventory_page.is_loaded (), \
            "Inventory page did not load after login."

        progress_step ("Add the first item to the cart and verify the badge count.")
        inventory_page.add_first_item_to_cart ()

        assert inventory_page.get_cart_badge_count () == "1", \
            "Cart badge did not update to 1 after adding an item."

        progress_step ("Open the side menu and reset the app state.")
        inventory_page.reset_app_state ()

        assert not inventory_page.is_cart_badge_displayed (), \
            "Cart badge should be cleared after Reset App State."

        assert inventory_page.is_loaded (), \
            "Inventory page was not in a usable state after Reset App State."

        progress_step ("Open the cart and confirm it is empty after reset.")
        inventory_page.open_cart ()

        assert cart_page.is_loaded (), \
            "Cart page did not load after reset."

        assert cart_page.get_cart_items_count () == 0, \
            "Cart should be empty after Reset App State."