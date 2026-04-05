"""
MCP Client: discovers tools from the server, then uses them with an LLM.
Start mcp_server.py first!
"""
import requests, json

MCP_URL = "http://localhost:8080"
LLM_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

# 1. Discover tools from MCP server
tools = requests.post(f"{MCP_URL}/tools/list", json={}).json()
print("Discovered tools:")
for t in tools:
    print(f"  - {t['name']}: {t['description']}")

# 2. Call a tool via MCP server
def call_tool(name, arguments):
    r = requests.post(f"{MCP_URL}/tools/call", json={"name": name, "arguments": arguments})
    return r.json()["result"]

# 3. Use LLM + MCP tools together
def ask(query):
    print(f"\nQuery: {query}")
    tool_desc = "\n".join(f"- {t['name']}: {t['description']}" for t in tools)
    r = requests.post(LLM_URL, json={"model": MODEL, "messages": [
        {"role": "system", "content": f"You have these tools:\n{tool_desc}\nTo use a tool, respond: TOOL: name(arg=value)\nOtherwise just answer directly."},
        {"role": "user", "content": query}
    ], "stream": False})
    response = r.json()["message"]["content"]

    if "TOOL:" in response:
        try:
            tool_line = [l for l in response.split("\n") if "TOOL:" in l][0]
            call = tool_line.split("TOOL:")[-1].strip()
            name = call.split("(")[0]
            args_str = call.split("(")[1].rstrip(")")
            args = dict(item.split("=") for item in args_str.split(","))
            args = {k.strip(): v.strip().strip("'\"") for k, v in args.items()}
            result = call_tool(name, args)
            print(f"Tool called: {name}({args}) -> {result}")
            r = requests.post(LLM_URL, json={"model": MODEL, "messages": [
                {"role": "user", "content": query},
                {"role": "assistant", "content": response},
                {"role": "user", "content": f"Tool result: {result}. Now answer the original question."}
            ], "stream": False})
            print(f"Answer: {r.json()['message']['content']}")
        except Exception as e:
            print(f"Tool parse error: {e}\nRaw: {response}")
    else:
        print(f"Answer: {response}")

ask("What's the weather in Tokyo?")
ask("How many words are in: 'The quick brown fox jumps over the lazy dog'")
