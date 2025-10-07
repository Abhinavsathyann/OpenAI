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


---

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Abhinavsathyann/OpenAI.git
cd OpenAI
