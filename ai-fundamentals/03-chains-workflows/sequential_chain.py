import requests

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def llm(prompt, system="You are a helpful assistant."):
    r = requests.post(URL, json={"model": MODEL, "messages": [
        {"role": "system", "content": system}, {"role": "user", "content": prompt}
    ], "stream": False})
    return r.json()["message"]["content"]

topic = "Why Python is popular for AI"

print("Step 1: Generate outline")
outline = llm(f"Create a 3-point outline for: {topic}")
print(outline)

print("\nStep 2: Write article")
article = llm(f"Write a short article (150 words) based on this outline:\n{outline}")
print(article)

print("\nStep 3: Summarize")
print(llm(f"Summarize this in one sentence:\n{article}"))
