import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser

@pytest.fixture(scope="function")
def page(browser):

        browser_context = browser.new_context(no_viewport=True)
        new_page = browser_context.new_page()

        yield new_page

        # 测试结束后清理资源
        new_page.close()
        browser_context.close()
