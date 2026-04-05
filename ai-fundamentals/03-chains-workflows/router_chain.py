import requests

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def llm(prompt, system="You are a helpful assistant."):
    r = requests.post(URL, json={"model": MODEL, "messages": [
        {"role": "system", "content": system}, {"role": "user", "content": prompt}
    ], "stream": False})
    return r.json()["message"]["content"]

def classify(query):
    return llm(f"Classify into one word - code, math, or general:\n{query}",
               system="Respond with only one word.").strip().lower()

routes = {
    "code": "You are an expert programmer. Write concise code.",
    "math": "You are a math tutor. Show your work step by step.",
    "general": "You are a helpful assistant. Be brief."
}

for q in ["Write a Python function to reverse a string", "What is the integral of x^2?", "What is the capital of France?"]:
    cat = classify(q)
    print(f"Query: {q}\nRoute: {cat}\nAnswer: {llm(q, system=routes.get(cat, routes['general']))}\n")
