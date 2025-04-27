"""
Browser Operation Flow

This module defines the browser operation flow for the automated browser operation tool.
It breaks down manual browser operations into detailed, step-by-step instructions.
"""

from typing import Dict, List, Optional, Any
import json

class BrowserOperation:
    """Base class for browser operations."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the operation to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "type": self.__class__.__name__
        }

class NavigateOperation(BrowserOperation):
    """Operation to navigate to a URL."""
    
    def __init__(self, url: str):
        super().__init__(
            name="Navigate",
            description=f"Navigate to {url}"
        )
        self.url = url
    
    def to_dict(self) -> Dict[str, Any]:
        result = super().to_dict()
        result["url"] = self.url
        return result

class SearchOperation(BrowserOperation):
    """Operation to enter a search keyword into a form."""
    
    def __init__(self, selector: str, keyword: str):
        super().__init__(
            name="Search",
            description=f"Enter '{keyword}' into {selector}"
        )
        self.selector = selector
        self.keyword = keyword
    
    def to_dict(self) -> Dict[str, Any]:
        result = super().to_dict()
        result["selector"] = self.selector
        result["keyword"] = self.keyword
        return result

class ClickOperation(BrowserOperation):
    """Operation to click on an element."""
    
    def __init__(self, selector: str, description: Optional[str] = None):
        desc = description or f"Click on element matching '{selector}'"
        super().__init__(
            name="Click",
            description=desc
        )
        self.selector = selector
    
    def to_dict(self) -> Dict[str, Any]:
        result = super().to_dict()
        result["selector"] = self.selector
        return result

class ExtractOperation(BrowserOperation):
    """Operation to extract content from the page."""
    
    def __init__(self, selector: Optional[str] = None):
        desc = "Extract content from the entire page"
        if selector:
            desc = f"Extract content from elements matching '{selector}'"
        
        super().__init__(
            name="Extract",
            description=desc
        )
        self.selector = selector
    
    def to_dict(self) -> Dict[str, Any]:
        result = super().to_dict()
        if self.selector:
            result["selector"] = self.selector
        return result

class FilterOperation(BrowserOperation):
    """Operation to filter extracted information."""
    
    def __init__(self, criteria: str):
        super().__init__(
            name="Filter",
            description=f"Filter information using criteria: {criteria}"
        )
        self.criteria = criteria
    
    def to_dict(self) -> Dict[str, Any]:
        result = super().to_dict()
        result["criteria"] = self.criteria
        return result

class BrowserFlow:
    """A sequence of browser operations forming a complete flow."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.operations: List[BrowserOperation] = []
    
    def add_operation(self, operation: BrowserOperation) -> None:
        """Add an operation to the flow."""
        self.operations.append(operation)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the flow to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "operations": [op.to_dict() for op in self.operations]
        }
    
    def to_json(self, indent: int = 2) -> str:
        """Convert the flow to a JSON string."""
        return json.dumps(self.to_dict(), indent=indent)

def create_example_flow() -> BrowserFlow:
    """Create an example browser operation flow."""
    flow = BrowserFlow(
        name="Example Search and Extract Flow",
        description="Access a website, search for a keyword, click a link, and extract content"
    )
    
    flow.add_operation(NavigateOperation(url="{WEBSITE_URL}"))
    
    flow.add_operation(SearchOperation(
        selector="{SEARCH_FORM_SELECTOR}",
        keyword="{SEARCH_KEYWORD}"
    ))
    
    flow.add_operation(ClickOperation(
        selector="{SELECTOR_FOR_FIRST_LINK}",
        description="Click the first search result link"
    ))
    
    flow.add_operation(ExtractOperation())
    
    flow.add_operation(FilterOperation(criteria="{FILTERING_CRITERIA}"))
    
    return flow

def create_google_search_flow(keyword: str) -> BrowserFlow:
    """Create a flow for searching on Google and extracting results."""
    flow = BrowserFlow(
        name=f"Google Search for '{keyword}'",
        description=f"Search Google for '{keyword}' and extract the first result"
    )
    
    flow.add_operation(NavigateOperation(url="https://www.google.com"))
    
    flow.add_operation(SearchOperation(
        selector="input[name='q']",
        keyword=keyword
    ))
    
    flow.add_operation(ClickOperation(
        selector="input[name='btnK']",
        description="Click the Google Search button"
    ))
    
    flow.add_operation(ClickOperation(
        selector=".g a",
        description="Click the first search result link"
    ))
    
    flow.add_operation(ExtractOperation())
    
    return flow

if __name__ == "__main__":
    example_flow = create_example_flow()
    print("Example Flow:")
    print(example_flow.to_json())
    print()
    
    google_flow = create_google_search_flow("LangChain Playwright tutorial")
    print("Google Search Flow:")
    print(google_flow.to_json())
