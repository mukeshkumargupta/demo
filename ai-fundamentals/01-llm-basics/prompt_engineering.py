import requests

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def ask(prompt, label):
    r = requests.post(URL, json={"model": MODEL, "messages": [{"role": "user", "content": prompt}], "stream": False})
    print(f"\n--- {label} ---\n{r.json()['message']['content']}")

ask("Classify the sentiment as Positive/Negative/Neutral: 'This movie was terrible' -> ", "Zero-shot")

ask("""Classify the sentiment:
'I love this!' -> Positive
'Worst ever.' -> Negative
'It was okay.' -> Neutral
'This movie was terrible' -> """, "Few-shot")

ask("""A store has 15 apples. 3 customers each buy 2 apples, then a delivery adds 10 apples.
How many apples are left? Think step by step.""", "Chain-of-thought")
