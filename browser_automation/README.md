# Browser Automation Tool

This tool uses LangChain and Playwright to automate browser operations based on user input through a Streamlit UI.

## Features

- Automate browser operations using natural language instructions
- Execute complex browser flows like navigation, search, clicking, and content extraction
- Custom tools for extended operations (form input, waiting for elements, etc.)
- Simple and intuitive user interface

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd browser-automation
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Install Chromium browser for Playwright:
```bash
python -m playwright install chromium
```

## Configuration

1. Create a `.env` file in the project root directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```

2. Replace `your_openai_api_key_here` with your actual OpenAI API key. You can get an API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).

## Usage

1. Run the application:
```bash
python main.py
```

2. Open your browser and navigate to [http://localhost:8501](http://localhost:8501).

3. Enter your OpenAI API key if prompted.

4. Enter your browser operation instructions in the text area.

5. Click "Run Automation" to execute the instructions.

## Example Instructions

Here are some example instructions you can use to test the tool:

1. **Simple Navigation and Information Extraction**:
   ```
   Go to google.com, search for "LangChain tutorials", and tell me the title of the first result.
   ```

2. **Wikipedia Search and Summary**:
   ```
   Navigate to wikipedia.org, search for "Artificial Intelligence", go to the article, and summarize the first paragraph.
   ```

3. **News Aggregation**:
   ```
   Go to news.ycombinator.com and tell me the titles of the top 5 stories.
   ```

## Advanced Options

- **Show detailed agent steps**: Toggle this option to see the detailed steps the agent takes to execute your instructions.
- **Maximum iterations**: Set the maximum number of iterations the agent can take to complete the task.

## Project Structure

- `main.py`: Main entry point for the application
- `env_setup.py`: Environment setup utilities
- `browser_setup.py`: Playwright browser initialization
- `langchain_setup.py`: LangChain toolkit setup
- `agent_setup.py`: Browser-operable agent setup
- `custom_tools.py`: Custom tools for extended browser operations
- `browser_flow.py`: Browser operation flow definitions
- `streamlit_app.py`: Streamlit UI implementation

## Troubleshooting

- **OpenAI API Key Issues**: Ensure your API key is correctly set in the `.env` file or entered in the UI.
- **Browser Initialization Errors**: Make sure Playwright is properly installed with `python -m playwright install chromium`.
- **Agent Execution Errors**: Check the detailed agent steps to identify where the execution is failing.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
