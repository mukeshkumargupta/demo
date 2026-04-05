import requests, json

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def chat(messages):
    r = requests.post(URL, json={"model": MODEL, "messages": messages, "stream": False})
    return r.json()["message"]["content"]

# 1. Basic chat completion
print("Basic:", chat([{"role": "user", "content": "What is machine learning in one sentence?"}]))

# 2. System prompt
print("\nSystem prompt:", chat([
    {"role": "system", "content": "You are a helpful assistant that responds in exactly 10 words."},
    {"role": "user", "content": "Explain neural networks"}
]))

# 3. Streaming
print("\nStreaming: ", end="")
r = requests.post(URL, json={"model": MODEL, "messages": [{"role": "user", "content": "Count from 1 to 5"}], "stream": True}, stream=True)
for line in r.iter_lines():
    if line:
        print(json.loads(line)["message"]["content"], end="", flush=True)
print()
