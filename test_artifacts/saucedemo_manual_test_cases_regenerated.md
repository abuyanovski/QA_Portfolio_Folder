
# SauceDemo Manual E2E Test Cases
**Project:** SauceDemo Web Application  
**Application URL:** https://www.saucedemo.com/  
**Document Type:** Manual End-to-End Test Case Suite  
**Prepared For:** QA Analyst / QA Automation Engineer Portfolio  
**Version:** 1.0  

---

## 1. Purpose
This document contains **10 complete end-to-end manual test cases** for SauceDemo.  
The suite is designed to demonstrate practical QA coverage across:

- Authentication
- Product inventory
- Product details
- Cart behavior
- Checkout flow
- Input validation
- Navigation and session handling

These are suitable as:
- portfolio documentation,
- source material for later Selenium/Pytest automation,
- interview discussion material for QA Analyst or QA Automation Engineer roles.

---

## 2. Test Environment

| Field | Value |
|---|---|
| Application | SauceDemo |
| URL | https://www.saucedemo.com/ |
| Browser | Chrome / Edge / Firefox |
| Test Level | End-to-End |
| Test Type | Manual Functional Testing |
| Suggested Evidence | Screenshots of each major checkpoint |

---

## 3. Test Data

| Data Item | Value |
|---|---|
| Valid Username | `standard_user` |
| Locked Username | `locked_out_user` |
| Invalid Username | `invalid_user` |
| Valid Password | `secret_sauce` |
| Invalid Password | `wrong_password` |
| First Name | Anton |
| Last Name | Tester |
| Postal Code | 98042 |

---

## 4. Coverage Summary

| Coverage Area | Included |
|---|---|
| Login | Yes |
| Negative Authentication | Yes |
| Inventory | Yes |
| Product Detail | Yes |
| Cart | Yes |
| Checkout | Yes |
| Checkout Validation | Yes |
| Logout / Session | Yes |
| Sorting | Yes |
| Cart Modification | Yes |

---

## 5. Test Case Index

| TC ID | Title | Priority | Type |
|---|---|---|---|
| TC-001 | Successful login and checkout with one item | High | Positive E2E |
| TC-002 | Successful checkout with multiple items | High | Positive E2E |
| TC-003 | Locked-out user cannot access inventory | High | Negative E2E |
| TC-004 | Invalid login credentials show error | High | Negative E2E |
| TC-005 | Add item from product detail page and complete checkout | High | Positive E2E |
| TC-006 | Remove item from cart, continue shopping, add another item, complete checkout | Medium-High | Positive E2E |
| TC-007 | Sort products, select item, and complete checkout | Medium | Positive E2E |
| TC-008 | Checkout validation blocks missing required fields, then recovery succeeds | High | Negative-to-Positive E2E |
| TC-009 | Cancel checkout and verify cart state remains correct | Medium | Navigation / State E2E |
| TC-010 | Logout ends session and blocks continued access to protected flow | High | Session / Security E2E |

---

# TC-001 — Successful Login and Checkout With One Item

## Objective
Verify a user can log in, add one item to the cart, complete checkout, and see order confirmation.

## Priority
**High**

## Preconditions
- User is on the login page.
- No required prior cart state.

## Test Data
- Username: `standard_user`
- Password: `secret_sauce`
- First Name: `Anton`
- Last Name: `Tester`
- Postal Code: `98042`

## Steps and Expected Results

| Step # | Action | Expected Result |
|---|---|---|
| 1 | Open `https://www.saucedemo.com/` | Login page loads successfully |
| 2 | Enter valid username | Username field accepts input |
| 3 | Enter valid password | Password field accepts input |
| 4 | Click **Login** | User is redirected to inventory page |
| 5 | Verify inventory page | Product list is displayed |
| 6 | Add the first listed item to the cart | Button changes state and cart badge updates |
| 7 | Verify cart badge | Cart badge displays `1` |
| 8 | Open cart | Cart page loads |
| 9 | Verify selected item in cart | Added item is displayed in cart |
| 10 | Click **Checkout** | Checkout information page loads |
| 11 | Enter first name, last name, postal code | Fields accept valid input |
| 12 | Click **Continue** | Checkout overview page loads |
| 13 | Review checkout overview | Selected item is listed in order summary |
| 14 | Click **Finish** | Checkout completes |
| 15 | Verify confirmation page | Success message is displayed |

## Expected Outcome
User completes the full purchase flow successfully and sees final order confirmation.

---

# TC-002 — Successful Checkout With Multiple Items

## Objective
Verify a user can add multiple items, see the correct cart count, and complete checkout successfully.

## Priority
**High**

## Preconditions
- User is on login page.

## Test Data
- Username: `standard_user`
- Password: `secret_sauce`

