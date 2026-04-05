# 06 - MCP (Model Context Protocol)

Learn the open standard for connecting LLMs to external tools and data.

## Files

- `mcp_server.py` - Build a simple MCP server exposing tools
- `mcp_client.py` - Connect to an MCP server and use its tools

## Setup

```bash
pip install -r requirements.txt
# Terminal 1: Start the server
python mcp_server.py
# Terminal 2: Run the client
python mcp_client.py
```
