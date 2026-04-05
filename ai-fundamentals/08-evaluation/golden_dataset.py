import requests, json

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def llm(messages):
    r = requests.post(URL, json={"model": MODEL, "messages": messages, "stream": False})
    return r.json()["message"]["content"]

# Golden dataset: question, expected keywords, criteria
golden = [
    {"question": "What is Python?", "must_contain": ["programming", "language"], "criteria": "Must identify Python as a programming language"},
    {"question": "What is a variable?", "must_contain": ["store", "value"], "criteria": "Must explain that variables store values"},
    {"question": "What is a function?", "must_contain": ["reusable", "code"], "criteria": "Must mention reusable code or similar concept"},
]

def evaluate(question, answer, must_contain, criteria):
    # Simple keyword check
    keyword_score = sum(1 for kw in must_contain if kw.lower() in answer.lower()) / len(must_contain)

    # LLM judge for criteria
    judgment = llm([{"role": "system", "content": "Answer only PASS or FAIL."},
                    {"role": "user", "content": f"Does this answer meet the criteria?\nCriteria: {criteria}\nAnswer: {answer}"}])
    criteria_pass = "pass" in judgment.lower()

    return {"keyword_score": keyword_score, "criteria_pass": criteria_pass}

print("Running golden dataset evaluation...\n")
total_keyword, total_criteria, n = 0, 0, len(golden)

for item in golden:
    answer = llm([{"role": "user", "content": item["question"]}])
    result = evaluate(item["question"], answer, item["must_contain"], item["criteria"])
    total_keyword += result["keyword_score"]
    total_criteria += 1 if result["criteria_pass"] else 0
    status = "✅" if result["criteria_pass"] and result["keyword_score"] > 0.5 else "❌"
    print(f"{status} Q: {item['question']}")
    print(f"   A: {answer[:100]}...")
    print(f"   Keywords: {result['keyword_score']:.0%} | Criteria: {'PASS' if result['criteria_pass'] else 'FAIL'}\n")

print(f"Overall: Keywords {total_keyword/n:.0%} | Criteria {total_criteria}/{n} passed")
