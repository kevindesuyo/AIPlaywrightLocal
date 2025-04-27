"""
Main entry point for the Browser Automation Tool

This script serves as the main entry point for the Browser Automation Tool.
It provides a simple command-line interface to run the Streamlit app.
"""

import os
import subprocess
import sys

def check_environment():
    """Check if the environment is properly set up."""
    # Python version compatibility check
    if sys.version_info >= (3, 12):
        print("Error: Python 3.12+ is not supported due to dependency compatibility issues. Please use Python 3.11 or earlier.")
        return False

    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Warning: Virtual environment is not activated. Make sure all dependencies are installed.")
        # Proceed without requiring virtual environment
     
    try:
        import streamlit
        import langchain
        import playwright
        import dotenv
    except ImportError as e:
        print(f"Error: Required package not installed - {e}")
        print("Please install the required packages before running the app.")
        print("Run: pip install -r requirements.txt")
        return False
    
    from dotenv import load_dotenv
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key or openai_api_key == "your_openai_api_key_here":
        print("Warning: OpenAI API key is not set.")
        print("You will need to provide your API key in the Streamlit app.")
    
    return True

def run_streamlit_app():
    """Run the Streamlit app."""
    print("Starting the Browser Automation Tool...")
    subprocess.run(["streamlit", "run", "streamlit_app.py"])

def main():
    """Main function to run the app."""
    print("Browser Automation Tool")
    print("======================")
    
    if not check_environment():
        print("\nEnvironment check failed. Please fix the issues before running the app.")
        return
    
    print("\nEnvironment check passed. Starting the app...")
    run_streamlit_app()

if __name__ == "__main__":
    main()
