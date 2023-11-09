# Onur's ChatGPT Project

Playground for what I can do with this pf.

The idea is that I record some commonly used long prompts in a documented way. Also maybe add some extra input information to the prompt, and easily ask chatgpt the same question without typing the same prompt over and over again in a text editor, and of course later, to record the output in an output.txt file.

## Installation

You'll need a prompt first. According to the nature of the prompt, you might need an extra input file. 

* You need to create a .env file in your folder and add your open api secret key using the format
```bash
OPENAI_API_KEY=your_api_key

* create a config.py file in root directory and insert the following to really connect to chatgpt
```bash
USE_OPENAI_API = True  # Set to False to use mock responses

```bash
pip install -r requirements.txt
# jnuo-gpt
