# QA Automation Framework

## Overview
This repository is a work in progress QA automation framework built with Python, Pytest, Selenium, and `requests`. It currently covers a small but practical slice of automated UI and API testing, with 11 automated tests in place: 7 UI tests and 4 API tests.

Right now, the project includes:
- UI automation for Sauce Demo login, inventory, and cart flows
- API automation for JSONPlaceholder `/posts` endpoints
- Page Object Model structure for UI tests
- Shared pytest fixtures and progress logging for clearer test runs
- Optional HTML and Allure reporting with failure screenshots for UI tests
- Supporting QA assets in `docs/` and `test_artifacts/`

## Current Stack
- Python
- Pytest
- Selenium WebDriver
- `requests`
- `webdriver-manager`
- `pytest-json-report`
- `pytest-html`
- `allure-pytest`

## Current Automated Coverage

The current automated test suite includes:

- Login UI coverage:
  - successful login with a standard user
  - locked-out user access denial and error validation
- Inventory UI coverage:
  - sorting products by price from low to high
  - validating product details page data against inventory list data
- Cart UI coverage:
  - adding one item to cart and validating badge and cart contents
  - removing one item and validating synchronized cart state
  - resetting app state from the side menu and confirming cart state is cleared
- API coverage for JSONPlaceholder `/posts`:
  - get all posts
  - get one post
  - create a post
  - delete a post

Current local verification status:

```bash
HEADLESS=True pytest -m "ui or api"
```

Latest verified result in this workspace:

```text
11 passed
```

## Project Structure
```text
qa-automation-framework/
├── .github/
│   └── workflows/
│       └── python-test.yml
├── api/
│   └── base_api_client.py
├── config/
│   ├── config.py
│   └── conftest.py
├── docs/
│   └── manual_test_cases.xlsx
├── allure-results/
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── reports/
├── test_artifacts/
│   ├── api_posts_test_cases.md
│   ├── ci_cd_tool_recommendation.md
│   ├── saucedemo_manual_test_cases_regenerated.md
│   ├── ui_login_test_cases.md
│   └── matrices/
├── tests/
│   ├── api/
│   │   └── test_posts_api.py
│   └── ui/
│       ├── test_cart.py
│       ├── test_inventory.py
│       └── test_login.py
├── utils/
│   └── driver_factory.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites
- Python 3.9+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd qa-automation-framework
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
The framework reads settings from environment variables in `config/config.py`.

Currently used settings:
- `BASE_URL`: UI base URL placeholder. Default: `http://www.example.com`
- `API_BASE_URL`: API base URL. Default: `http://jsonplaceholder.typicode.com`
- `BROWSER`: Browser for UI tests. Default: `chrome`
- `HEADLESS`: Run browser headless. Default: `False`
- `IMPLICIT_WAIT`: Selenium implicit wait in seconds. Default: `6`
- `EXPLICIT_WAIT`: Configured explicit wait value in seconds. Default: `10`
- `SCREENSHOT_PATH`: Screenshot output directory. Default: `screenshots`
- `LOG_LEVEL`: Logging level placeholder for future expansion. Default: `INFO`
- `CHROMEDRIVER_PATH`: Optional explicit ChromeDriver executable path
- `GECKODRIVER_PATH`: Optional explicit GeckoDriver executable path

Notes:
- `BASE_URL` exists in config, but the current Sauce Demo page objects still use direct page URLs.
- The GitHub Actions workflow sets `HEADLESS=true` for CI runs.

## Running Tests

### Default Run
By default, `pytest` runs the UI suite because `pytest.ini` excludes tests marked `api`. This currently runs 7 UI tests.

```bash
pytest
```

### Run UI Tests
```bash
pytest tests/ui
```

### Run API Tests
```bash
pytest -m api
```

### Run UI and API Tests Together
```bash
pytest -m "ui or api"
```

On PowerShell, to force headless execution for a local full-suite run:

```powershell
$env:HEADLESS="True"; pytest -m "ui or api"
```

### Run Specific Files
```bash
pytest tests/ui/test_login.py
pytest tests/ui/test_inventory.py
pytest tests/ui/test_cart.py
pytest tests/api/test_posts_api.py -m api
```

### Run Specific Test Cases
```bash
pytest tests/ui/test_login.py::TestLogin::test_successful_login_TC_LOGIN_001
pytest tests/api/test_posts_api.py::TestPostsApi::test_get_single_post -m api
```

### Test Output
The current pytest setup prints progress information during execution, including:
- session start and finish
- collected test counts
- per-test start and end status
- numbered step messages inside tests

### Generate an HTML Report
```bash
pytest tests/ui --html=reports/ui-report.html --self-contained-html
```

Notes:
- UI test failures automatically save screenshots into `reports/screenshots/` when an HTML report is enabled.
- The HTML report includes environment metadata such as browser, headless mode, and configured base URLs.

### Generate Allure Results
```bash
pytest tests/ui --alluredir=allure-results
```

To render the report locally, use the Allure CLI after installing it on your machine:

```bash
allure serve allure-results
```

Or generate a static report:

```bash
allure generate allure-results --clean -o allure-report
```

When Allure reporting is enabled, failed UI tests attach screenshots to the Allure result.

## CI/CD
The GitHub Actions workflow in `.github/workflows/python-test.yml` currently:
- runs on pushes and pull requests to `main`
- installs dependencies
- executes UI tests with both JSON and self-contained HTML reporting enabled
- uploads the generated `reports/` directory as a build artifact

The workflow sets:
- `BASE_URL=https://www.saucedemo.com`
- `HEADLESS=true`

## Documentation and QA Assets
Additional supporting material is already included in the repo:
- `docs/` for higher-level project documentation and manual test materials
- `test_artifacts/` for generated/manual QA assets and coverage-related files

Useful files:
- `test_artifacts/api_posts_test_cases.md`
- `test_artifacts/ui_login_test_cases.md`
- `test_artifacts/saucedemo_manual_test_cases_regenerated.md`
- `test_artifacts/matrices/feature_coverage_matrix.xlsx`

Generated runtime output may appear in `reports/`, `allure-results/`, and `screenshots/`; those outputs are ignored by Git except for placeholder files.

## Notes
- The framework is intentionally small at this stage, but the current UI and API test checkpoint is passing locally.
- Some config values and support files are in place for future expansion even if they are not fully wired into every test yet.
- The current automated coverage is focused on a few representative UI and API flows rather than full application coverage.
- Generated report, screenshot, cache, virtual environment, and IDE files are ignored by Git.
