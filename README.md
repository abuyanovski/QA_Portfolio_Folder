# QA Automation Framework

## Overview
This repository is a work in progress QA automation framework built with Python, Pytest, Selenium, and `requests`. It currently covers a small but practical slice of automated UI and API testing, and it will continue to grow to cover more aspects of QA over time.

Right now, the project includes:
- UI automation for Sauce Demo login, inventory, and cart flows
- API automation for JSONPlaceholder `/posts` endpoints
- Page Object Model structure for UI tests
- Shared pytest fixtures and progress logging for clearer test runs
- Supporting QA assets in `docs/` and `test_artifacts/`

## Current Stack
- Python
- Pytest
- Selenium WebDriver
- `requests`
- `webdriver-manager`
- `pytest-json-report`

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
│   ├── Detailed Documentation_ QA Automation Framework.md
│   ├── manual_test_cases.xlsx
│   └── QA Automation Project with Python, Selenium, and API Testing.md
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── inventory_page.py
│   └── login_page.py
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
- `API_BASE_URL`: API base URL. Default: `http://jsonplaceholder.typicode.com`
- `BROWSER`: Browser for UI tests. Default: `chrome`
- `HEADLESS`: Run browser headless. Default: `False`
- `IMPLICIT_WAIT`: Selenium implicit wait in seconds. Default: `10`
- `EXPLICIT_WAIT`: Configured explicit wait value in seconds. Default: `20`
- `SCREENSHOT_PATH`: Screenshot output directory. Default: `screenshots`
- `LOG_LEVEL`: Logging level placeholder for future expansion. Default: `INFO`

Notes:
- `BASE_URL` exists in config, but the current Sauce Demo page objects still use direct page URLs.
- The GitHub Actions workflow sets `HEADLESS=true` for CI runs.

## Running Tests

### Default Run
By default, `pytest` runs the UI suite because `pytest.ini` excludes tests marked `api`.

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

## CI/CD
The GitHub Actions workflow in `.github/workflows/python-test.yml` currently:
- runs on pushes and pull requests to `main`
- installs dependencies
- executes pytest with JSON reporting enabled
- uploads `report.json` as a build artifact

The workflow sets:
- `BASE_URL=https://www.saucedemo.com`
- `API_BASE_URL=https://jsonplaceholder.typicode.com`
- `HEADLESS=true`

## Documentation and QA Assets
Additional supporting material is already included in the repo:
- `docs/` for higher-level project documentation and manual test materials
- `test_artifacts/` for generated/manual QA assets and coverage-related files

Useful files:
- `docs/Detailed Documentation_ QA Automation Framework.md`
- `docs/QA Automation Project with Python, Selenium, and API Testing.md`
- `test_artifacts/api_posts_test_cases.md`
- `test_artifacts/ui_login_test_cases.md`

## Notes
- The framework is intentionally small at this stage and is being built out incrementally.
- Some config values and support files are in place for future expansion even if they are not fully wired into every test yet.
- The current automated coverage is focused on a few representative UI and API flows rather than full application coverage.
