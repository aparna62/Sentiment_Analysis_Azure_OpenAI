# Import necessary libraries
from flask import Flask, render_template, request
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file for secure secret management
load_dotenv()

# Initialize the Flask web application
app = Flask(__name__)

# Read Azure OpenAI configurations from environment variables (no hard-coding)
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Set up Azure OpenAI client using the latest SDK and your env variables
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_OPENAI_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

# Define the route for the home page (web form and result view)
@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    error_message = None

    if request.method == 'POST':
        user_input = request.form['text']

        try:
            # Send user's input to the Azure OpenAI model for sentiment analysis
            response = client.chat.completions.create(
                model=AZURE_OPENAI_DEPLOYMENT,  # Deployment name set on Azure
                messages=[
                    {"role": "system", "content": "You are a sentiment analysis assistant. For the user input, return one of: Positive, Negative, or Neutral, as a single word answer (no explanations)."},
                    {"role": "user", "content": user_input}
                ]
            )
            # Save the sentiment result from the model's output
            sentiment = response.choices[0].message.content.strip()
        except Exception as e:
            # Handle errors gracefully
            error_message = f"Error: {str(e)}"

    # Render the web page with result or error message
    return render_template('index.html', sentiment=sentiment, error_message=error_message)

# Only run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production