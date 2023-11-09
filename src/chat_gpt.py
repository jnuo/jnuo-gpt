from dotenv import load_dotenv
import openai
import os

# load the .env file
load_dotenv()

# Set the Open AI key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def ask_chat_gpt(prompt, temperature=0.7, max_tokens=150):
    """Ask a question to ChatGPT and return the response."""
    response = openai.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()
