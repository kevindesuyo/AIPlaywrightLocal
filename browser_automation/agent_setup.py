import os
from typing import List, Optional
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain_openai import ChatOpenAI
from langchain.tools.base import BaseTool

from env_setup import setup_environment
from langchain_setup import create_playwright_toolkit

def create_browser_agent(tools: List[BaseTool], verbose: bool = True):
    """Create a browser-operable agent using OpenAI GPT.
    
    Args:
        tools: List of tools to provide to the agent.
        verbose: Whether to print agent actions. Default is True.
        
    Returns:
        An initialized agent that can use the provided tools.
    """
    if not setup_environment():
        raise ValueError("Environment setup failed. Please check your .env file.")
    
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0125",
    )
    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=verbose,
        handle_parsing_errors=True,
    )
    
    print("Browser-operable agent created successfully!")
    return agent

def test_agent():
    """Test the browser-operable agent with a simple task."""
    tools = create_playwright_toolkit()
    
    agent = create_browser_agent(tools)
    
    print("\nTesting agent with a simple task...")
    result = agent.invoke({
        "input": "Navigate to example.com and tell me what the page is about."
    })
    
    print("\nAgent response:")
    print(result["output"])
    
    print("\nAgent test completed!")

if __name__ == "__main__":
    test_agent()
