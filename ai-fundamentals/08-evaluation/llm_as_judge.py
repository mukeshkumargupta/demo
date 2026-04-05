import requests

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def llm(messages):
    r = requests.post(URL, json={"model": MODEL, "messages": messages, "stream": False})
    return r.json()["message"]["content"]

def generate_answer(question):
    return llm([{"role": "user", "content": question}])

def judge(question, answer):
    return llm([{"role": "system", "content": """You are an AI judge. Rate the answer on a scale of 1-5 for:
1. Accuracy - Is it factually correct?
2. Relevance - Does it address the question?
3. Clarity - Is it easy to understand?

Format: Accuracy: X/5, Relevance: X/5, Clarity: X/5
Reason: brief explanation"""}, {"role": "user", "content": f"Question: {question}\nAnswer: {answer}"}])

questions = [
    "What is Python?",
    "Explain recursion in one sentence.",
    "What is the difference between a list and a tuple in Python?"
]

for q in questions:
    answer = generate_answer(q)
    evaluation = judge(q, answer)
    print(f"Q: {q}\nA: {answer}\nEval: {evaluation}\n{'='*50}\n")
