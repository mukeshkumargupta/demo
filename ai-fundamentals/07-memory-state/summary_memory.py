import requests

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def llm(messages):
    r = requests.post(URL, json={"model": MODEL, "messages": messages, "stream": False})
    return r.json()["message"]["content"]

class SummaryMemory:
    """Summarize old messages to compress conversation history."""
    def __init__(self, max_recent=2):
        self.summary = ""
        self.recent = []
        self.max_recent = max_recent

    def add(self, role, content):
        self.recent.append({"role": role, "content": content})
        if len(self.recent) > self.max_recent * 2:
            old = self.recent[:2]
            self.recent = self.recent[2:]
            old_text = "\n".join(f"{m['role']}: {m['content']}" for m in old)
            self.summary = llm([
                {"role": "system", "content": "Summarize this conversation in 1-2 sentences. Include key facts."},
                {"role": "user", "content": f"Previous summary: {self.summary}\n\nNew messages:\n{old_text}"}
            ])
            print(f"  [Summary updated: {self.summary}]")

    def get_messages(self):
        msgs = [{"role": "system", "content": "You are a helpful assistant."}]
        if self.summary:
            msgs.append({"role": "system", "content": f"Conversation summary: {self.summary}"})
        return msgs + self.recent

memory = SummaryMemory(max_recent=2)

print("Chat with summary memory. Old messages get summarized. Type 'quit' to exit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    memory.add("user", user_input)
    reply = llm(memory.get_messages())
    memory.add("assistant", reply)
    print(f"AI: {reply}\n")
