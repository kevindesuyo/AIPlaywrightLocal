"""
Streamlit UI for Browser Automation

This module provides a simple web UI using Streamlit that allows users to enter
browser operation instructions and submit them for processing by the browser-operable agent.
"""

import os
import streamlit as st
from dotenv import load_dotenv

from langchain_setup import create_playwright_toolkit
from custom_tools import create_custom_tools
from agent_setup import create_browser_agent

load_dotenv()

st.set_page_config(
    page_title="Browser Automation Tool",
    page_icon="🌐",
    layout="wide"
)

def main():
    """Main function to run the Streamlit app."""
    
    st.title("🌐 Browser Automation Tool")
    st.markdown("""
    This tool uses LangChain and Playwright to automate browser operations based on your instructions.
    Enter your instructions below and click 'Run Automation' to execute them.
    """)
    
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key or openai_api_key == "your_openai_api_key_here":
        st.warning(
            "⚠️ OpenAI API key not found. Please set your API key in the .env file or enter it below."
        )
        openai_api_key = st.text_input("OpenAI API Key", type="password")
        if openai_api_key:
            os.environ["OPENAI_API_KEY"] = openai_api_key
    
    st.header("Browser Operation Instructions")
    
    with st.expander("See example instructions"):
        st.markdown("""
        **Example 1:** Go to google.com, search for "LangChain tutorials", and tell me the title of the first result.
        
        **Example 2:** Navigate to wikipedia.org, search for "Artificial Intelligence", go to the article, and summarize the first paragraph.
        
        **Example 3:** Go to news.ycombinator.com and tell me the titles of the top 5 stories.
        """)
    
    user_instruction = st.text_area(
        "Enter your instructions here",
        height=150,
        placeholder="E.g., Go to google.com, search for 'LangChain tutorials', and tell me the title of the first result."
    )
    
    with st.expander("Advanced Options"):
        verbose = st.checkbox("Show detailed agent steps", value=True)
        max_iterations = st.slider("Maximum iterations", min_value=1, max_value=20, value=10)
    
    if st.button("Run Automation", type="primary"):
        if not user_instruction:
            st.error("Please enter instructions before running the automation.")
            return
        
        if not openai_api_key or openai_api_key == "your_openai_api_key_here":
            st.error("Please provide a valid OpenAI API key.")
            return
        
        with st.spinner("Running browser automation..."):
            try:
                standard_tools = create_playwright_toolkit()
                custom_tools = create_custom_tools()
                all_tools = standard_tools + custom_tools
                
                agent = create_browser_agent(all_tools, verbose=verbose)
                
                result = agent.invoke({
                    "input": user_instruction
                })
                
                st.success("Automation completed successfully!")
                st.subheader("Result")
                st.write(result["output"])
                
                screenshot_files = [f for f in os.listdir() if f.endswith('.png') and f.startswith('screenshot')]
                if screenshot_files:
                    st.subheader("Screenshots")
                    for screenshot in screenshot_files:
                        st.image(screenshot, caption=screenshot)
                
            except Exception as e:
                st.error(f"An error occurred during automation: {str(e)}")
    
    st.markdown("---")
    st.markdown(
        "Built with ❤️ using LangChain, Playwright, and Streamlit"
    )

if __name__ == "__main__":
    main()