## Steps and Expected Results

| Step # | Action | Expected Result |
|---|---|---|
| 1 | Log in with valid credentials | Inventory page loads |
| 2 | Add two different products | Both items are added successfully |
| 3 | Verify cart badge | Cart badge displays `2` |
| 4 | Open cart | Cart page loads |
| 5 | Review cart items | Both selected items are listed |
| 6 | Click **Checkout** | Checkout information page loads |
| 7 | Enter valid checkout info | Form accepts input |
| 8 | Click **Continue** | Checkout overview page loads |
| 9 | Review overview | Both items appear in summary |
| 10 | Click **Finish** | Order completes successfully |
| 11 | Verify confirmation | Order confirmation page is displayed |

## Expected Outcome
Two selected items persist from inventory to cart to checkout overview, and the order completes successfully.

---

# TC-003 — Locked-Out User Cannot Access Inventory

## Objective
Verify a locked-out user cannot log in or access protected application pages.

## Priority
**High**

## Preconditions
- User is on login page.

## Test Data
- Username: `locked_out_user`
- Password: `secret_sauce`

## Steps and Expected Results

| Step # | Action | Expected Result |
|---|---|---|
| 1 | Open the login page | Login page loads |
| 2 | Enter `locked_out_user` | Username field accepts input |
| 3 | Enter `secret_sauce` | Password field accepts input |
| 4 | Click **Login** | Login is rejected |
| 5 | Observe page state | User remains on login page |
| 6 | Review error message | Visible error message explains access failure |

## Expected Outcome
Locked-out user is denied access and inventory page does not load.

---

# TC-004 — Invalid Login Credentials Show Error

## Objective
Verify invalid credentials do not allow access and produce an error message.

## Priority
**High**

## Preconditions
- User is on login page.

## Test Data
- Username: `invalid_user`
- Password: `wrong_password`

## Steps and Expected Results

| Step # | Action | Expected Result |
|---|---|---|
| 1 | Open login page | Login page loads |
| 2 | Enter invalid username | Username field accepts input |
| 3 | Enter invalid password | Password field accepts input |
| 4 | Click **Login** | Authentication fails |
| 5 | Review page | User remains on login page |
| 6 | Verify visible message | Error message is displayed |

## Expected Outcome
Invalid credentials do not create a session and do not grant access to inventory.

---

# TC-005 — Add Item From Product Detail Page and Complete Checkout

## Objective
Verify the product detail page shows correct item details and supports add-to-cart through checkout completion.

## Priority
**High**

## Preconditions
- User can log in with valid credentials.

## Test Data
- Username: `standard_user`
- Password: `secret_sauce`

## Steps and Expected Results

| Step # | Action | Expected Result |
|---|---|---|
| 1 | Log in with valid credentials | Inventory page loads |
| 2 | Click a product name or image | Product detail page opens |
| 3 | Review product details | Name, description, and price are displayed |
| 4 | Click **Add to cart** | Item is added successfully |
| 5 | Verify cart badge | Cart badge displays `1` |
| 6 | Open cart | Cart page loads |
| 7 | Review cart | Same item appears in cart |
| 8 | Proceed to checkout | Checkout information page loads |
| 9 | Enter valid checkout info and continue | Checkout overview page loads |
| 10 | Click **Finish** | Order confirmation is shown |

## Expected Outcome
Item selected from product detail page remains consistent through cart and checkout.

---

# TC-006 — Remove Item, Continue Shopping, Add Another Item, Complete Checkout

## Objective
Verify the cart updates correctly after item removal and the user can continue shopping and purchase a different item.

## Priority
**Medium-High**

## Preconditions
- User is logged in.

## Steps and Expected Results

| Step # | Action | Expected Result |
|---|---|---|
| 1 | Log in with valid credentials | Inventory page loads |
| 2 | Add one item to cart | Item is added successfully |
| 3 | Open cart | Cart page loads |
| 4 | Verify the item is present | Added item is displayed |
| 5 | Click **Remove** | Item is removed from cart |
| 6 | Verify cart state | Removed item no longer appears |
| 7 | Click **Continue Shopping** | User returns to inventory page |
| 8 | Add a different item | New item is added to cart |
| 9 | Verify cart badge | Badge reflects current quantity |
| 10 | Open cart | Cart page loads |
| 11 | Review cart contents | Only new item is listed |
| 12 | Proceed through checkout | Checkout completes successfully |

## Expected Outcome
Cart state updates correctly after removal, continue shopping works, and checkout succeeds with the new item.

---

# TC-007 — Sort Products, Select Item, and Complete Checkout

## Objective
Verify sorting changes the visible product order and does not break selection or checkout flow.

## Priority
**Medium**

