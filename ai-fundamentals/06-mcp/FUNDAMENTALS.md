# MCP (Model Context Protocol) Fundamentals

## What is MCP?
MCP is an open protocol (by Anthropic) that standardizes how LLM applications connect to external tools and data sources. Think of it as a **USB-C for AI** — one standard connector instead of custom integrations.

## Why MCP?
Before MCP:
```
Your App → Custom code for GitHub API
Your App → Custom code for Slack API
Your App → Custom code for Database
(N integrations = N custom implementations)
```

With MCP:
```
Your App → MCP Client → MCP Server (GitHub)
                      → MCP Server (Slack)
                      → MCP Server (Database)
(One protocol for all)
```

## Architecture
```
┌─────────────┐     ┌────────────┐     ┌────────────┐
│  LLM Host   │────▶│ MCP Client │────▶│ MCP Server │
│ (your app)  │     │            │     │ (tools/data)│
└─────────────┘     └────────────┘     └────────────┘
```

- **Host**: Your application (e.g., Claude Desktop, VS Code, custom app)
- **Client**: Manages connection to servers (usually built into the host)
- **Server**: Exposes tools, resources, and prompts

## MCP Primitives

### Tools
Functions the LLM can call:
```json
{
  "name": "get_weather",
  "description": "Get weather for a city",
  "inputSchema": {"type": "object", "properties": {"city": {"type": "string"}}}
}
```

### Resources
Data the LLM can read (like files):
```
resource://weather/current → Current weather data
resource://docs/readme → README file content
```

### Prompts
Reusable prompt templates:
```
prompt://summarize → "Summarize the following: {text}"
```

## Transport
- **stdio**: Server runs as a subprocess, communicates via stdin/stdout (local)
- **HTTP + SSE**: Server runs as a web service (remote, scalable)

## Ecosystem
Pre-built MCP servers exist for:
- GitHub, GitLab (repos, issues, PRs)
- Slack, Discord (messages, channels)
- PostgreSQL, SQLite (database queries)
- Filesystem (read/write files)
- Web search, web scraping
- And many more at [mcp.so](https://mcp.so)

## Key Takeaway
MCP separates **tool logic** from **AI logic**. Your app focuses on the AI experience, MCP servers handle the integrations.
