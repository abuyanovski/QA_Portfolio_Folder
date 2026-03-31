import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
class TestLogin:
    def test_successful_login_TC_LOGIN_001(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory.html" in login_page.get_current_url(), \
            "User was not redirected to the inventory page."

        assert inventory_page.is_loaded(), \
            "Inventory page did not load correctly or product list is missing."

        assert not login_page.is_error_message_displayed(), \
            "Unexpected login error message was displayed."

    def test_locked_out_user_denied_access_TC_LOGIN_002(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        assert "inventory.html" not in login_page.get_current_url(), \
            "Locked out user should not be redirected to the inventory page."

        assert login_page.is_error_message_displayed(), \
            "Expected login error message was not displayed for locked out user."

        assert "locked out" in login_page.get_error_message_text().lower(), \
            "Expected locked out error message was not displayed."

        assert login_page.get_current_url() == login_page.LOGIN_PAGE_URL, \
            "Locked out user should remain on the login page."