## Preconditions
- User is logged in.

## Steps and Expected Results

| Step # | Action | Expected Result |
|---|---|---|
| 1 | Log in with valid credentials | Inventory page loads |
| 2 | Observe current product order | Baseline order is visible |
| 3 | Change sort option | Product order updates |
| 4 | Verify displayed order changed | UI reflects selected sort mode |
| 5 | Add the first item shown after sorting | Selected item is added to cart |
| 6 | Verify cart badge | Cart badge displays `1` |
| 7 | Open cart | Cart page loads |
| 8 | Review cart item | Correct sorted item appears |
| 9 | Complete checkout | Checkout completes successfully |

## Expected Outcome
Sorting affects displayed order correctly, and selected items still flow properly into cart and checkout.

---

# TC-008 — Checkout Validation Blocks Missing Required Fields, Then Recovery Succeeds

## Objective
Verify checkout form validation prevents progress when required fields are blank, and that the flow succeeds after valid data is entered.

## Priority
**High**

## Preconditions
- User is logged in.
- At least one item is in the cart.

## Steps and Expected Results

| Step # | Action | Expected Result |
|---|---|---|
| 1 | Log in with valid credentials | Inventory page loads |
| 2 | Add one item to cart | Item is added successfully |
| 3 | Open cart and click **Checkout** | Checkout information page loads |
| 4 | Leave checkout fields blank | Form remains empty |
| 5 | Click **Continue** | Validation prevents progress |
| 6 | Review page | Error message is displayed and user remains on same page |
| 7 | Enter valid first name, last name, and postal code | Form accepts input |
| 8 | Click **Continue** again | Checkout overview page loads |
| 9 | Click **Finish** | Checkout completes |
| 10 | Verify confirmation | Order confirmation page is displayed |

## Expected Outcome
Blank required fields block progress; valid input allows recovery and successful completion.

---

# TC-009 — Cancel Checkout and Verify Cart State Remains Correct

## Objective
Verify cancelling checkout does not corrupt cart contents and the user can resume checkout successfully.

## Priority
**Medium**

## Preconditions
- User is logged in.
- At least one item is in cart.

## Steps and Expected Results

| Step # | Action | Expected Result |
|---|---|---|
| 1 | Log in with valid credentials | Inventory page loads |
| 2 | Add one item to cart | Item is added successfully |
| 3 | Open cart | Cart page loads |
| 4 | Click **Checkout** | Checkout information page loads |
| 5 | Click **Cancel** | User exits checkout step |
| 6 | Verify destination page | User is redirected appropriately |
| 7 | Review cart state | Previously added item is still available |
| 8 | Return to cart if needed | Cart remains usable |
| 9 | Restart checkout flow | Checkout information page loads again |
| 10 | Complete checkout | Order confirmation page is displayed |

## Expected Outcome
Cancel action exits checkout without losing cart state unexpectedly.

---

# TC-010 — Logout Ends Session and Blocks Continued Access

## Objective
Verify logout ends the authenticated session and protected areas are no longer usable without logging in again.

## Priority
**High**

## Preconditions
- User is logged in.

## Steps and Expected Results

| Step # | Action | Expected Result |
|---|---|---|
| 1 | Log in with valid credentials | Inventory page loads |
| 2 | Open application menu | Navigation menu is displayed |
| 3 | Click **Logout** | User is returned to login page |
| 4 | Verify login page | Login screen is visible |
| 5 | Attempt browser Back navigation | Protected access should not remain available as an active session |
| 6 | Attempt to revisit prior protected flow | Re-authentication should be required |

## Expected Outcome
Logout invalidates the active session and prevents continued use of protected pages.

---

## 6. Recommended First Automation Candidates

| Rank | TC ID | Reason |
|---|---|---|
| 1 | TC-001 | Core happy path with highest business value |
| 2 | TC-008 | Strong validation and recovery coverage |
| 3 | TC-003 | Important negative authentication scenario |
| 4 | TC-005 | Verifies data consistency across navigation layers |
| 5 | TC-010 | Covers logout and session handling |

---

## 7. Portfolio Notes

### Why this suite looks strong in a QA portfolio
- Covers both **positive and negative** scenarios
- Tests complete user journeys instead of isolated clicks
- Demonstrates awareness of **state transitions**, **validation**, **navigation**, and **session control**
- Provides a clear foundation for automation in Selenium, Playwright, or Cypress

### Good interview framing
You can describe this suite like this:

> I created a manual E2E test suite for SauceDemo focused on the highest-value user workflows: authentication, inventory browsing, product selection, cart behavior, checkout, validation, and session handling. I included both happy paths and negative paths so the suite would be useful not only for manual testing but also as a clean foundation for future UI automation.
