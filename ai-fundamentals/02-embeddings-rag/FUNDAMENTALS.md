# Embeddings & RAG Fundamentals

## What are Embeddings?
Embeddings convert text into numerical vectors (arrays of numbers). Similar texts produce similar vectors. This lets us do **semantic search** — finding content by meaning, not just keywords.

## Key Concepts

### Embedding Space
- Each text becomes a point in high-dimensional space (e.g., 768 dimensions)
- Similar meanings = close together, different meanings = far apart
- "dog" is closer to "puppy" than to "airplane"

### Cosine Similarity
- Measures angle between two vectors: `1.0` = identical, `0.0` = unrelated, `-1.0` = opposite
- Formula: `dot(A, B) / (|A| * |B|)`
- Most common similarity metric for embeddings

### Chunking
When documents are too long for the embedding model:
| Strategy | Description | Best For |
|----------|-------------|----------|
| Fixed size | Split every N characters | Simple, fast |
| Sentence | Split on sentence boundaries | General text |
| Semantic | Split when topic changes | Complex documents |
| Overlap | Chunks share some text at boundaries | Preserving context |

## What is RAG?
Retrieval-Augmented Generation = give the LLM relevant context before asking it to answer.

### RAG Pipeline
```
User Query
    ↓
1. EMBED the query (convert to vector)
    ↓
2. RETRIEVE top-K similar documents from vector store
    ↓
3. AUGMENT the prompt with retrieved context
    ↓
4. GENERATE answer using LLM + context
```

### Why RAG?
- LLMs have a knowledge cutoff — RAG gives them fresh data
- No fine-tuning needed — just update your document store
- Answers are grounded in your actual data (reduces hallucination)

### Vector Databases
Store and search embeddings efficiently:
- **ChromaDB** - Simple, local, Python-native
- **Pinecone** - Cloud-hosted, managed
- **pgvector** - PostgreSQL extension
- **Weaviate** - Open source, feature-rich
