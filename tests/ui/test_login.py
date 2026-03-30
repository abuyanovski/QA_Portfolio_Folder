import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
class TestLogin:
    def test_successful_login_TC_LOGIN_001(self, driver):
        LOGIN_PAGE_URL = LoginPage(driver)
        INVENTORY_PAGE_URL = InventoryPage(driver)

        LOGIN_PAGE_URL.open()
        LOGIN_PAGE_URL.login("standard_user", "secret_sauce")

        assert "inventory.html" in LOGIN_PAGE_URL.get_current_url(), \
            "User was not redirected to the inventory page."

        assert INVENTORY_PAGE_URL.is_loaded(), \
            "Inventory page did not load correctly or product list is missing."

        assert not LOGIN_PAGE_URL.is_error_message_displayed(), \
            "Unexpected login error message was displayed."
