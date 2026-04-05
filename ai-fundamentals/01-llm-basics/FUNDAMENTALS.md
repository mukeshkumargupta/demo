# LLM Fundamentals

## What is an LLM?
A Large Language Model is a neural network trained on massive text data that predicts the next token (word/subword) in a sequence. This simple mechanism enables conversation, code generation, reasoning, and more.

## Key Concepts

### Tokens
- LLMs don't see words — they see **tokens** (subwords)
- "Hello world" = 2 tokens, "Unbelievable" = 3 tokens
- Each model has a **context window** (max tokens it can process at once)

### Roles in Chat API
- **system**: Sets the AI's behavior/personality (invisible to user)
- **user**: The human's message
- **assistant**: The AI's response

### Temperature
- Controls randomness: `0.0` = deterministic, `1.0` = creative
- Use low temperature for factual tasks, higher for creative tasks

### Prompt Engineering Techniques
| Technique | Description | When to Use |
|-----------|-------------|-------------|
| Zero-shot | Ask directly, no examples | Simple tasks |
| Few-shot | Provide examples first | Classification, formatting |
| Chain-of-thought | "Think step by step" | Math, reasoning, logic |
| System prompt | Set behavior/constraints | All tasks |

### Streaming
- Instead of waiting for the full response, get tokens as they're generated
- Better UX for chat applications — user sees text appearing in real-time

## How Ollama Works
- Runs LLMs locally on your machine (no cloud, no API key)
- Exposes a REST API at `http://localhost:11434`
- `/api/chat` - Chat completion (what we use)
- `/api/generate` - Text completion
- `/api/embeddings` - Generate embeddings
