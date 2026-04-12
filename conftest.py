import os
import re
import time
from pathlib import Path

import pytest

from api.base_api_client import BaseApiClient
from config.config import Config
from utils.driver_factory import DriverFactory

try:
    import allure
    from allure_commons.types import AttachmentType
except ImportError:
    allure = None
    AttachmentType = None

try:
    from pytest_metadata.plugin import metadata_key
except ImportError:
    metadata_key = None


SUPPORTED_BROWSERS = ("chrome", "firefox")


def _default_browser():
    browser = Config.BROWSER.lower()
    return browser if browser in SUPPORTED_BROWSERS else "chrome"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=_default_browser(),
        choices=SUPPORTED_BROWSERS,
        help="Browser to use for UI tests. Overrides BROWSER. Supported values: chrome, firefox.",
    )


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


def _safe_file_name(value):
    return re.sub(r"[^\w.-]+", "_", value)


def _get_driver_from_item(item):
    driver = item.funcargs.get("driver")
    if driver is not None:
        return driver

    setup_driver = item.funcargs.get("setup")
    if setup_driver is not None:
        return setup_driver

    test_instance = getattr(item, "instance", None)
    return getattr(test_instance, "driver", None)


def _get_failure_artifacts_dir(config):
    html_path = getattr(config.option, "htmlpath", None)
    if html_path:
        return Path(html_path).parent / "screenshots"

    return Path(Config.SCREENSHOT_PATH) / "failures"


def _capture_failure_screenshot(item, report):
    driver = _get_driver_from_item(item)
    if driver is None:
        return None

    screenshot_dir = _get_failure_artifacts_dir(item.config)
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    screenshot_path = screenshot_dir / f"{_safe_file_name(item.nodeid)}_{report.when}.png"

    try:
        saved = driver.save_screenshot(str(screenshot_path))
    except Exception as exc:
        report.sections.append(("reporting", f"Could not capture screenshot: {exc}"))
        return None

    if not saved:
        report.sections.append(("reporting", "WebDriver did not save a failure screenshot."))
        return None

    return screenshot_path


def _relative_to_html_report(config, target_path):
    html_path = getattr(config.option, "htmlpath", None)
    if not html_path:
        return target_path.as_posix()

    report_dir = Path(html_path).parent
    return os.path.relpath(target_path, report_dir).replace("\\", "/")


def _add_pytest_html_extras(item, report, screenshot_path):
    pytest_html = item.config.pluginmanager.getplugin("html")
    if pytest_html is None or screenshot_path is None:
        return

    extras = getattr(report, "extras", [])
    extras.append(
        pytest_html.extras.url(
            _relative_to_html_report(item.config, screenshot_path),
            name="Failure screenshot",
        )
    )
    report.extras = extras


def _add_allure_attachment(item, screenshot_path):
    if screenshot_path is None or allure is None or AttachmentType is None:
        return

    if not item.config.pluginmanager.hasplugin("allure_pytest"):
        return

    allure.attach.file(
        str(screenshot_path),
        name=f"{item.name} failure screenshot",
        attachment_type=AttachmentType.PNG,
    )


def _ensure_report_directories(config):
    for option_name in ("htmlpath", "json_report_file"):
        option_value = getattr(config.option, option_name, None)
        if option_value:
            Path(option_value).parent.mkdir(parents=True, exist_ok=True)

    for option_name in ("allure_report_dir", "alluredir"):
        option_value = getattr(config.option, option_name, None)
        if option_value:
            Path(option_value).mkdir(parents=True, exist_ok=True)


def _set_report_metadata(config):
    metadata = None

    if metadata_key is not None and hasattr(config, "stash"):
        try:
            metadata = config.stash[metadata_key]
        except KeyError:
            metadata = {}
            config.stash[metadata_key] = metadata
    elif hasattr(config, "_metadata"):
        metadata = config._metadata

    if metadata is None:
        return

    metadata["Browser"] = config.getoption("browser")
    metadata["Headless"] = str(Config.HEADLESS)
    metadata["UI Base URL"] = os.getenv("BASE_URL", Config.BASE_URL)
    metadata["API Base URL"] = Config.API_BASE_URL


def pytest_configure(config):
    _ensure_report_directories(config)
    _set_report_metadata(config)


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "QA Automation Framework Test Report"


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

    if report.when == "call" and report.failed:
        screenshot_path = _capture_failure_screenshot(item, report)
        _add_pytest_html_extras(item, report, screenshot_path)
        _add_allure_attachment(item, screenshot_path)


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
def driver(request, progress_step):
    selected_browser = request.config.getoption("browser")
    progress_step(f"Launch the {selected_browser} browser.")
    browser = DriverFactory.get_driver(selected_browser)
    try:
        yield browser
    finally:
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
