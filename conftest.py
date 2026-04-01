import re
import time

import pytest

from api.base_api_client import BaseApiClient
from config.config import Config
from utils.driver_factory import DriverFactory


def _humanize_test_name(name):
    match = re.match(r"test_(?P<title>.+?)_(?P<case_id>TC_[A-Z]+_\d+)$", name)
    if match:
        title = match.group("title").replace("_", " ")
        case_id = match.group("case_id")
        return f"{title} [{case_id}]"

    return name.removeprefix("test_").replace("_", " ")


def _build_test_label(item):
    parts = item.nodeid.split("::")
    test_name = _humanize_test_name(parts[-1])

    if len(parts) > 2:
        return f"{parts[-2]} - {test_name}"

    return test_name


def pytest_sessionstart(session):
    print("\nStarting pytest run...", flush=True)


def pytest_collection_finish(session):
    total_tests = len(session.items)
    ui_tests = sum(1 for item in session.items if "ui" in item.keywords)
    api_tests = sum(1 for item in session.items if "api" in item.keywords)

    print(
        f"Collected {total_tests} tests ({ui_tests} UI, {api_tests} API).",
        flush=True,
    )
    session._progress_index = 0


def pytest_sessionfinish(session, exitstatus):
    print(f"Pytest run finished with exit code {exitstatus}.", flush=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(scope="function")
def progress_step():
    step_number = 0

    def _step(message):
        nonlocal step_number
        step_number += 1
        print(f"    Step {step_number}: {message}", flush=True)

    return _step


@pytest.fixture(scope="function", autouse=True)
def test_progress(request):
    session = request.session
    current_test = getattr(session, "_progress_index", 0) + 1
    session._progress_index = current_test
    total_tests = getattr(session, "testscollected", 0)
    test_label = _build_test_label(request.node)
    start_time = time.perf_counter()

    print(f"\n[TEST {current_test}/{total_tests}] Starting {test_label}", flush=True)

    yield

    duration = time.perf_counter() - start_time
    call_report = getattr(request.node, "rep_call", None)
    setup_report = getattr(request.node, "rep_setup", None)
    teardown_report = getattr(request.node, "rep_teardown", None)

    if call_report and call_report.failed:
        outcome = "FAILED"
    elif call_report and call_report.skipped:
        outcome = "SKIPPED"
    elif setup_report and setup_report.failed:
        outcome = "ERROR"
    elif teardown_report and teardown_report.failed:
        outcome = "ERROR"
    elif setup_report and setup_report.skipped:
        outcome = "SKIPPED"
    else:
        outcome = "PASSED"

    print(
        f"[TEST {current_test}/{total_tests}] {outcome} in {duration:.2f}s",
        flush=True,
    )


@pytest.fixture(scope="function")
def driver(progress_step):
    progress_step(f"Launch the {Config.BROWSER} browser.")
    browser = DriverFactory.get_driver(Config.BROWSER)
    yield browser
    print("\n    Cleanup: Close the browser.", flush=True)
    browser.quit()


@pytest.fixture(scope="function")
def api_client(progress_step):
    progress_step(f"Create an API session for {Config.API_BASE_URL}.")
    client = BaseApiClient()
    yield client
    print("\n    Cleanup: Close the API session.", flush=True)
    client.close_session()


@pytest.fixture(scope="function")
def setup(request, driver):
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
