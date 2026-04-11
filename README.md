# QA Automation Framework

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-9.x-0A9EDC?logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)
![API](https://img.shields.io/badge/API-requests-2D6CDF)
![Status](https://img.shields.io/badge/Current%20Checkpoint-11%20Passing%20Tests-2EA44F)

Portfolio-ready QA automation framework covering browser UI tests, REST API tests, manual test design, reporting, and CI-friendly execution.
THIS IS WIP AND THIS REPO IS IN ACTIVE DEVELOPMENT

## 📌 Portfolio Snapshot

| Area | Current State |
|---|---|
| Automated tests | 11 total: 7 UI + 4 API |
| UI target | SauceDemo login, inventory, and cart workflows |
| API target | JSONPlaceholder `/posts` endpoints |
| Test design assets | Manual UI + API workbook with 18 documented cases |
| Framework style | Pytest fixtures, Selenium Page Object Model, reusable API client |
| Reporting | Console progress logs, HTML reports, Allure results, failure screenshots |
| CI | GitHub Actions workflow for headless UI execution |

## 🔗 Quick Links

| Asset | Link |
|---|---|
| Manual UI and API workbook | [docs/saucedemo_manual_test_cases_with_api.xlsx](docs/saucedemo_manual_test_cases_with_api.xlsx) |
| API testing scope | [test_artifacts/api_posts_test_cases.md](test_artifacts/api_posts_test_cases.md) |
| Login UI test notes | [test_artifacts/ui_login_test_cases.md](test_artifacts/ui_login_test_cases.md) |
| API test implementation | [tests/api/test_posts_api.py](tests/api/test_posts_api.py) |
| API client | [api/base_api_client.py](api/base_api_client.py) |
| UI tests | [tests/ui/](tests/ui/) |
| Page objects | [pages/](pages/) |
| CI workflow | [.github/workflows/python-test.yml](.github/workflows/python-test.yml) |

## 🧰 Current Stack

| Layer | Tools |
|---|---|
| Test runner | Pytest |
| UI automation | Selenium WebDriver, webdriver-manager |
| API automation | requests |
| Reporting | pytest-html, pytest-json-report, allure-pytest |
| Structure | Page Object Model, shared fixtures, reusable client classes |

## 🧪 Automated Coverage

| Suite | Coverage | Automated Checks |
|---|---|---|
| Login UI | Standard and locked-out user paths | Redirect validation, inventory load checks, error message checks |
| Inventory UI | Product sorting and product details | Price ordering, item count stability, detail page data consistency |
| Cart UI | Add, remove, and reset state | Badge count, cart contents, removal sync, reset app state behavior |
| API `/posts` | Representative CRUD-style flow | `GET /posts`, `GET /posts/1`, `POST /posts`, `DELETE /posts/1` |

See [test_artifacts/api_posts_test_cases.md](test_artifacts/api_posts_test_cases.md) for the current automated API testing scope.

## ✅ Verification Checkpoint

Latest local full-suite command:

```bash
HEADLESS=True pytest -m "ui or api"
```

Latest verified result in this workspace:

```text
11 passed
```

## 📘 Manual Test Case Assets

The current workbook is [docs/saucedemo_manual_test_cases_with_api.xlsx](docs/saucedemo_manual_test_cases_with_api.xlsx).

It replaces the previous `docs/manual_test_cases.xlsx` workbook and includes:

| Manual Suite | Count | Case IDs |
|---|---:|---|
| SauceDemo UI | 10 | `TC_LOGIN_001`, `TC_LOGIN_002`, `TC_INV_001`, `TC_INV_002`, `TC_CART_001`, `TC_CART_002`, `TC_CART_003`, `TC_CHECKOUT_001`, `TC_CHECKOUT_002`, `TC_CHECKOUT_003` |
| API scenarios | 8 | `TC_API_001` through `TC_API_008` |
| Summary tracker | 1 sheet | Execution status, priority, and automation readiness |

The manual workbook is intentionally broader than the automated suite. Checkout scenarios are documented as manual coverage, while checkout automation remains a future expansion area.

## 📁 Project Structure
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
│   └── saucedemo_manual_test_cases_with_api.xlsx
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

## ⚙️ Setup

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

## 🛠️ Configuration
The framework reads settings from environment variables in [config/config.py](config/config.py).

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

## 🚀 Running Tests

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

## 🔄 CI/CD
The GitHub Actions workflow in [.github/workflows/python-test.yml](.github/workflows/python-test.yml) currently:
- runs on pushes and pull requests to `main`
- installs dependencies
- executes UI tests with both JSON and self-contained HTML reporting enabled
- uploads the generated `reports/` directory as a build artifact

The workflow sets:
- `BASE_URL=https://www.saucedemo.com`
- `HEADLESS=true`

## 📚 Documentation and QA Assets
Additional supporting material is already included in the repo:
- [docs/](docs/) for higher-level project documentation and manual test materials
- [test_artifacts/](test_artifacts/) for generated/manual QA assets and coverage-related files

Useful files:
- [docs/saucedemo_manual_test_cases_with_api.xlsx](docs/saucedemo_manual_test_cases_with_api.xlsx)
- [test_artifacts/api_posts_test_cases.md](test_artifacts/api_posts_test_cases.md)
- [test_artifacts/ui_login_test_cases.md](test_artifacts/ui_login_test_cases.md)
- [test_artifacts/saucedemo_manual_test_cases_regenerated.md](test_artifacts/saucedemo_manual_test_cases_regenerated.md)
- [test_artifacts/matrices/feature_coverage_matrix.xlsx](test_artifacts/matrices/feature_coverage_matrix.xlsx)

Generated runtime output may appear in `reports/`, `allure-results/`, and `screenshots/`; those outputs are ignored by Git except for placeholder files.

## 📝 Notes
- The framework is intentionally small at this stage, but the current UI and API test checkpoint is passing locally.
- Some config values and support files are in place for future expansion even if they are not fully wired into every test yet.
- The current automated coverage is focused on a few representative UI and API flows rather than full application coverage.
- Generated report, screenshot, cache, virtual environment, and IDE files are ignored by Git.
