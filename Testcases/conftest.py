import pytest
from selenium import webdriver
from pytest import hookimpl
import os

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser name to execute tests on"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    try:
        if browser_name == "chrome":
            driver = webdriver.Chrome()
        elif browser_name == "safari":
            driver = webdriver.Safari()
        elif browser_name == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
    except Exception as e:
        raise RuntimeError(f"Failed to initialize browser: {e}")

    driver.implicitly_wait(20)
    driver.get("https://organicsmantra.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

@hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Extends the PyTest Plugin to take and embed screenshot in HTML report, whenever a test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extras", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get("setup")  # Retrieve the driver instance from the fixture
            if driver:
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(driver, file_name)
                if file_name:
                    html = (
                        '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    )
                    extra.append(pytest_html.extras.html(html))
    report.extras = extra

def _capture_screenshot(driver, name):
    screenshots_dir = "/Users/riyabakoria/OrganixmantraAPP/.pytest_cache/Screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    file_path = os.path.join(screenshots_dir, name)
    driver.get_screenshot_as_file(file_path)
