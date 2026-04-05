# Tools & Function Calling Fundamentals

## What is Function Calling?
Function calling lets an LLM request execution of specific functions. The LLM doesn't run the code — it outputs a structured JSON saying "call this function with these arguments", and your code executes it.

## How It Works
```
User: "What's the weather in Tokyo?"
    ↓
LLM thinks: I need the get_weather tool
LLM outputs: {"name": "get_weather", "arguments": {"city": "Tokyo"}}
    ↓
Your code: runs get_weather("Tokyo") → "68°F Clear"
    ↓
Send result back to LLM
    ↓
LLM: "The weather in Tokyo is 68°F and clear."
```

## Key Concepts

### Tool Definition
You describe tools using JSON Schema:
- **name**: Function name
- **description**: What it does (LLM reads this to decide when to use it)
- **parameters**: Input schema with types and descriptions

### The Execution Loop
1. Send user message + tool definitions to LLM
2. LLM responds with either text OR tool call(s)
3. If tool calls: execute them, send results back to LLM
4. Repeat until LLM responds with text (no more tool calls)

### Parallel Tool Calls
- LLM can request multiple tools in one response
- Example: "Weather in NYC and calculate 100/3" → two tool calls at once
- Execute all, send all results back together

### Tool Choice
- `auto` - LLM decides whether to use tools (default)
- `required` - LLM must use at least one tool
- `none` - LLM cannot use tools
- Specific tool name - Force a particular tool

## Best Practices
- Write clear tool descriptions — the LLM uses them to decide
- Validate arguments before executing
- Handle errors gracefully and return useful error messages
- Limit the number of tools (too many confuses the LLM)
