import os
from typing import List, Optional

from langchain.tools.base import BaseTool
from langchain_community.tools.playwright.click import ClickTool
from langchain_community.tools.playwright.current_page import CurrentWebPageTool
from langchain_community.tools.playwright.extract_hyperlinks import ExtractHyperlinksTool
from langchain_community.tools.playwright.extract_text import ExtractTextTool
from langchain_community.tools.playwright.get_elements import GetElementsTool
from langchain_community.tools.playwright.navigate import NavigateTool
from langchain_community.tools.playwright.navigate_back import NavigateBackTool

# カスタムユーティリティをインポート
from .playwright_utils import create_custom_sync_playwright_browser, get_current_page

def create_playwright_toolkit() -> List[BaseTool]:
    """Create a toolkit of Playwright tools for browser automation.
    
    Returns:
        List[BaseTool]: A list of Playwright tools for browser automation.
    """
    # カスタムブラウザを使用
    sync_browser = create_custom_sync_playwright_browser(headless=True, slow_mo=50)
    
    tools = [
        NavigateTool(sync_browser=sync_browser),
        NavigateBackTool(sync_browser=sync_browser),
        ClickTool(sync_browser=sync_browser),
        ExtractTextTool(sync_browser=sync_browser),
        ExtractHyperlinksTool(sync_browser=sync_browser),
        GetElementsTool(sync_browser=sync_browser),
        CurrentWebPageTool(sync_browser=sync_browser),
    ]
    
    print(f"Created {len(tools)} Playwright tools for browser automation.")
    return tools

def test_toolkit():
    """Test the Playwright toolkit by navigating to a website and extracting text."""
    tools = create_playwright_toolkit()
    
    print("Available tools:")
    for tool in tools:
        print(f"- {tool.name}: {tool.description}")
    
    navigate_tool = next((tool for tool in tools if "navigate" in tool.name.lower()), None)
    if navigate_tool:
        print("\nNavigating to example.com...")
        navigate_tool.run({"url": "https://example.com"})
        
        extract_text_tool = next((tool for tool in tools if "extract_text" in tool.name.lower() or "get_text" in tool.name.lower()), None)
        if extract_text_tool:
            print("Extracting text from the page...")
            text = extract_text_tool.run({})
            print("Extracted text:", text[:200] + "..." if len(text) > 200 else text)
        else:
            print("Extract text tool not found.")
        
        screenshot_tool = next((tool for tool in tools if "screenshot" in tool.name.lower()), None)
        if screenshot_tool:
            print("Taking a screenshot...")
            screenshot_path = screenshot_tool.run({})
            print(f"Screenshot saved to {screenshot_path}")
        else:
            print("Screenshot tool not found.")
    else:
        print("Navigate tool not found.")
    
    print("Toolkit test completed!")

if __name__ == "__main__":
    test_toolkit()
