# Chains & Workflows Fundamentals

## What is a Chain?
A chain is a sequence of LLM calls where the output of one step becomes the input of the next. Instead of one big prompt, you break the task into smaller, focused steps.

## Key Patterns

### Sequential Chain
```
Input → LLM Call 1 → Output 1 → LLM Call 2 → Output 2 → Final Result
```
- Each step has a focused task (outline → write → summarize)
- Easier to debug — you can inspect each step's output
- Better quality — each LLM call has a simpler job

### Parallel Chain
```
         ┌→ LLM Call A → Result A ─┐
Input ───┼→ LLM Call B → Result B ─┼→ Combine
         └→ LLM Call C → Result C ─┘
```
- Run independent tasks simultaneously using threads
- Faster than sequential when tasks don't depend on each other
- Example: analyze sentiment + extract keywords + generate summary at the same time

### Router Chain
```
Input → Classifier → Route A (code expert)
                   → Route B (math expert)
                   → Route C (general assistant)
```
- First LLM call classifies the input
- Based on classification, route to a specialized prompt/model
- Each route has a system prompt optimized for that task type

### Map-Reduce
```
[Doc1, Doc2, Doc3] → Map (summarize each) → Reduce (combine summaries)
```
- Process many items in parallel (map phase)
- Combine results into a single output (reduce phase)
- Great for: summarizing multiple documents, analyzing datasets

## When to Use What
| Pattern | Use When |
|---------|----------|
| Sequential | Tasks have dependencies (step 2 needs step 1's output) |
| Parallel | Tasks are independent and you want speed |
| Router | Different input types need different handling |
| Map-Reduce | Processing collections of items |

## Frameworks
- **LangChain** - Popular, lots of built-in chains
- **LangGraph** - State machines for complex workflows
- **Plain Python** - Often sufficient for simple chains (what we use here)
