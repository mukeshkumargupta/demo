# Evaluation & Testing Fundamentals

## Why is Evaluation Hard?
LLM outputs are non-deterministic — the same prompt can produce different responses. Traditional unit tests (expected == actual) don't work well. We need new approaches.

## Evaluation Methods

### LLM-as-Judge
Use a (stronger) LLM to score outputs:
```
Prompt: "Rate this answer 1-5 on accuracy and helpfulness"
Input: user question + AI answer
Output: score + reasoning
```
- Fast and scalable
- Correlates well with human judgment
- Can evaluate multiple criteria (accuracy, relevance, tone)

### Golden Dataset
Curated set of question-answer pairs:
```json
{"question": "What is Python?", "expected": "A programming language", "criteria": "Must mention programming"}
```
- Run your AI against all questions
- Compare outputs to expected answers
- Track scores over time (regression testing)

### Human Evaluation
- Most accurate but slowest and most expensive
- Use for high-stakes applications
- Often combined with LLM-as-judge for initial filtering

## Key Metrics

| Metric | What it Measures |
|--------|-----------------|
| Relevance | Does the answer address the question? |
| Faithfulness | Is the answer grounded in provided context? (for RAG) |
| Coherence | Is the answer well-structured and logical? |
| Completeness | Does it cover all aspects of the question? |
| Conciseness | Is it appropriately brief without losing info? |

## Prompt Regression Testing
When you change a prompt:
1. Run the new prompt against your golden dataset
2. Compare scores to the previous version
3. Ensure no regressions on existing test cases
4. Only deploy if scores improve or stay the same

## Tools
- **Promptfoo** - CLI tool for prompt testing and comparison
- **Ragas** - RAG-specific evaluation framework
- **DeepEval** - Python framework for LLM evaluation
- **Langfuse** - Observability + evaluation platform

## Key Takeaway
Always evaluate before deploying. Start with a small golden dataset and LLM-as-judge, then add human evaluation for critical use cases.
