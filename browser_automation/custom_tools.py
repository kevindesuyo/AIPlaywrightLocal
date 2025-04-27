"""
Custom Tools for Extended Browser Operations

This module defines custom tools for operations not supported by LangChain's standard Playwright tools,
such as entering text into a form, waiting for and clicking a selector, etc.
"""

from typing import Dict, Any, Optional, Type
from langchain.tools.base import BaseTool, ToolException

# カスタムユーティリティをインポート
from .playwright_utils import create_custom_sync_playwright_browser, get_current_page

class FormInputTool(BaseTool):
    """Tool to enter text into a form field."""
    
    name: str = "form_input"
    description: str = "Enter text into a form field with the given selector"
    sync_browser: Any = None
    
    def __init__(self, sync_browser=None):
        """Initialize the tool with a synchronous browser instance."""
        super().__init__()
        self.sync_browser = sync_browser or create_custom_sync_playwright_browser()
    
    def _run(self, selector: str, text: str) -> str:
        """Run the tool to enter text into a form field.
        
        Args:
            selector: CSS selector for the form field
            text: Text to enter into the form field
            
        Returns:
            A message indicating success or failure
        """
        try:
            page = get_current_page(self.sync_browser)
            page.fill(selector, text)
            return f"Successfully entered text into form field with selector '{selector}'"
        except Exception as e:
            raise ToolException(f"Error entering text into form field: {str(e)}")
    
    def args_schema(self) -> Type[Dict[str, Any]]:
        """Define the arguments schema for the tool."""
        from pydantic import BaseModel, Field
        
        class FormInputArgs(BaseModel):
            selector: str = Field(..., description="CSS selector for the form field")
            text: str = Field(..., description="Text to enter into the form field")
        
        return FormInputArgs

class WaitAndClickTool(BaseTool):
    """Tool to wait for an element to be visible and then click it."""
    
    name: str = "wait_and_click"
    description: str = "Wait for an element with the given selector to be visible and then click it"
    sync_browser: Any = None
    
    def __init__(self, sync_browser=None):
        """Initialize the tool with a synchronous browser instance."""
        super().__init__()
        self.sync_browser = sync_browser or create_custom_sync_playwright_browser()
    
    def _run(self, selector: str, timeout: int = 30000) -> str:
        """Run the tool to wait for and click an element.
        
        Args:
            selector: CSS selector for the element to click
            timeout: Maximum time to wait for the element in milliseconds
            
        Returns:
            A message indicating success or failure
        """
        try:
            page = get_current_page(self.sync_browser)
            page.wait_for_selector(selector, timeout=timeout)
            page.click(selector)
            return f"Successfully waited for and clicked element with selector '{selector}'"
        except Exception as e:
            raise ToolException(f"Error waiting for or clicking element: {str(e)}")
    
    def args_schema(self) -> Type[Dict[str, Any]]:
        """Define the arguments schema for the tool."""
        from pydantic import BaseModel, Field
        
        class WaitAndClickArgs(BaseModel):
            selector: str = Field(..., description="CSS selector for the element to click")
            timeout: int = Field(30000, description="Maximum time to wait for the element in milliseconds")
        
        return WaitAndClickArgs

class WaitForNavigationTool(BaseTool):
    """Tool to wait for navigation to complete after an action."""
    
    name: str = "wait_for_navigation"
    description: str = "Wait for navigation to complete after performing an action"
    sync_browser: Any = None
    
    def __init__(self, sync_browser=None):
        """Initialize the tool with a synchronous browser instance."""
        super().__init__()
        self.sync_browser = sync_browser or create_custom_sync_playwright_browser()
    
    def _run(self, action_description: str, timeout: int = 30000) -> str:
        """Run the tool to wait for navigation to complete.
        
        Args:
            action_description: Description of the action that triggered navigation
            timeout: Maximum time to wait for navigation in milliseconds
            
        Returns:
            A message indicating success or failure
        """
        try:
            page = get_current_page(self.sync_browser)
            with page.expect_navigation(timeout=timeout):
                return f"Successfully waited for navigation to complete after {action_description}"
        except Exception as e:
            raise ToolException(f"Error waiting for navigation: {str(e)}")
    
    def args_schema(self) -> Type[Dict[str, Any]]:
        """Define the arguments schema for the tool."""
        from pydantic import BaseModel, Field
        
        class WaitForNavigationArgs(BaseModel):
            action_description: str = Field(..., description="Description of the action that triggered navigation")
            timeout: int = Field(30000, description="Maximum time to wait for navigation in milliseconds")
        
        return WaitForNavigationArgs

