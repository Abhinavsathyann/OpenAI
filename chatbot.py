import os
import openai

# ------------- CONFIG -------------
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY environment variable before running.")
openai.api_key = API_KEY

MODEL = "gpt-4o"   # or "gpt-3.5-turbo" or another available model
# -----------------------------------

def chat_loop():
    print("Simple ChatGPT-style chatbot. Type 'quit' to exit.\n")
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user = input("You: ").strip()
        if not user:
            continue
        if user.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        # add user message to conversation
        conversation.append({"role": "user", "content": user})

        # call OpenAI Chat Completion
        try:
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=conversation,
                max_tokens=512,
                temperature=0.7,
                n=1,
            )
        except Exception as e:
            print("API error:", e)
            # pop last user message if you don't want it to persist on error
            conversation.pop()
            continue

        # extract assistant reply
        assistant_msg = response.choices[0].message["content"].strip()
        print("Assistant:", assistant_msg)
        # append assistant reply to conversation so context is preserved
        conversation.append({"role": "assistant", "content": assistant_msg})

if __name__ == "__main__":
    chat_loop()
