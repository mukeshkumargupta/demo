"""
Simple MCP-like server using HTTP.
Demonstrates the concept: expose tools over a standard protocol.
Run this first, then run mcp_client.py in another terminal.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Tool implementations
def get_weather(city):
    return {"New York": "72F Sunny", "London": "58F Cloudy", "Tokyo": "68F Clear"}.get(city, "No data")

def word_count(text):
    return str(len(text.split()))

TOOLS = {
    "get_weather": {"fn": get_weather, "description": "Get weather for a city", "parameters": {"city": "string"}},
    "word_count": {"fn": word_count, "description": "Count words in text", "parameters": {"text": "string"}}
}

class MCPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))

        if self.path == "/tools/list":
            result = [{"name": k, "description": v["description"], "parameters": v["parameters"]} for k, v in TOOLS.items()]
        elif self.path == "/tools/call":
            tool = TOOLS.get(data["name"])
            result = {"result": tool["fn"](**data["arguments"])} if tool else {"error": "Unknown tool"}
        else:
            result = {"error": "Unknown endpoint"}

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

    def log_message(self, format, *args):
        print(f"[MCP Server] {args[0]}")

print("MCP Server running on http://localhost:8080")
print("Tools available:", list(TOOLS.keys()))
HTTPServer(("localhost", 8080), MCPHandler).serve_forever()
