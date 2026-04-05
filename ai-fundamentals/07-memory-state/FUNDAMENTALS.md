# Memory & State Fundamentals

## The Problem
LLMs are stateless — each API call is independent. They don't remember previous conversations unless you explicitly include the history in the prompt.

## Memory Types

### Buffer Memory (Sliding Window)
Keep the last N messages in context:
```
[system, user1, assistant1, user2, assistant2, user3, assistant3]
                            ↑ only keep last 4 messages ↑
```
- Simple and effective
- Loses old context when window fills up
- Best for: short conversations

### Summary Memory
Summarize older messages to compress history:
```
[system, summary_of_old_messages, user5, assistant5, user6, assistant6]
```
- Preserves key information from old messages
- Uses an LLM call to generate summaries
- Best for: long conversations where old context matters

### Vector/Semantic Memory
Store all messages as embeddings, retrieve relevant ones:
```
User: "What did I say about Python?"
→ Search embeddings → Find relevant past messages → Include in context
```
- Most flexible — retrieves by relevance, not recency
- Best for: very long conversations, knowledge bases

### Entity Memory
Track facts about specific entities:
```
{
  "user": {"name": "Mukesh", "likes": "Python", "role": "developer"},
  "project": {"name": "demo", "language": "Python"}
}
```
- Structured knowledge that persists
- Best for: personalization, CRM-like applications

## State Management for Workflows

### Checkpointing
Save workflow state so it can resume:
```
Step 1: ✅ Done (saved)
Step 2: ✅ Done (saved)
Step 3: ❌ Failed
→ Resume from Step 3 instead of starting over
```

### State Machines
Define explicit states and transitions:
```
IDLE → GATHERING_INFO → PROCESSING → CONFIRMING → DONE
```
- Each state has allowed actions and transitions
- Prevents invalid operations
- LangGraph uses this pattern

## Key Takeaway
Choose memory strategy based on conversation length and what information matters most.
