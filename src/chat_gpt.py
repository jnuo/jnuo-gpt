from dotenv import load_dotenv
import openai
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

# load the .env file
load_dotenv()

# Set the Open AI key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def ask_chat_gpt(prompt, temperature=0.7, max_tokens=150):
    """Ask a question to ChatGPT and return the response."""
    
    if(config.USE_OPENAI_API):
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    else:
        return "Hola, ¿cómo estás?"

