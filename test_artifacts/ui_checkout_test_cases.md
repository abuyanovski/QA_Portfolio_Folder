# SauceDemo Checkout UI Test Cases

![UI](https://img.shields.io/badge/UI-SauceDemo-E2231A)
![Coverage](https://img.shields.io/badge/Automated%20Checks-3-2EA44F)
![Behavior](https://img.shields.io/badge/Includes-Expected%20XFail-9A6700)

Checkout coverage validates the most business-visible part of the SauceDemo flow: moving a selected item from cart to checkout, proving the overview data is consistent, handling required-field validation, and documenting `error_user` behavior.

## 📌 At A Glance

| Item | Details |
|---|---|
| Application | `https://www.saucedemo.com/` |
| Automated test file | [`tests/ui/test_checkout.py`](../tests/ui/test_checkout.py) |
| Page objects | [`pages/cart_page.py`](../pages/cart_page.py), [`pages/checkout_page.py`](../pages/checkout_page.py), [`pages/inventory_page.py`](../pages/inventory_page.py), [`pages/login_page.py`](../pages/login_page.py) |
| Test runner | Pytest |
| Marker | `ui` |

## 🧪 Automated Coverage

| Case ID | Test | User Story | What It Proves |
|---|---|---|---|
| `TC_CHECKOUT_001` | `test_successful_checkout_with_valid_customer_information_TC_CHECKOUT_001` | Standard user completes checkout with valid customer data | Selected item remains consistent from inventory through checkout overview, and confirmation loads after finish |
| `TC_CHECKOUT_002` | `test_checkout_blocks_progress_when_first_name_is_blank_TC_CHECKOUT_002` | Checkout blocks missing required first name | User remains on the information step and sees the expected validation message |
| `TC_CHECKOUT_003` | `test_error_user_checkout_completion_behavior_TC_CHECKOUT_003` | `error_user` checkout finish behavior is observed | Abnormal completion behavior is captured as an expected xfail with diagnostic state in the message |

## 🔐 Test Data

| Role | Username | Password | Checkout Data |
|---|---|---|---|
| Standard user | `standard_user` | `secret_sauce` | `Anton`, `Buyer`, `98042` |
| Error user | `error_user` | `secret_sauce` | `Anton`, `Buyer`, `98042` |
| Validation path | `standard_user` | `secret_sauce` | blank first name, `Buyer`, `98042` |

## ✅ Assertion Focus

| Layer | Examples |
|---|---|
| Cart readiness | cart page loads and contains exactly one item before checkout |
| Checkout information | first name, last name, and postal code drive the next step |
| Validation | blank first name blocks progress and shows a required-field message |
| Data consistency | checkout overview item matches selected inventory item name, description, and price |
| Completion behavior | standard user reaches confirmation; `error_user` behavior is recorded as expected abnormal behavior |

## 🚀 Execution

Run only checkout UI tests:

```bash
pytest tests/ui/test_checkout.py
```

Run one checkout case:

```bash
pytest -m ui -k "TC_CHECKOUT_001 or successful_checkout"
```

On PowerShell, force visible browser execution:

```powershell
$env:HEADLESS="False"; pytest -m ui -k "TC_CHECKOUT_001 or successful_checkout" -v
```

## 📝 Portfolio Notes

- Checkout coverage demonstrates positive flow, validation flow, and exploratory defect documentation.
- `TC_CHECKOUT_003` is intentionally marked `xfail` when SauceDemo keeps `error_user` on checkout overview instead of completing normally.
- The test records the observed URL, checkout title, and error text in the xfail reason so the behavior is traceable.
- This is useful portfolio evidence because it shows the test suite can document product behavior without forcing unstable expectations into the pass/fail signal.
