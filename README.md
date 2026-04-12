<div align="center">

# QA Automation Framework

**Portfolio-ready QA automation project for UI testing, API testing, manual test design, reporting, and CI-friendly execution.**

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-9.x-0A9EDC?logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)
![Google Chrome](https://img.shields.io/badge/Chrome-UI%20Automation-4285F4?logo=googlechrome&logoColor=white)

![Requests](https://img.shields.io/badge/Requests-API%20Testing-20232A?logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-Response%20Validation-000000?logo=json&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI-2088FF?logo=githubactions&logoColor=white)
![Allure Report](https://img.shields.io/badge/Allure-Reporting-FF6A00?logo=allure&logoColor=white)

![Checkpoint](https://img.shields.io/badge/Checkpoint-13%20Passed%20%7C%201%20Expected%20XFail-2EA44F)
![Automated Tests](https://img.shields.io/badge/Automated%20Tests-14-6F42C1)
![UI Tests](https://img.shields.io/badge/UI%20Tests-10-43B02A)
![API Tests](https://img.shields.io/badge/API%20Tests-4-2D6CDF)

</div>

---

## 📌 Project Story

This framework demonstrates a practical QA automation workflow: manual test design, Selenium UI automation, REST API checks, reusable page objects, reusable API client code, reporting hooks, and CI-ready execution.

It is intentionally built as a portfolio project, so the repo shows both the finished test code and the QA thinking behind it: coverage planning, test data choices, validation strategy, and current suite health.

> **Status:** Active work in progress. New scenarios and documentation are being added as the framework grows.

---

## ✨ Highlights

| Area | What This Shows |
|---|---|
| UI automation | SauceDemo login, inventory, cart, and checkout workflows |
| API automation | JSONPlaceholder `/posts` CRUD-style checks |
| Test design | Manual UI + API workbook with 18 documented cases |
| Framework structure | Pytest fixtures, Selenium Page Object Model, reusable API client |
| Reporting | Console progress logs, HTML reports, Allure results, failure screenshots |
| CI readiness | GitHub Actions workflow for headless browser execution |
| Quality signal | 14 collected tests: 13 passed, 1 expected xfail |

---

## 🔗 Quick Navigation

| Portfolio Asset | Link |
|---|---|
| Manual UI and API workbook | [docs/saucedemo_manual_test_cases_with_api.xlsx](docs/saucedemo_manual_test_cases_with_api.xlsx) |
| API testing scope | [test_artifacts/api_posts_test_cases.md](test_artifacts/api_posts_test_cases.md) |
| Login UI test notes | [test_artifacts/ui_login_test_cases.md](test_artifacts/ui_login_test_cases.md) |
| Checkout UI test notes | [test_artifacts/ui_checkout_test_cases.md](test_artifacts/ui_checkout_test_cases.md) |
| API test implementation | [tests/api/test_posts_api.py](tests/api/test_posts_api.py) |
| Checkout test implementation | [tests/ui/test_checkout.py](tests/ui/test_checkout.py) |
| API client | [api/base_api_client.py](api/base_api_client.py) |
| UI tests | [tests/ui/](tests/ui/) |
| Page objects | [pages/](pages/) |
| CI workflow | [.github/workflows/python-test.yml](.github/workflows/python-test.yml) |

---

## 🧰 Tech Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Test runner | Pytest |
| UI automation | Selenium WebDriver, Chrome, webdriver-manager |
| API automation | requests |
| Reporting | pytest-html, pytest-json-report, allure-pytest |
| Architecture | Page Object Model, shared fixtures, reusable client classes |
| CI | GitHub Actions |

---

## 🧪 Automated Coverage

| Suite | Coverage | Automated Checks |
|---|---|---|
| Login UI | Standard and locked-out user paths | Redirect validation, inventory load checks, error message checks |
| Inventory UI | Product sorting and product details | Price ordering, item count stability, detail page data consistency |
| Cart UI | Add, remove, and reset state | Badge count, cart contents, removal sync, reset app state behavior |
| Checkout UI | Successful checkout, validation, and `error_user` behavior | Overview item consistency, required-field validation, completion state observation |
| API `/posts` | Representative CRUD-style flow | `GET /posts`, `GET /posts/1`, `POST /posts`, `DELETE /posts/1` |

See [test_artifacts/api_posts_test_cases.md](test_artifacts/api_posts_test_cases.md) for the current automated API testing scope.

---

## ✅ Current Checkpoint

Latest full-suite command:

```bash
HEADLESS=True pytest -m "ui or api"
```

Latest verified result:

```text
13 passed, 1 xfailed
```

The expected `xfail` documents SauceDemo `error_user` checkout behavior. It is intentionally tracked because the abnormal behavior is useful QA evidence, not a hidden failure.

---

## 📘 Manual Test Case Assets

The current workbook is [docs/saucedemo_manual_test_cases_with_api.xlsx](docs/saucedemo_manual_test_cases_with_api.xlsx).

It replaces the previous `docs/manual_test_cases.xlsx` workbook and includes:

| Manual Suite | Count | Case IDs |
|---|---:|---|
| SauceDemo UI | 10 | `TC_LOGIN_001`, `TC_LOGIN_002`, `TC_INV_001`, `TC_INV_002`, `TC_CART_001`, `TC_CART_002`, `TC_CART_003`, `TC_CHECKOUT_001`, `TC_CHECKOUT_002`, `TC_CHECKOUT_003` |
| API scenarios | 8 | `TC_API_001` through `TC_API_008` |
| Summary tracker | 1 sheet | Execution status, priority, and automation readiness |

The UI automation now maps to the current login, inventory, cart, and checkout case IDs in the workbook.

---

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
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── reports/
├── test_artifacts/
│   ├── api_posts_test_cases.md
│   ├── ci_cd_tool_recommendation.md
│   ├── saucedemo_manual_test_cases_regenerated.md
│   ├── ui_checkout_test_cases.md
│   ├── ui_login_test_cases.md
│   └── matrices/
├── tests/
│   ├── api/
│   │   └── test_posts_api.py
│   └── ui/
│       ├── test_cart.py
│       ├── test_checkout.py
│       ├── test_inventory.py
│       └── test_login.py
├── utils/
│   └── driver_factory.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### Prerequisites

- Python 3.9+
- pip
- Chrome for UI execution

### Installation

```bash
git clone <repository_url>
cd qa-automation-framework
pip install -r requirements.txt
```

---

## 🛠️ Configuration

The framework reads settings from environment variables in [config/config.py](config/config.py).

| Variable | Purpose | Default |
|---|---|---|
| `BASE_URL` | UI base URL placeholder | `http://www.example.com` |
| `API_BASE_URL` | API base URL | `http://jsonplaceholder.typicode.com` |
| `BROWSER` | Browser for UI tests | `chrome` |
| `HEADLESS` | Run browser headless | `False` |
| `IMPLICIT_WAIT` | Selenium implicit wait seconds | `6` |
| `EXPLICIT_WAIT` | Selenium explicit wait seconds | `10` |
| `SCREENSHOT_PATH` | Screenshot output directory | `screenshots` |
| `LOG_LEVEL` | Logging level placeholder | `INFO` |
| `CHROMEDRIVER_PATH` | Optional ChromeDriver executable path | unset |
| `GECKODRIVER_PATH` | Optional GeckoDriver executable path | unset |

Notes:

- `BASE_URL` exists in config, but the current SauceDemo page objects still use direct page URLs.
- UI tests select the browser with the pytest `--browser` option or the `BROWSER` environment variable. Supported values are `chrome` and `firefox`; default is `chrome`. The command-line option takes precedence.
- The GitHub Actions workflow sets `HEADLESS=true` for CI runs.

---

## 🚀 Running Tests

| Goal | Command |
|---|---|
| Default UI run | `pytest` |
| All UI tests | `pytest tests/ui` |
| UI tests in Chrome | `pytest tests/ui --browser chrome` |
| UI tests in Firefox | `pytest tests/ui --browser firefox` |
| API tests only | `pytest -m api` |
| UI + API together | `pytest -m "ui or api"` |
| Login tests | `pytest tests/ui/test_login.py` |
| Checkout tests | `pytest tests/ui/test_checkout.py` |
| API posts tests | `pytest tests/api/test_posts_api.py -m api` |

PowerShell headless full-suite run:

```powershell
$env:HEADLESS="True"; pytest -m "ui or api"
```

Run specific examples:

```bash
pytest tests/ui/test_login.py::TestLogin::test_successful_login_TC_LOGIN_001
pytest tests/ui/test_checkout.py::TestCheckout::test_successful_checkout_with_valid_customer_information_TC_CHECKOUT_001
pytest tests/api/test_posts_api.py::TestPostsApi::test_get_single_post -m api
```

---

## 📊 Reporting

| Report Type | Command / Behavior |
|---|---|
| Console progress | Built into pytest hooks in `conftest.py` |
| HTML report | `pytest tests/ui --html=reports/ui-report.html --self-contained-html` |
| Failure screenshots | Captured automatically for UI failures |
| Allure results | `pytest tests/ui --alluredir=allure-results` |
| Static Allure report | `allure generate allure-results --clean -o allure-report` |

Serve Allure locally after installing the Allure CLI:

```bash
allure serve allure-results
```

---

## 🔄 CI/CD

The GitHub Actions workflow in [.github/workflows/python-test.yml](.github/workflows/python-test.yml) currently:

- runs on pushes and pull requests to `main`
- installs dependencies
- executes UI tests with JSON and self-contained HTML reporting enabled
- uploads the generated `reports/` directory as a build artifact

The workflow sets:

- `BASE_URL=https://www.saucedemo.com`
- `HEADLESS=true`

---

## 📚 Documentation and QA Assets

| Asset | Purpose |
|---|---|
| [docs/](docs/) | Manual test workbooks and higher-level project materials |
| [test_artifacts/](test_artifacts/) | Generated/manual QA assets and coverage notes |
| [docs/saucedemo_manual_test_cases_with_api.xlsx](docs/saucedemo_manual_test_cases_with_api.xlsx) | Current UI + API manual workbook |
| [test_artifacts/api_posts_test_cases.md](test_artifacts/api_posts_test_cases.md) | Automated API testing scope |
| [test_artifacts/ui_checkout_test_cases.md](test_artifacts/ui_checkout_test_cases.md) | Checkout UI testing scope |
| [test_artifacts/ui_login_test_cases.md](test_artifacts/ui_login_test_cases.md) | Login UI testing scope |
| [test_artifacts/saucedemo_manual_test_cases_regenerated.md](test_artifacts/saucedemo_manual_test_cases_regenerated.md) | Manual SauceDemo E2E scenarios |
| [test_artifacts/matrices/feature_coverage_matrix.xlsx](test_artifacts/matrices/feature_coverage_matrix.xlsx) | Coverage matrix |

Generated runtime output may appear in `reports/`, `allure-results/`, and `screenshots/`; those outputs are ignored by Git except for placeholder files.

---

## 📝 Notes

- This is an active portfolio project, so new automation and documentation will continue to be added.
- Current automated coverage focuses on representative UI and API flows rather than full application coverage.
- The suite documents both clean passing behavior and known abnormal behavior through an expected `xfail`.
- Generated report, screenshot, cache, virtual environment, and IDE files are ignored by Git.
