# Python ChatGPT AI

A simple Python-based ChatGPT-style AI that interacts with OpenAI's GPT models. This project provides a terminal-based interface to chat with an AI using your OpenAI API key.

---

## Features

- Chat with OpenAI GPT models via Python
- Configurable model, temperature, and max tokens
- Terminal interface with `exit` and `clear` commands
- Environment variable-based API key management
- Modular code structure for easy customization

---

## Folder Structure

OpenAI/
├── main.py # Entry point for the chat application
├── chat_engine.py # Handles sending prompts and receiving AI responses
├── config.py # API client and configuration
├── requirements.txt # Python dependencies
├── .gitignore # Excludes secrets and temporary files
└── README.md # Project documentation


## Create a virtual environment (optional but recommended):

python -m venv venv

venv\Scripts\activate     # Windows

source venv/bin/activate  # macOS / Linux


## Install dependencies:

pip install -r requirements.txt

---

## Set your OpenAI API key as an environment variable:

setx OPENAI_API_KEY "YOUR_OPENAI_API_KEY"

Important: Do not commit your API key to GitHub. Always use .gitignore to exclude .env or config files containing secrets.

## Run the chat application:

python main.py

Type your messages after You: prompt.

Commands:
exit → Quit the chat
clear → Reset the chat

#Security

.env and API keys are excluded from GitHub via .gitignore.

Never commit sensitive information.

Use a fresh mirror clone if you accidentally commit secrets.

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Abhinavsathyann/OpenAI.git
cd OpenAI
