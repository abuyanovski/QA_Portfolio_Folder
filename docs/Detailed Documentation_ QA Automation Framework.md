# Detailed Documentation: QA Automation Framework

## 1. Introduction
This document provides an in-depth explanation of the Python and Selenium-based test automation framework. It is intended for QA Analysts, Automation Engineers, and Developers who will be contributing to or maintaining the test suite. The goal is to ensure a clear understanding of the framework's architecture, implementation details, and best practices for effective test automation.

## 2. Architecture Overview

### 2.1 Page Object Model (POM)
The **Page Object Model (POM)** is a design pattern in test automation that creates an object repository for UI elements within web pages. Instead of embedding UI element locators and actions directly within test scripts, POM encapsulates them into separate classes, known as "Page Objects." [1]

**Benefits of POM:**
*   **Maintainability:** When the UI changes, only the Page Object needs to be updated, not every test script that interacts with that UI element.
*   **Readability:** Test scripts become cleaner and easier to understand as they interact with methods representing user actions rather than direct UI manipulations.
*   **Reusability:** Page Objects and their methods can be reused across multiple test cases.
*   **Reduced Duplication:** Avoids repeating locator definitions and common interaction logic.

**Implementation in this Framework:**
*   Each significant web page or component has its own Page Object class (e.g., `LoginPage`).
*   Page Object classes inherit from `BasePage` to leverage common WebDriver functionalities.
*   Locators are defined as class variables using `selenium.webdriver.common.by.By`.
*   Methods within Page Objects represent user interactions (e.g., `enter_username`, `click_login`).

