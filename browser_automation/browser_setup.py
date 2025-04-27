import asyncio
from playwright.async_api import async_playwright

async def initialize_browser(headless=True):
    """Initialize a Playwright browser.
    
    Args:
        headless (bool): Whether to run browser in headless mode. Default is True.
    """
    print(f"Initializing Playwright browser (headless={headless})...")
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=headless)
    context = await browser.new_context()
    page = await context.new_page()
    
    print("Browser initialized successfully!")
    return playwright, browser, context, page

async def close_browser(playwright, browser):
    """Close the browser and playwright instance."""
    await browser.close()
    await playwright.stop()
    print("Browser closed successfully.")

async def test_browser():
    """Test the browser by navigating to a website."""
    playwright, browser, context, page = await initialize_browser(headless=True)
    
    try:
        print("Navigating to example.com...")
        await page.goto("https://example.com")
        print("Page title:", await page.title())
        
        print("Taking a screenshot...")
        await page.screenshot(path="example_screenshot.png")
        print("Screenshot saved as example_screenshot.png")
        
    finally:
        await close_browser(playwright, browser)

if __name__ == "__main__":
    asyncio.run(test_browser())
