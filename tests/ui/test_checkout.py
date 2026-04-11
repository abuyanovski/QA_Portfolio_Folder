import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.ui
class TestCheckout:
    def test_successful_checkout_with_valid_customer_information_TC_CHECKOUT_001(self, driver, progress_step):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        progress_step("Open the login page and sign in as the standard user.")
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_loaded(), \
            "Inventory page did not load after login."

        progress_step("Capture the first inventory item details for later validation.")
        expected_item = inventory_page.get_first_inventory_item_data()

        progress_step("Add the first item to the cart and open the cart page.")
        inventory_page.add_first_item_to_cart()
        inventory_page.open_cart()

        assert cart_page.is_loaded(), \
            "Cart page did not load."

        assert cart_page.get_cart_items_count() == 1, \
            "Cart should contain exactly one item before checkout."

        progress_step("Click Checkout and confirm checkout information step loads.")
        cart_page.click_checkout()

        assert checkout_page.is_information_step_loaded(), \
            "Checkout information step did not load."

        progress_step("Enter valid customer information and continue to overview.")
        checkout_page.complete_checkout_information(
            first_name="Anton",
            last_name="Buyer",
            postal_code="98042"
        )

        assert checkout_page.is_overview_step_loaded(), \
            "Checkout overview step did not load after entering valid information."

        progress_step("Verify overview item matches the selected inventory item.")
        overview_item = checkout_page.get_overview_item_data()

        assert overview_item["name"] == expected_item["name"], \
            "Checkout overview item name does not match selected inventory item."

        assert overview_item["description"] == expected_item["description"], \
            "Checkout overview item description does not match selected inventory item."

        assert overview_item["price"] == expected_item["price"], \
            "Checkout overview item price does not match selected inventory item."

        progress_step("Finish checkout and verify confirmation page is displayed.")
        checkout_page.click_finish()

        assert checkout_page.is_complete_step_loaded(), \
            "Checkout completion page did not load."

        assert "thank you" in checkout_page.get_complete_header_text().lower(), \
            "Expected checkout success header was not displayed."

        assert checkout_page.get_complete_text(), \
            "Expected checkout confirmation text was not displayed."

    def test_checkout_blocks_progress_when_first_name_is_blank_TC_CHECKOUT_002 (self, driver, progress_step):
        login_page = LoginPage (driver)
        inventory_page = InventoryPage (driver)
        cart_page = CartPage (driver)
        checkout_page = CheckoutPage (driver)

        progress_step ("Open the login page and sign in as the standard user.")
        login_page.open ()
        login_page.login ("standard_user", "secret_sauce")

        assert inventory_page.is_loaded (), \
            "Inventory page did not load after login."

        progress_step ("Add the first item to the cart and open the cart page.")
        inventory_page.add_first_item_to_cart ()
        inventory_page.open_cart ()

        assert cart_page.is_loaded (), \
            "Cart page did not load."

        assert cart_page.get_cart_items_count () == 1, \
            "Cart should contain exactly one item before checkout."

        progress_step ("Click Checkout and confirm checkout information step loads.")
        cart_page.click_checkout ()

        assert checkout_page.is_information_step_loaded (), \
            "Checkout information step did not load."

        progress_step ("Leave first name blank, enter valid last name and postal code, then click Continue.")
        checkout_page.enter_last_name ("Buyer")
        checkout_page.enter_postal_code ("98042")
        checkout_page.click_continue ()

        assert checkout_page.is_information_step_loaded (), \
            "User should remain on checkout information step when first name is blank."

        assert checkout_page.is_error_message_displayed (), \
            "Expected validation error message was not displayed when first name was blank."

        assert "first name is required" in checkout_page.get_error_message_text ().lower (), \
            "Expected first-name validation error message was not displayed."

    def test_error_user_checkout_completion_behavior_TC_CHECKOUT_003 (self, driver, progress_step):
        login_page = LoginPage (driver)
        inventory_page = InventoryPage (driver)
        cart_page = CartPage (driver)
        checkout_page = CheckoutPage (driver)

        progress_step ("Open the login page and sign in as error_user.")
        login_page.open ()
        login_page.login ("error_user", "secret_sauce")

        assert inventory_page.is_loaded (), \
            "Inventory page did not load after login for error_user."

        progress_step ("Add the first item to the cart and open the cart page.")
        inventory_page.add_first_item_to_cart ()
        inventory_page.open_cart ()

        assert cart_page.is_loaded (), \
            "Cart page did not load for error_user."

        assert cart_page.get_cart_items_count () == 1, \
            "Cart should contain exactly one item before checkout for error_user."

        progress_step ("Click Checkout and confirm checkout information step loads.")
        cart_page.click_checkout ()

        assert checkout_page.is_information_step_loaded (), \
            "Checkout information step did not load for error_user."

        progress_step ("Enter valid customer information and continue to overview.")
        checkout_page.complete_checkout_information (
            first_name="Anton",
            last_name="Buyer",
            postal_code="98042"
        )

        assert checkout_page.is_overview_step_loaded (), \
            "Checkout overview step did not load for error_user."

        progress_step ("Click Finish and observe the resulting system behavior.")
        checkout_page.click_finish ()

        current_url = checkout_page.get_current_url ()
        current_title = checkout_page.get_checkout_title_text ()

        if checkout_page.is_complete_step_loaded ():
            assert "thank you" in checkout_page.get_complete_header_text ().lower (), \
                "Checkout completed for error_user, but expected success header was not displayed."

            assert checkout_page.get_complete_text (), \
                "Checkout completed for error_user, but confirmation text was missing."

        else:
            error_text = ""
            if checkout_page.is_error_message_displayed ():
                error_text = checkout_page.get_error_message_text ()

            assert (
                    checkout_page.is_overview_step_loaded ()
                    or checkout_page.is_information_step_loaded ()
                    or bool (error_text)
            ), (
                f"Observed unexpected post-finish state for error_user. "
                f"URL: {current_url}, Title: {current_title}, Error: {error_text or 'None'}"
            )

            pytest.xfail (
                f"Observed abnormal checkout behavior for error_user. "
                f"URL: {current_url}, Title: {current_title}, Error: {error_text or 'None'}"
            )