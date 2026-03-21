# QA Automation Project with Python, Selenium, and API Testing

## Overview
This project provides a robust and scalable test automation framework built with Python, Selenium, and the `requests` library for API testing, designed for QA Analyst II level professionals. It follows the Page Object Model (POM) design pattern for UI tests and a dedicated API client for API tests to enhance test maintainability, reduce code duplication, and improve readability. The framework is configured to support multiple browsers and environments, making it flexible for various testing needs.

## Features
- **Page Object Model (POM):** Organizes UI elements and interactions into classes, promoting reusability and maintainability.
- **API Testing:** Includes a `BaseApiClient` for structured and reusable API test development using the `requests` library.
- **Pytest Framework:** Utilizes Pytest for test discovery, execution, and reporting, offering powerful fixtures and plugins.
- **WebDriver Manager:** Automatically handles browser driver management, eliminating manual downloads and configuration.
- **Configurable Environment:** Easy configuration of base URLs, browsers, and wait times via `config.py` and environment variables.
- **Cross-Browser Testing:** Supports Chrome and Firefox out-of-the-box.
- **Headless Mode:** Option to run browser tests in headless mode for faster execution in CI/CD pipelines.
- **CI/CD Integration:** Includes a sample GitHub Actions workflow for automated test execution.

## Project Structure
```
qa_automation_project/
├── .github/
│   └── workflows/
│       └── python-test.yml   # GitHub Actions workflow for CI/CD
├── api/
│   └── base_api_client.py    # Base class for all API interactions
├── config/
│   └── config.py             # Configuration settings for the framework
├── pages/
│   ├── base_page.py          # Base class for all Page Objects
│   └── login_page.py         # Example Page Object for a login page
├── tests/
│   ├── api/                  # Directory for API test suites
│   │   └── test_posts_api.py # Example API test suite for posts
│   └── test_login.py         # Example UI test suite for the login page
├── utils/
│   └── driver_factory.py     # Handles WebDriver initialization
├── conftest.py               # Pytest fixtures for test setup and teardown
├── requirements.txt          # Python dependencies
└── README.md                 # Project README file
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd qa_automation_project
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run Tests

### Environment Variables
You can configure the test execution using environment variables:
- `BASE_URL`: The base URL of the application under test (default: `http://www.example.com`)
- `API_BASE_URL`: The base URL for API endpoints (default: `http://jsonplaceholder.typicode.com`)
- `BROWSER`: The browser to use for UI testing (`chrome` or `firefox`, default: `chrome`)
- `HEADLESS`: Run browser in headless mode (`True` or `False`, default: `True`)
- `IMPLICIT_WAIT`: Implicit wait time in seconds (default: `10`)
- `EXPLICIT_WAIT`: Explicit wait time in seconds (default: `20`)

**Example:**
```bash
export BASE_URL="https://staging.example.com"\
       API_BASE_URL="https://api.staging.example.com"\
       BROWSER="firefox"\
       HEADLESS="False"
pytest
```

### Running All Tests (UI and API)
To run all tests in the `tests/` directory:
```bash
pytest
```

### Running UI Tests Only
To run tests from the UI test directory:
```bash
pytest tests/test_login.py
```

### Running API Tests Only
To run tests from the API test directory:
```bash
pytest tests/api/test_posts_api.py
```

### Running Specific Test Files
To run tests from a specific file:
```bash
pytest tests/test_login.py
pytest tests/api/test_posts_api.py
```

### Running Specific Test Cases
To run a specific test method within a file:
```bash
pytest tests/test_login.py::TestLogin::test_successful_login
pytest tests/api/test_posts_api.py::TestPostsApi::test_get_single_post
```

### Generating Reports
Pytest supports various reporting plugins. For example, to generate an HTML report:
```bash
pytest --html=report.html --self-contained-html
```

## CI/CD with GitHub Actions
A sample GitHub Actions workflow (`.github/workflows/python-test.yml`) is provided to demonstrate how to integrate this framework into a CI/CD pipeline. This workflow will automatically:
1.  **Checkout Code:** Retrieve the project source code.
2.  **Set up Python:** Configure the Python environment.
3.  **Install Dependencies:** Install all required Python packages from `requirements.txt`.
4.  **Install Browser:** Install Google Chrome for UI test execution.
5.  **Run Tests:** Execute both UI (Selenium) and API (requests) tests using Pytest.
6.  **Upload Reports:** Publish test reports as artifacts, making them accessible for review.

**To use the GitHub Actions workflow:**
1.  Push your project to a GitHub repository.
2.  The workflow will automatically trigger on pushes to the `main` branch.
3.  Monitor the workflow runs in the "Actions" tab of your GitHub repository.

## Best Practices for QA Analyst II
- **Maintainability:** Adhere strictly to the Page Object Model for UI tests and create dedicated API clients for API tests. Ensure objects are clean, concise, and only contain elements/methods related to their specific domain.
- **Readability:** Write clear, self-documenting code. Use meaningful variable and function names. Add comments where necessary to explain complex logic.
- **Reusability:** Design reusable components and utility functions to avoid code duplication. Leverage Pytest fixtures for common setup and teardown tasks.
- **Robustness:** Implement appropriate waits (explicit waits are preferred) to handle dynamic web elements and improve UI test stability. For API tests, handle various HTTP response codes and error scenarios gracefully.
- **Error Handling:** Implement logging and screenshot capabilities on UI test failures to aid in debugging. For API tests, log request/response details for failed tests.
- **Version Control:** Use Git for version control, commit frequently with descriptive messages, and follow a branching strategy.
- **CI/CD Integration:** Design tests to be easily integrated into Continuous Integration/Continuous Deployment pipelines for automated execution.

## Further Documentation
For more in-depth information on the framework's design principles, advanced usage, and contribution guidelines, please refer to `DOCUMENTATION.md`.
