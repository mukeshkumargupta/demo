import requests

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

class BufferMemory:
    """Keep only the last N message pairs to stay within context limits."""
    def __init__(self, max_pairs=3):
        self.system = {"role": "system", "content": "You are a helpful assistant. Remember what the user tells you."}
        self.messages = []
        self.max_pairs = max_pairs

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})
        # Keep only last N pairs (user + assistant = 2 messages per pair)
        if len(self.messages) > self.max_pairs * 2:
            self.messages = self.messages[-self.max_pairs * 2:]

    def get_messages(self):
        return [self.system] + self.messages

memory = BufferMemory(max_pairs=3)

print("Chat with buffer memory (last 3 exchanges). Type 'quit' to exit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    memory.add("user", user_input)
    r = requests.post(URL, json={"model": MODEL, "messages": memory.get_messages(), "stream": False})
    reply = r.json()["message"]["content"]
    memory.add("assistant", reply)
    print(f"AI: {reply}")
    print(f"  [Memory: {len(memory.messages)//2} exchanges stored]\n")
