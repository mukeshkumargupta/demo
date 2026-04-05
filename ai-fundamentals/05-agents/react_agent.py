import requests, json

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

# Tools the agent can use
def search(query):
    data = {"Python": "A programming language created in 1991", "AI": "Artificial Intelligence, machines that mimic human intelligence",
            "LLM": "Large Language Model, neural network trained on text data"}
    return data.get(query, f"No results for '{query}'")

def calculate(expr):
    try: return str(eval(expr))
    except: return "Error"

tools = {"search": search, "calculate": calculate}

SYSTEM = """You are an AI agent. You can use tools to answer questions.

Available tools:
- search(query): Search for information. query must be a single word/topic.
- calculate(expr): Evaluate a math expression.

Respond in this exact format:
THOUGHT: your reasoning
ACTION: tool_name(argument)

When you have the final answer:
THOUGHT: I have enough information
ANSWER: your final answer"""

def run_agent(query, max_steps=5):
    print(f"\nQuery: {query}")
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": query}]

    for step in range(max_steps):
        r = requests.post(URL, json={"model": MODEL, "messages": messages, "stream": False})
        response = r.json()["message"]["content"]
        print(f"\nStep {step + 1}:\n{response}")

        if "ANSWER:" in response:
            return response.split("ANSWER:")[-1].strip()

        if "ACTION:" in response:
            action_line = [l for l in response.split("\n") if "ACTION:" in l]
            if action_line:
                action = action_line[0].split("ACTION:")[-1].strip()
                try:
                    func_name = action.split("(")[0].strip()
                    arg = action.split("(")[1].rstrip(")")
                    arg = arg.strip("'\"")
                    if func_name in tools:
                        result = tools[func_name](arg)
                        print(f"OBSERVATION: {result}")
                        messages.append({"role": "assistant", "content": response})
                        messages.append({"role": "user", "content": f"OBSERVATION: {result}"})
                        continue
                except: pass

        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "user", "content": "Continue. Use the format specified."})

    return "Max steps reached"

run_agent("What is Python?")
run_agent("What is 25 * 4 + 10?")
