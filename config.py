import os
from openai import OpenAI

# Load API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("⚠️ Please set your OPENAI_API_KEY environment variable.")

# Create OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Model configuration
MODEL = "gpt-4o-mini"   # or "gpt-3.5-turbo"
TEMPERATURE = 0.7
MAX_TOKENS = 500
