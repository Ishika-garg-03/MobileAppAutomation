import datetime
import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pytest_metadata.plugin import metadata_key
from pages.variables.device_variables import *
from utilities.report_mail import send_report
from utilities.logger import setup_logger, get_appium_logs

logger = setup_logger()


@pytest.fixture(scope="session")
def appium_driver():
    desired_caps = dict(
        platformName=platform_name,
        automationName=automation_name,
        deviceID=deviceID,
        platformVersion=platform_version,
    )
    global driver
    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def pytest_html_report_title(report):
    report.title = "Test Report"


def pytest_configure(config):
    config.stash[metadata_key]["foo"] = "bar"


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["Project"] = "Amazon App testing"


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if hasattr(item, "log_capture"):
        logs = item.log_capture.getvalue()
        if logs:
            item.add_report_section("call", "Logs", logs)


@pytest.fixture(autouse=True)
def attach_logs(request):
    if hasattr(request.node, "log_capture"):
        request.node.log_capture = request.node.funcargs.get("log_capture")


@pytest.fixture(scope="session", autouse=True)
def capture_appium_logs():
    logger.info("Starting Appium log capture...")
    logs_start = get_appium_logs()
    logger.info(f"Appium Logs at Start:\n{logs_start}")
    yield
    logs_end = get_appium_logs()
    logger.info(f"Appium Logs at End:\n{logs_end}")


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>BDD Scenario Steps</th>")  # Add a new column header


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_row(report, cells):
    description = "N/A"  # Default value

    # Check if 'scenario' info exists
    scenario_data = getattr(report, "scenario", None)

    if isinstance(scenario_data, dict) and "steps" in scenario_data:
        steps = "\n".join([step["keyword"] + " " + step["name"] for step in scenario_data["steps"]])
        description = steps  # Only include Given, When, Then
    cells.insert(2, f"<td>{description.replace('\n', '<br>')}</td>")  # Format for HTML report


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if config.option.htmlpath:
        if not os.path.exists('reports'):
            os.makedirs('reports')
        global html_report
        html_report = 'reports/' + datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
        config.option.htmlpath = html_report


@pytest.hookimpl(tryfirst=True)
def pytest_unconfigure(config):
    if config.option.htmlpath:
        if html_report:
            send_report(html_report)
            print("Report Sent")
    else:
        print("No report file path found.")

# #@pytest.hookimpl()
# def pytest_unconfigure(config):
#     html_report = config.option.htmlpath
#     send_report(html_report)
#     print("Report sent")
