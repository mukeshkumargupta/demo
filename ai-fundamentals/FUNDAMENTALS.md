# AI Application Fundamentals - Complete Learning Guide

## 1. LLM Basics

The foundation of everything. Understand how Large Language Models work and how to interact with them.

### What to Learn
- What are LLMs (GPT, Claude, Llama, Gemini)
- Tokens, context windows, and token limits
- Temperature, top-p, and other generation parameters
- Prompt engineering: zero-shot, few-shot, chain-of-thought
- System prompts vs user prompts vs assistant messages
- API usage (OpenAI, Anthropic, etc.)

### Key Concepts
- **Completion API**: Send a prompt, get a response
- **Chat API**: Multi-turn conversation with roles (system/user/assistant)
- **Streaming**: Get responses token-by-token for better UX

---

## 2. Embeddings & RAG (Retrieval-Augmented Generation)

How to give LLMs access to your own data without fine-tuning.

### What to Learn
- What are embeddings (text → vector representation)
- Similarity search (cosine similarity)
- Vector databases (Pinecone, ChromaDB, Weaviate, pgvector)
- Chunking strategies for documents
- RAG pipeline: Retrieve → Augment prompt → Generate

### Key Concepts
- **Embedding Models**: OpenAI `text-embedding-3-small`, Cohere, sentence-transformers
- **Chunking**: Split documents into meaningful pieces (by size, sentence, semantic)
- **Retrieval**: Find the most relevant chunks for a user query
- **Augmentation**: Inject retrieved context into the LLM prompt

---

## 3. Chains & Workflows

Combine multiple LLM calls into structured workflows.

### What to Learn
- Sequential chains (output of one LLM call feeds into the next)
- Parallel execution (run multiple calls simultaneously)
- Conditional branching (route based on LLM output)
- LangChain / LlamaIndex basics
- Orchestration patterns

### Key Concepts
- **Chain**: A sequence of LLM calls with data flowing between them
- **Router**: Classify input and route to the right chain
- **Map-Reduce**: Process many items in parallel, then summarize
- **Workflow Engines**: LangGraph, CrewAI, Temporal for complex flows

---

## 4. Tools & Function Calling

Let LLMs interact with the real world by calling functions.

### What to Learn
- Function calling / tool use API (OpenAI, Anthropic)
- Defining tool schemas (JSON Schema)
- Parsing and executing tool calls
- Error handling and retries
- Common tools: web search, calculator, code execution, API calls

### Key Concepts
- **Tool Definition**: Describe what a function does, its parameters, and types
- **Tool Choice**: Let the LLM decide which tool to use (auto) or force one
- **Execution Loop**: LLM requests tool → you execute → return result → LLM continues
- **Parallel Tool Calls**: LLM can request multiple tools at once

---

## 5. Agents

Autonomous systems that use LLMs to reason, plan, and act.

### What to Learn
- What is an agent vs a chain (agents decide their own steps)
- ReAct pattern (Reason → Act → Observe → Repeat)
- Planning and task decomposition
- Multi-agent systems (agents collaborating)
- Agent frameworks: LangGraph, CrewAI, AutoGen, Swarm

### Key Concepts
- **Agent Loop**: Think → Pick tool → Execute → Observe → Repeat until done
- **Planning**: Break a complex task into subtasks
- **Reflection**: Agent reviews its own output and improves
- **Multi-Agent**: Specialized agents (researcher, coder, reviewer) working together
- **Guardrails**: Limit what agents can do to prevent harmful actions

---

## 6. MCP (Model Context Protocol)

An open standard for connecting LLMs to external tools and data sources.

### What to Learn
- What is MCP and why it exists (standardized tool/resource interface)
- MCP architecture: Host → Client → Server
- MCP primitives: Tools, Resources, Prompts
- Building an MCP server
- Connecting MCP servers to LLM applications

### Key Concepts
- **MCP Server**: Exposes tools/resources over a standard protocol (stdio or HTTP/SSE)
- **MCP Client**: Connects to servers and makes tools available to the LLM
- **Tools**: Functions the LLM can call (like function calling, but standardized)
- **Resources**: Data the LLM can read (files, DB records, API responses)
- **Prompts**: Reusable prompt templates exposed by the server
- **Transport**: stdio (local) or HTTP+SSE (remote)

### Why MCP Matters
- One standard instead of custom integrations per tool
- Ecosystem of pre-built servers (GitHub, Slack, databases, etc.)
- Separation of concerns: tool logic lives in the server, not your app

---

## 7. Memory & State Management

How to make AI applications remember context across interactions.

### What to Learn
- Short-term memory (conversation history in context window)
- Long-term memory (persisted across sessions)
- Summary memory (compress old conversations)
- Entity memory (track facts about users/topics)
- State machines for complex workflows

### Key Concepts
- **Buffer Memory**: Keep last N messages in context
- **Summary Memory**: Summarize older messages to save tokens
- **Vector Memory**: Store past interactions as embeddings, retrieve relevant ones
- **Checkpointing**: Save workflow state so it can resume after failures

---

## 8. Evaluation & Testing

How to measure if your AI application actually works well.

### What to Learn
- Why evaluation is hard for LLM apps (non-deterministic outputs)
- Metrics: relevance, faithfulness, coherence, toxicity
- LLM-as-judge (use one LLM to evaluate another)
- Human evaluation frameworks
- Regression testing for prompts
- Tools: Ragas, DeepEval, Promptfoo

### Key Concepts
- **Golden Dataset**: Curated question-answer pairs for testing
- **LLM-as-Judge**: Ask GPT-4 to score outputs on criteria
- **A/B Testing**: Compare two prompt versions on real traffic
- **Prompt Regression**: Ensure prompt changes don't break existing behavior

---

## 9. Production Deployment

Taking AI apps from prototype to production.

### What to Learn
- API rate limits and retry strategies
- Caching LLM responses (semantic cache)
- Cost optimization (model selection, prompt compression)
- Observability and tracing (LangSmith, Langfuse, Phoenix)
- Streaming responses to users
- Guardrails and content filtering
- Latency optimization

### Key Concepts
- **Semantic Cache**: Cache responses for semantically similar queries
- **Fallback Models**: Use cheaper models first, escalate to expensive ones
- **Tracing**: Log every LLM call, tool use, and decision for debugging
- **Guardrails**: Input/output validation to prevent misuse
- **Streaming**: Send tokens as they're generated for better UX

---

## Learning Path (Recommended Order)

```
LLM Basics → Embeddings & RAG → Chains & Workflows
    ↓
Tools & Function Calling → Agents → MCP
    ↓
Memory & State → Evaluation → Production Deployment
```

## Recommended Resources

| Topic | Resource |
|-------|----------|
| LLM Basics | [OpenAI API Docs](https://platform.openai.com/docs) |
| RAG | [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/) |
| Agents | [LangGraph Docs](https://langchain-ai.github.io/langgraph/) |
| MCP | [MCP Specification](https://modelcontextprotocol.io/) |
| Evaluation | [Promptfoo](https://www.promptfoo.dev/) |
| Observability | [Langfuse](https://langfuse.com/) |
