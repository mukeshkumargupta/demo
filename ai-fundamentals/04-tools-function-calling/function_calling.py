import requests, json

URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

tools = [
    {"type": "function", "function": {
        "name": "get_weather", "description": "Get current weather for a city",
        "parameters": {"type": "object", "properties": {"city": {"type": "string", "description": "City name"}}, "required": ["city"]}
    }},
    {"type": "function", "function": {
        "name": "calculate", "description": "Evaluate a math expression",
        "parameters": {"type": "object", "properties": {"expression": {"type": "string", "description": "Math expression"}}, "required": ["expression"]}
    }}
]

def get_weather(city):
    return {"New York": "72F Sunny", "London": "58F Cloudy", "Tokyo": "68F Clear"}.get(city, "No data")

def calculate(expression):
    try: return str(eval(expression))
    except Exception as e: return str(e)

tool_map = {"get_weather": get_weather, "calculate": calculate}

def run(query):
    print(f"Query: {query}")
    messages = [{"role": "user", "content": query}]
    r = requests.post(URL, json={"model": MODEL, "messages": messages, "tools": tools, "stream": False})
    msg = r.json()["message"]

    while msg.get("tool_calls"):
        messages.append(msg)
        for tc in msg["tool_calls"]:
            args = tc["function"]["arguments"]
            if isinstance(args, str):
                args = json.loads(args)
            result = tool_map[tc["function"]["name"]](**args)
            print(f"  Tool: {tc['function']['name']}({args}) -> {result}")
            messages.append({"role": "tool", "content": result})
        r = requests.post(URL, json={"model": MODEL, "messages": messages, "tools": tools, "stream": False})
        msg = r.json()["message"]

    print(f"Answer: {msg['content']}\n")

run("What's the weather in Tokyo?")
run("What is 15 * 7 + 23?")
