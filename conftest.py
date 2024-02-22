import pytest
from base.const import *
from playwright.sync_api import Browser


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="master", help="Choose environment: master, prod or qa")
    parser.addoption("--launch_type", action="store", default="headed", help="Choose launch_type: headed or headless")


@pytest.fixture(scope="session")
def base_url(request):
    base_url = request.config.getoption("base_url")
    if base_url == "prod":
        return prod_url
    else:
        raise pytest.UsageError("--base_url should be master or prod")


@pytest.fixture(scope="session")
def launch_type(request):
    launch_type = request.config.getoption("launch_type")
    if launch_type == "headed":
        return False
    elif launch_type == "headless":
        return True
    else:
        raise pytest.UsageError("--launch_type should be headed or headless")


@pytest.fixture
def test_name(request):
    return request.node.name


@pytest.fixture(scope="function")
def page_logged_out(base_url, browser_type: Browser, launch_type, test_name):
    browser = browser_type.launch(headless=launch_type)
    context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=f"test-results/{test_name}.zip")
    page.close()
    context.close()
    browser.close()