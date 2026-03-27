import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
@pytest.mark.usefixtures("setup")
class TestLogin:
    pass
