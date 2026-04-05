import requests

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"
messages = [{"role": "system", "content": "You are a Python tutor. Keep answers brief."}]

print("Chat with AI (type 'quit' to exit)")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "quit":
        break
    messages.append({"role": "user", "content": user_input})
    r = requests.post(URL, json={"model": MODEL, "messages": messages, "stream": False})
    reply = r.json()["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print(f"AI: {reply}")
