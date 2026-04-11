# API Testing Scope: JSONPlaceholder Posts

![API](https://img.shields.io/badge/API-REST-2D6CDF)
![Coverage](https://img.shields.io/badge/Automated%20Checks-4-2EA44F)
![Client](https://img.shields.io/badge/Client-requests-555555)

Focused REST API coverage for the JSONPlaceholder `/posts` resource, built to show clean request handling, response validation, and reusable client structure.

## 📌 At A Glance

| Item | Details |
|---|---|
| API under test | `http://jsonplaceholder.typicode.com/posts` |
| Automated test file | [`tests/api/test_posts_api.py`](../tests/api/test_posts_api.py) |
| Reusable client | [`api/base_api_client.py`](../api/base_api_client.py) |
| Test runner | Pytest |
| Marker | `api` |

## 🧪 Automated Coverage

| Signal | Test | Request | What It Proves |
|---|---|---|---|
| Read collection | `test_get_all_posts` | `GET /posts` | Endpoint returns a usable list with expected post fields |
| Read item | `test_get_single_post` | `GET /posts/1` | A specific resource can be retrieved and validated by ID |
| Create | `test_create_post` | `POST /posts` | Request payload is accepted and echoed in the created resource |
| Delete | `test_delete_post` | `DELETE /posts/1` | Delete operation returns a successful response and empty body |

## ✅ Assertion Focus

| Layer | Examples |
|---|---|
| Status codes | `200`, `201` |
| Response shape | list vs. object payloads |
| Required fields | `userId`, `id`, `title`, `body` |
| Payload consistency | created post echoes submitted `title`, `body`, and `userId` |
| Response body rules | delete response returns `{}` |

## 🚀 Execution

Run only API tests:

```bash
pytest -m api
```

Run the full UI and API suite:

```bash
pytest -m "ui or api"
```

On PowerShell, force headless mode for the full suite:

```powershell
$env:HEADLESS="True"; pytest -m "ui or api"
```

## 📝 Portfolio Notes

- JSONPlaceholder is used as a stable public REST API for demonstration.
- The framework keeps request logic in a reusable client instead of duplicating HTTP setup inside each test.
- The manual workbook tracks broader future API scenarios under `TC_API_001` through `TC_API_008`.
- This scope is intentionally small but complete enough to demonstrate GET, POST, DELETE, fixture usage, and response validation.
