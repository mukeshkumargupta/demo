# Agent Fundamentals

## What is an Agent?
An agent is an LLM that autonomously decides what actions to take to accomplish a goal. Unlike chains (fixed steps), agents dynamically choose their next step based on observations.

## Agent vs Chain
| | Chain | Agent |
|---|---|---|
| Steps | Pre-defined | Dynamic |
| Control | Developer decides flow | LLM decides flow |
| Flexibility | Fixed path | Adapts to results |
| Complexity | Simple | Can handle unexpected situations |

## Key Patterns

### ReAct (Reason + Act)
The most common agent pattern:
```
1. THOUGHT: "I need to find the weather in Tokyo"
2. ACTION: call get_weather("Tokyo")
3. OBSERVATION: "68°F Clear"
4. THOUGHT: "Now I have the answer"
5. FINAL ANSWER: "The weather in Tokyo is 68°F and clear"
```
Loop continues until the agent decides it has enough info to answer.

### Planning Agent
```
Goal: "Write a blog post about Python"
    ↓
Plan:
  1. Research key Python features
  2. Create an outline
  3. Write each section
  4. Review and edit
    ↓
Execute each step (may re-plan if needed)
```

### Multi-Agent Systems
Multiple specialized agents collaborating:
- **Researcher** - Gathers information
- **Writer** - Creates content
- **Reviewer** - Checks quality
- **Orchestrator** - Coordinates the team

## Key Concepts

### Agent Loop
```python
while not done:
    thought = llm.think(observations)
    action = llm.choose_action(thought)
    observation = execute(action)
    if llm.is_done(observation):
        done = True
```

### Reflection
Agent reviews its own output and improves:
1. Generate initial response
2. Critique: "What's wrong with this?"
3. Improve based on critique
4. Repeat until satisfactory

### Guardrails
- Limit max iterations (prevent infinite loops)
- Restrict available tools (principle of least privilege)
- Validate outputs before returning to user
- Human-in-the-loop for critical actions

## Frameworks
- **LangGraph** - State machine-based agents
- **CrewAI** - Multi-agent orchestration
- **AutoGen** - Microsoft's multi-agent framework
- **Swarm** - OpenAI's lightweight agent framework
