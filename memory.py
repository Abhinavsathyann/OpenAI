class ChatMemory:
    def __init__(self):
        # start with a system prompt
        self.messages = [
            {"role": "system", "content": "You are a friendly AI assistant named Nova."}
        ]

    def add_user(self, message: str):
        self.messages.append({"role": "user", "content": message})

    def add_assistant(self, message: str):
        self.messages.append({"role": "assistant", "content": message})

    def get(self):
        return self.messages

    def clear(self):
        self.messages = [
            {"role": "system", "content": "You are a friendly AI assistant named Nova."}
        ]
