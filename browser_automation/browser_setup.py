import asyncio
import os
import sys
import platform
import tempfile
from pathlib import Path
from playwright.async_api import async_playwright

def get_browser_data_dir():
    """Get a platform-specific directory for browser data.
    
    Returns:
        Path: Path to the browser data directory
    """
    if platform.system() == "Darwin":  # macOS
        base_dir = Path.home() / "Library" / "Application Support" / "AIPlaywrightLocal"
    elif platform.system() == "Windows":
        base_dir = Path(os.environ.get("APPDATA", "")) / "AIPlaywrightLocal"
    else:  # Linux and others
        base_dir = Path.home() / ".config" / "AIPlaywrightLocal"
    
    os.makedirs(base_dir, exist_ok=True)
    
    print(f"Using browser data directory: {base_dir}")
    return str(base_dir)

def get_screenshot_dir():
    """Get a platform-specific directory for screenshots.
    
    Returns:
        Path: Path to the screenshots directory
    """
    if platform.system() == "Darwin":  # macOS
        base_dir = Path.home() / "Pictures" / "AIPlaywrightScreenshots"
    elif platform.system() == "Windows":
        base_dir = Path.home() / "Pictures" / "AIPlaywrightScreenshots"
    else:  # Linux and others
        base_dir = Path.home() / "Pictures" / "AIPlaywrightScreenshots"
    
    os.makedirs(base_dir, exist_ok=True)
    
    print(f"Using screenshot directory: {base_dir}")
    return str(base_dir)

async def initialize_browser(headless=True):
    """Initialize a Playwright browser.
    
    Args:
        headless (bool): Whether to run browser in headless mode. Default is True.
    """
    print(f"Initializing Playwright browser (headless={headless})...")
    
    user_data_dir = get_browser_data_dir()
    
    launch_options = {
        "headless": headless,
    }
    
    if platform.system() == "Darwin":  # macOS
        print("Detected macOS platform, applying Mac-specific browser options...")
        launch_options.update({
            "chromium_sandbox": False,  # Equivalent to --no-sandbox
            "user_data_dir": user_data_dir,  # Set user data directory
        })
    
    try:
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(**launch_options)
        
        context_options = {}
        
        if platform.system() == "Darwin":
            pass
            
        context = await browser.new_context(**context_options)
        page = await context.new_page()
        
        print("Browser initialized successfully!")
        return playwright, browser, context, page
    except Exception as e:
        print(f"Error initializing browser: {str(e)}")
        if platform.system() == "Darwin":
            print("Mac-specific troubleshooting tips:")
            print("- Make sure Chromium is installed: python -m playwright install chromium")
            print("- Check permissions for browser data directory")
            print("- Try running with --no-sandbox option")
            print("- If using M1/M2 Mac, ensure Rosetta 2 is installed for x86 compatibility")
        raise

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
        
        screenshot_dir = get_screenshot_dir()
        screenshot_path = Path(screenshot_dir) / "example_screenshot.png"
        
        print(f"Taking a screenshot and saving to {screenshot_path}...")
        await page.screenshot(path=str(screenshot_path))
        print(f"Screenshot saved as {screenshot_path}")
        
    except Exception as e:
        print(f"Error during browser test: {str(e)}")
        if platform.system() == "Darwin":
            print("Mac-specific troubleshooting tips:")
            print("- Check network connectivity")
            print("- Verify Chromium installation: python -m playwright install chromium")
            print("- Check permissions for screenshot directory")
        raise
    finally:
        await close_browser(playwright, browser)

if __name__ == "__main__":
    asyncio.run(test_browser())
