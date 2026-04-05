import requests

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def llm(prompt, system="You are a helpful assistant."):
    r = requests.post(URL, json={"model": MODEL, "messages": [
        {"role": "system", "content": system}, {"role": "user", "content": prompt}
    ], "stream": False})
    return r.json()["message"]["content"]

def planning_agent(goal):
    print(f"\nGoal: {goal}\n")

    # Step 1: Create plan
    plan = llm(f"Break this goal into 3 simple subtasks (numbered list):\n{goal}",
               system="You are a planning assistant. Output only the numbered list.")
    print(f"Plan:\n{plan}\n")

    # Step 2: Execute each subtask
    results = []
    for line in plan.strip().split("\n"):
        line = line.strip()
        if line and line[0].isdigit():
            print(f"Executing: {line}")
            result = llm(f"Complete this task concisely:\n{line}")
            print(f"Result: {result}\n")
            results.append(result)

    # Step 3: Combine results
    combined = "\n".join(results)
    final = llm(f"Combine these results into a coherent response:\n{combined}")
    print(f"Final Output:\n{final}")

planning_agent("Explain the 3 most important Python libraries for data science")
