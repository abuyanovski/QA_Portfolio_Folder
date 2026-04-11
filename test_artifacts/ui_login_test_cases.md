# SauceDemo Login UI Test Cases

![UI](https://img.shields.io/badge/UI-SauceDemo-E2231A)
![Coverage](https://img.shields.io/badge/Automated%20Checks-2-2EA44F)
![Pattern](https://img.shields.io/badge/Pattern-Page%20Object%20Model-555555)

Focused authentication coverage for SauceDemo, written to show clear Page Object usage, readable test steps, and meaningful state assertions.

## 📌 At A Glance

| Item | Details |
|---|---|
| Application | `https://www.saucedemo.com/` |
| Automated test file | [`tests/ui/test_login.py`](../tests/ui/test_login.py) |
| Page objects | [`pages/login_page.py`](../pages/login_page.py), [`pages/inventory_page.py`](../pages/inventory_page.py) |
| Test runner | Pytest |
| Marker | `ui` |

## 🧪 Automated Coverage

| Case ID | Test | User Story | What It Proves |
|---|---|---|---|
| `TC_LOGIN_001` | `test_successful_login_TC_LOGIN_001` | Standard user signs in successfully | Valid credentials create a usable session and load inventory |
| `TC_LOGIN_002` | `test_locked_out_user_denied_access_TC_LOGIN_002` | Locked-out user is blocked | Access denial is visible, user remains on login, and protected flow is not reached |

## 🔐 Test Data

| Role | Username | Password | Expected Result |
|---|---|---|---|
| Standard user | `standard_user` | `secret_sauce` | Redirect to inventory |
| Locked user | `locked_out_user` | `secret_sauce` | Login error remains visible |

## ✅ Assertion Focus

| Layer | Examples |
|---|---|
| Navigation | URL includes or excludes `inventory.html` |
| Page readiness | inventory title and product list are visible |
| Negative path | locked-out error message is displayed |
| Session boundary | locked-out user remains on the login page |

## 🚀 Execution

Run only login UI tests:

```bash
pytest tests/ui/test_login.py
```

On PowerShell, force headless mode:

```powershell
$env:HEADLESS="True"; pytest tests/ui/test_login.py
```

## 📝 Portfolio Notes

- Login coverage includes one high-value positive path and one important negative path.
- The tests use page objects to keep browser actions readable and reusable.
- Broader manual authentication coverage is tracked in [`docs/saucedemo_manual_test_cases_with_api.xlsx`](../docs/saucedemo_manual_test_cases_with_api.xlsx).
