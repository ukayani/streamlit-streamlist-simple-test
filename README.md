# streamlit-streamlist-simple-test

Streamlit application repository

## Setup GitHub API Access

1. Create a GitHub personal access token:
   - Go to [GitHub Settings](https://github.com/settings/tokens)
   - Click on "Generate new token"
   - Select the scopes you need (e.g., `repo`, `read:org`)
   - Generate the token and copy it

2. Add the token to your environment variables:
   - On macOS/Linux, add the following line to your `~/.bashrc` or `~/.zshrc` file:
     ```sh
     export GITHUB_API_TOKEN=your_token_here
     ```
   - On Windows, add the token to your environment variables through the System Properties.

## Running the Streamlit App

1. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

3. Open your web browser and go to `http://localhost:8501` to view the app.