class SelectDropdownOptionTool(BaseTool):
    """Tool to select an option from a dropdown menu."""
    
    name: str = "select_dropdown_option"
    description: str = "Select an option from a dropdown menu with the given selector"
    sync_browser: Any = None
    
    def __init__(self, sync_browser=None):
        """Initialize the tool with a synchronous browser instance."""
        super().__init__()
        self.sync_browser = sync_browser or create_custom_sync_playwright_browser()
    
    def _run(self, selector: str, value: str, label: Optional[str] = None) -> str:
        """Run the tool to select an option from a dropdown menu.
        
        Args:
            selector: CSS selector for the dropdown menu
            value: Value of the option to select
            label: Optional label of the option to select (used if value is not provided)
            
        Returns:
            A message indicating success or failure
        """
        try:
            page = get_current_page(self.sync_browser)
            if label:
                page.select_option(selector, label=label)
                return f"Successfully selected option with label '{label}' from dropdown with selector '{selector}'"
            else:
                page.select_option(selector, value=value)
                return f"Successfully selected option with value '{value}' from dropdown with selector '{selector}'"
        except Exception as e:
            raise ToolException(f"Error selecting option from dropdown: {str(e)}")
    
    def args_schema(self) -> Type[Dict[str, Any]]:
        """Define the arguments schema for the tool."""
        from pydantic import BaseModel, Field
        
        class SelectDropdownOptionArgs(BaseModel):
            selector: str = Field(..., description="CSS selector for the dropdown menu")
            value: str = Field(..., description="Value of the option to select")
            label: Optional[str] = Field(None, description="Optional label of the option to select (used if value is not provided)")
        
        return SelectDropdownOptionArgs

class SubmitFormTool(BaseTool):
    """Tool to submit a form."""
    
    name: str = "submit_form"
    description: str = "Submit a form with the given selector"
    sync_browser: Any = None
    
    def __init__(self, sync_browser=None):
        """Initialize the tool with a synchronous browser instance."""
        super().__init__()
        self.sync_browser = sync_browser or create_custom_sync_playwright_browser()
    
    def _run(self, selector: str) -> str:
        """Run the tool to submit a form.
        
        Args:
            selector: CSS selector for the form
            
        Returns:
            A message indicating success or failure
        """
        try:
            page = get_current_page(self.sync_browser)
            with page.expect_navigation():
                page.evaluate(f"document.querySelector('{selector}').submit()")
            return f"Successfully submitted form with selector '{selector}'"
        except Exception as e:
            raise ToolException(f"Error submitting form: {str(e)}")
    
    def args_schema(self) -> Type[Dict[str, Any]]:
        """Define the arguments schema for the tool."""
        from pydantic import BaseModel, Field
        
        class SubmitFormArgs(BaseModel):
            selector: str = Field(..., description="CSS selector for the form")
        
        return SubmitFormArgs

def create_custom_tools(sync_browser=None):
    """Create a list of custom tools for extended browser operations.
    
    Args:
        sync_browser: Optional synchronous browser instance to use for the tools
        
    Returns:
        A list of custom tools
    """
    browser = sync_browser or create_custom_sync_playwright_browser()
    
    tools = [
        FormInputTool(sync_browser=browser),
        WaitAndClickTool(sync_browser=browser),
        WaitForNavigationTool(sync_browser=browser),
        SelectDropdownOptionTool(sync_browser=browser),
        SubmitFormTool(sync_browser=browser),
    ]
    
    print(f"Created {len(tools)} custom tools for extended browser operations.")
    return tools

def test_custom_tools():
    """Test the custom tools by printing their descriptions."""
    tools = create_custom_tools()
    
    print("Available custom tools:")
    for tool in tools:
        print(f"- {tool.name}: {tool.description}")
    
    print("\nCustom tools test completed!")

if __name__ == "__main__":
    test_custom_tools()
