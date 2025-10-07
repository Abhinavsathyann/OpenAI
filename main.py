from memory import ChatMemory
from chat_engine import generate_reply

def main():
    print("🤖 ChatGPT-style AI (type 'exit' or 'clear' to quit or reset)\n")

    memory = ChatMemory()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        elif user_input.lower() == "clear":
            memory.clear()
            print("🧹 Memory cleared.")
            continue
        elif not user_input:
            continue

        memory.add_user(user_input)
        assistant_reply = generate_reply(memory.get())
        print("AI:", assistant_reply)
        memory.add_assistant(assistant_reply)

if __name__ == "__main__":
    main()
