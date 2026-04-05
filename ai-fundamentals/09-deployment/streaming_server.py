"""
Simple HTTP server that streams LLM responses using Server-Sent Events (SSE).
Open http://localhost:9090 in your browser to see streaming in action.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests, json

HTML = """<!DOCTYPE html>
<html><body>
<h3>Streaming LLM Demo</h3>
<input id="q" placeholder="Ask something..." style="width:300px">
<button onclick="ask()">Ask</button>
<pre id="out"></pre>
<script>
function ask() {
    document.getElementById('out').textContent = '';
    const q = document.getElementById('q').value;
    const es = new EventSource('/stream?q=' + encodeURIComponent(q));
    es.onmessage = e => {
        if (e.data === '[DONE]') { es.close(); return; }
        document.getElementById('out').textContent += e.data;
    };
}
</script></body></html>"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(HTML.encode())
        elif self.path.startswith("/stream"):
            query = self.path.split("q=")[-1].replace("%20", " ") if "q=" in self.path else "Hello"
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            r = requests.post("http://localhost:11434/api/chat",
                json={"model": "llama3.2:1b", "messages": [{"role": "user", "content": query}], "stream": True}, stream=True)
            for line in r.iter_lines():
                if line:
                    chunk = json.loads(line)
                    token = chunk["message"]["content"]
                    self.wfile.write(f"data: {token}\n\n".encode())
                    self.wfile.flush()
            self.wfile.write(b"data: [DONE]\n\n")

    def log_message(self, format, *args): pass

print("Open http://localhost:9090 in your browser")
HTTPServer(("localhost", 9090), Handler).serve_forever()
