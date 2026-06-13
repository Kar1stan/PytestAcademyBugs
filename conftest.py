import pytest

from playwright.sync_api import Playwright

disable_loggers = []


@pytest.fixture(scope='function')
def new_page(playwright: Playwright, request):
    browser_name = request.config.getoption('--browser_name')
    headless = False if request.config.getoption('--headed') else True
    if browser_name == 'chromium':
        browser = playwright.chromium.launch(headless=headless)
    if browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=headless)
    if browser_name == 'webkit':
        browser = playwright.webkit.launch(headless=headless)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.set_default_timeout(60000)  # 60 seconds
    page.set_default_navigation_timeout(60000) # Increase timeouts if page loads too long
    page.goto('https://academybugs.com/#')
    yield page
    browser.close()

# Fixture that launches the requested browser, opens the app page, yields the page to tests,
# and closes the browser when the test finishes.

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chromium')

# Adds a pytest CLI option for selecting browser type. Use `--browser_name=firefox` or
# `--browser_name=webkit` when running tests.