### 2.2 Pytest Framework
[Pytest](https://docs.pytest.org/en/stable/) is a powerful and flexible testing framework for Python. It simplifies the process of writing small, readable tests and scales to support complex functional testing for applications and libraries. [2]

**Key Pytest Features Used:**
*   **Test Discovery:** Automatically finds tests based on naming conventions (files starting with `test_` or ending with `_test.py`, and functions/methods starting with `test_`).
*   **Fixtures:** Special functions that provide a baseline for tests. They are used for setup and teardown operations, ensuring a clean and consistent environment for each test. In this framework, `conftest.py` defines a `setup` fixture to initialize and quit the WebDriver.
*   **Markers:** Allow for tagging and categorizing tests, enabling selective test execution.

### 2.3 Configuration Management
The framework uses `config/config.py` to manage various settings and parameters. This approach centralizes configuration, making it easy to modify settings without altering test code. Environment variables can override default values, which is particularly useful for CI/CD pipelines and different testing environments.

## 3. Core Components Explained

### 3.1 `config/config.py`
This file defines global configuration parameters for the test framework. It leverages environment variables for flexible deployment.

| Parameter         | Description                                                                 | Default Value         | Environment Variable | Type    |
| :---------------- | :-------------------------------------------------------------------------- | :-------------------- | :------------------- | :------ |
| `BASE_URL`        | The base URL of the application under test.                                 | `http://www.example.com` | `BASE_URL`           | `str`   |
| `BROWSER`         | The browser to use for test execution (`chrome` or `firefox`).              | `chrome`              | `BROWSER`            | `str`   |
| `HEADLESS`        | Boolean to determine if the browser should run in headless mode.            | `True`                | `HEADLESS`           | `bool`  |
| `IMPLICIT_WAIT`   | Implicit wait time in seconds for elements to be present.                   | `10`                  | `IMPLICIT_WAIT`      | `int`   |
| `EXPLICIT_WAIT`   | Explicit wait time in seconds for specific conditions to be met.            | `20`                  | `EXPLICIT_WAIT`      | `int`   |
| `SCREENSHOT_PATH` | Directory to save screenshots on test failures.                             | `screenshots`         | `SCREENSHOT_PATH`    | `str`   |
| `LOG_LEVEL`       | Logging level for the framework (e.g., `INFO`, `DEBUG`, `ERROR`).           | `INFO`                | `LOG_LEVEL`          | `str`   |
| `API_BASE_URL`    | The base URL for API endpoints.                                             | `http://jsonplaceholder.typicode.com` | `API_BASE_URL`       | `str`   |

### 3.2 `pages/base_page.py`
`BasePage` is the parent class for all Page Objects. It encapsulates common WebDriver interactions and explicit wait conditions, ensuring consistency and reducing boilerplate code in derived Page Objects.

**Key Methods:**
*   `__init__(self, driver)`: Initializes the WebDriver and `WebDriverWait` instance.
*   `go_to_url(self, url)`: Navigates the browser to a specified URL.
*   `find_element(self, by_locator)`: Waits for and returns a single visible web element.
*   `find_elements(self, by_locator)`: Waits for and returns a list of visible web elements.
*   `click(self, by_locator)`: Clicks on a web element.
*   `type_into(self, by_locator, text)`: Enters text into an input field.
*   `get_title(self)`: Returns the current page title.
*   `get_text(self, by_locator)`: Returns the visible text of a web element.

### 3.3 `utils/driver_factory.py`
This utility class is responsible for initializing and configuring WebDriver instances based on the specified browser. It uses `webdriver-manager` to automatically download and manage browser executables.

**Key Features:**
*   **`get_driver(browser)`:** Static method that returns a configured WebDriver instance (Chrome or Firefox).
*   **Headless Mode Support:** Configures browser options for headless execution, which is beneficial for CI/CD environments.
*   **Implicit Wait:** Sets a global implicit wait time for the WebDriver.
*   **Window Maximization:** Maximizes the browser window upon initialization.

### 3.4 `api/base_api_client.py`
`BaseApiClient` provides a standardized way to interact with RESTful APIs. It uses the `requests` library to send HTTP requests and handles common error scenarios. This promotes reusability and consistency across API tests.

**Key Methods:**
*   `__init__(self, base_url)`: Initializes the API client with a base URL and a `requests.Session`.
*   `_send_request(self, method, endpoint, **kwargs)`: Internal method to send HTTP requests, handle errors, and return the response.
*   `get(self, endpoint, params=None, headers=None)`: Sends a GET request.
*   `post(self, endpoint, data=None, json=None, headers=None)`: Sends a POST request.
*   `put(self, endpoint, data=None, json=None, headers=None)`: Sends a PUT request.
*   `delete(self, endpoint, headers=None)`: Sends a DELETE request.
*   `patch(self, endpoint, data=None, json=None, headers=None)`: Sends a PATCH request.
*   `close_session(self)`: Closes the `requests` session.

### 3.5 `conftest.py`
This file is central to Pytest's fixture management. It contains the `setup` fixture, which is automatically discovered and executed before and after tests that request it.

**`setup` Fixture:**
*   **Scope:** `function` scope ensures that a new browser instance is launched for each test function, providing isolation.
*   **WebDriver Initialization:** Calls `DriverFactory.get_driver()` to create a WebDriver instance.
*   **Test Context:** Makes the `driver` instance available to test classes via `request.cls.driver`.
*   **Teardown:** Uses `yield` to ensure `driver.quit()` is called after each test function completes, closing the browser and cleaning up resources.

## 4. Writing Tests

### 4.1 Creating Page Objects
To create a new Page Object:
1.  Create a new Python file in the `pages/` directory (e.g., `dashboard_page.py`).
2.  Define a class that inherits from `BasePage`.
3.  Define locators for all relevant UI elements on that page using `By` strategies (e.g., `By.ID`, `By.XPATH`, `By.CSS_SELECTOR`).
4.  Implement methods that represent user interactions or retrieve information from the page.

**Example (`dashboard_page.py`):**
```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    WELCOME_MESSAGE = (By.ID, "welcomeMessage")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/dashboard"

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_MESSAGE)

    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)
```

### 4.2 Creating UI Test Cases
To write new UI test cases:
1.  Create a new Python file in the `tests/` directory (e.g., `test_dashboard.py`).
2.  Define a test class (e.g., `TestDashboard`) that uses the `setup` fixture (`@pytest.mark.usefixtures("setup")`).
3.  Write test methods within the class, ensuring they start with `test_`.
4.  Instantiate Page Objects within your test methods and use their methods to perform actions and assertions.

**Example (`test_dashboard.py`):**
```python
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import Config

@pytest.mark.usefixtures("setup")
class TestDashboard:
    def test_dashboard_load(self):
        self.driver.get(Config.BASE_URL + "/login")
        login_page = LoginPage(self.driver)
        login_page.login("validuser", "validpassword") # Assuming a valid user

        dashboard_page = DashboardPage(self.driver)
        assert "Dashboard" in self.driver.title
        assert "Welcome" in dashboard_page.get_welcome_message()

    def test_logout_functionality(self):
        self.driver.get(Config.BASE_URL + "/login")
        login_page = LoginPage(self.driver)
        login_page.login("validuser", "validpassword")

        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_logout()
        assert "login" in self.driver.current_url # Assert redirection to login page
```

### 4.3 Creating API Test Cases
To write new API test cases:
1.  Create a new Python file in the `tests/api/` directory (e.g., `test_users_api.py`).
2.  Define a test class (e.g., `TestUsersApi`).
3.  Instantiate `BaseApiClient` to interact with the API.
4.  Write test methods within the class, ensuring they start with `test_`.
5.  Use the `BaseApiClient` methods (e.g., `get`, `post`) to send requests and assert on the responses.

**Example (`test_users_api.py`):**
```python
import pytest
from api.base_api_client import BaseApiClient

class TestUsersApi:
    api_client = BaseApiClient()

    def test_get_all_users(self):
        response = self.api_client.get("/users")
        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, list)
        assert len(users) > 0
        assert "id" in users[0]
        assert "name" in users[0]

    def test_get_single_user(self):
        user_id = 1
        response = self.api_client.get(f"/users/{user_id}")
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == user_id
        assert "name" in user
```

### 4.4 Assertions
Assertions are crucial for verifying the expected behavior of the application. Pytest uses standard Python `assert` statements. Ensure assertions are specific, clear, and directly validate the test's objective.

## 5. Advanced Usage and Enhancements

### 5.1 Reporting
Integrate `pytest-html` for generating comprehensive HTML test reports. Install it via `pip install pytest-html` and run tests with `pytest --html=report.html --self-contained-html`.

### 5.2 Logging
Implement a logging utility (e.g., using Python's built-in `logging` module) to record test execution details, errors, and warnings. This aids in debugging and provides an audit trail.

### 5.3 Screenshot on Failure
Enhance the `setup` fixture in `conftest.py` to automatically take screenshots when a test fails. This provides valuable visual context for debugging.

### 5.4 Data-Driven Testing
For tests requiring multiple sets of input data, leverage Pytest's `@pytest.mark.parametrize` decorator or external data sources (CSV, Excel, JSON) to achieve data-driven testing.

### 5.5 CI/CD with GitHub Actions

Continuous Integration/Continuous Deployment (CI/CD) is a critical practice for modern software development, enabling automated testing, building, and deployment of applications. This framework is designed to be easily integrated into CI/CD pipelines, with a strong recommendation for **GitHub Actions** due to its seamless integration with GitHub repositories, ease of use, and robust feature set.

**Key Benefits of GitHub Actions for this Framework:**
*   **Automated Test Execution:** Automatically triggers UI and API tests on code pushes or pull requests, ensuring immediate feedback on code quality.
*   **Environment Consistency:** Provides a consistent execution environment for tests, reducing "it works on my machine" issues.
*   **Faster Feedback Loop:** Developers receive quick feedback on changes, allowing for early detection and resolution of bugs.
*   **Scalability:** Supports parallel test execution, significantly reducing the overall test run time for large test suites.
*   **Reporting:** Can be configured to generate and publish test reports (e.g., JSON, HTML) as build artifacts, providing clear visibility into test results.

**Workflow (`.github/workflows/python-test.yml`):**
A sample GitHub Actions workflow file (`python-test.yml`) is provided in the `.github/workflows/` directory. This workflow demonstrates how to:
1.  **Checkout Code:** Retrieves the project source code.
2.  **Set up Python:** Configures the Python environment.
3.  **Install Dependencies:** Installs all required Python packages from `requirements.txt`, including `selenium`, `pytest`, `requests`, and `webdriver-manager`.
4.  **Install Browser:** Installs Google Chrome for UI test execution.
5.  **Run Tests:** Executes both UI (Selenium) and API (requests) tests using Pytest.
6.  **Upload Reports:** Publishes test reports as artifacts, making them accessible for review.

**Configuration:**
Environment variables for `BASE_URL`, `API_BASE_URL`, and `HEADLESS` can be set directly within the GitHub Actions workflow file, allowing for environment-specific configurations without modifying the codebase.

For detailed instructions on setting up and customizing the GitHub Actions workflow, refer to the `README.md` file in the project root.

## 6. Contribution Guidelines

### 6.1 Coding Standards
Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style. Use linters like `flake8` or `pylint` to ensure code quality and consistency.

### 6.2 Git Workflow
*   Use a feature-branch workflow: Create a new branch for each feature or bug fix.
*   Commit frequently with clear, concise commit messages.
*   Rebase your branch on `main` (or `master`) before creating a Pull Request.

### 6.3 Code Review
All new code should undergo a peer code review process to ensure quality, catch potential issues, and share knowledge within the team.

## References
[1] Selenium. (n.d.). *Page Object Model*. Retrieved from [https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
[2] Pytest. (n.d.). *pytest documentation*. Retrieved from [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)
