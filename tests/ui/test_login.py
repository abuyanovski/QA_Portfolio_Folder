
import pytest
from pages.login_page import LoginPage
from config.config import Config

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_successful_login(self):
        self.driver.get(Config.BASE_URL + "/login")
        login_page = LoginPage(self.driver)
        login_page.login("testuser", "testpassword")
        # Assert successful login (e.g., check for a welcome message or URL change)
        assert "dashboard" in self.driver.current_url

    def test_invalid_login(self):
        self.driver.get(Config.BASE_URL + "/login")
        login_page = LoginPage(self.driver)
        login_page.login("invaliduser", "invalidpassword")
        error_message = login_page.get_error_message()
        assert "Invalid credentials" in error_message
