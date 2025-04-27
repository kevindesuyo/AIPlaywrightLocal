"""
Custom Playwright utilities for browser automation

This module provides custom utilities for Playwright browser automation,
specifically designed to work with Python 3.12+ and the latest versions of Playwright.
"""

from typing import Any, Optional
from playwright.sync_api import sync_playwright

def create_custom_sync_playwright_browser(
    headless: bool = False,  # デバッグのためデフォルトをFalseに
    slow_mo: Optional[int] = None,
) -> Any:
    """Create a synchronous Playwright browser with custom options.
    
    Args:
        headless: Whether to run browser in headless mode. Default is False for debug.
        slow_mo: Slow down operations by the specified amount of milliseconds. Default is None.
        
    Returns:
        A synchronous Playwright browser instance.
    """
    print(f"Creating custom sync Playwright browser (headless={headless})...")
    
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=headless,
        slow_mo=slow_mo,
    )
    context = browser.new_context()
    page = context.new_page()
    browser.playwright = playwright
    browser.context = context
    browser.page = page
    print("Custom sync Playwright browser created successfully!")
    return browser

def get_current_page(browser: Any) -> Any:
    return browser.page

def close_sync_browser(browser: Any) -> None:
    browser.close()
    browser.playwright.stop()
    print("Browser closed successfully.")

def test_custom_browser():
    try:
        browser = create_custom_sync_playwright_browser(headless=False)
        try:
            page = get_current_page(browser)
            print("Navigating to example.com...")
            page.goto("https://example.com")
            print("Page title:", page.title())
            print("Taking a screenshot...")
            page.screenshot(path="example_screenshot.png")
            print("Screenshot saved as example_screenshot.png")
        finally:
            close_sync_browser(browser)
        print("Custom browser test completed!")
    except Exception as e:
        print(f"Error during browser test: {str(e)}")

if __name__ == "__main__":
    test_custom_browser()
