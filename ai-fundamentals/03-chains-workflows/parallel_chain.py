import requests
import concurrent.futures

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def llm(prompt):
    r = requests.post(URL, json={"model": MODEL, "messages": [{"role": "user", "content": prompt}], "stream": False})
    return r.json()["message"]["content"]

text = "AI will transform education by personalizing learning for every student."
tasks = {
    "sentiment": f"What is the sentiment of: '{text}'",
    "keywords": f"Extract 3 keywords from: '{text}'",
    "counter": f"Give one counter-argument to: '{text}'"
}

print(f"Analyzing: {text}\n")
with concurrent.futures.ThreadPoolExecutor() as ex:
    futures = {ex.submit(llm, p): n for n, p in tasks.items()}
    for f in concurrent.futures.as_completed(futures):
        print(f"{futures[f]}: {f.result()}\n")
