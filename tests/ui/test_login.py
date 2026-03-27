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