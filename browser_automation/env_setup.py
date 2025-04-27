import os
from dotenv import load_dotenv

def setup_environment():
    """Load environment variables from .env file and verify they are set."""
    load_dotenv()
    
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key or openai_api_key == "your_openai_api_key_here":
        print("Warning: OPENAI_API_KEY is not set or is using the default placeholder value.")
        print("Please update the .env file with your actual OpenAI API key.")
        return False
    
    print("Environment variables loaded successfully.")
    return True

if __name__ == "__main__":
    setup_environment()
