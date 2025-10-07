from config import client, MODEL, TEMPERATURE, MAX_TOKENS

def generate_reply(messages):
    """Send conversation to OpenAI API and return assistant reply."""
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ API Error: {e}"
