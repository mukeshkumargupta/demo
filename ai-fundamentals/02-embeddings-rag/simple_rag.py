import requests
import numpy as np

EMBED_URL = "http://localhost:11434/api/embeddings"
CHAT_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

docs = [
    "Python was created by Guido van Rossum and released in 1991.",
    "JavaScript was created by Brendan Eich in 1995 for Netscape.",
    "Rust was developed by Mozilla and first released in 2015.",
    "Go was designed at Google by Robert Griesemer, Rob Pike, and Ken Thompson.",
    "TypeScript is a superset of JavaScript developed by Microsoft."
]

def get_embedding(text):
    return requests.post(EMBED_URL, json={"model": "nomic-embed-text", "prompt": text}).json()["embedding"]

def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("Indexing documents...")
doc_embeddings = [get_embedding(d) for d in docs]

def retrieve(query, top_k=2):
    q_emb = get_embedding(query)
    scores = sorted([(i, cosine_sim(q_emb, d)) for i, d in enumerate(doc_embeddings)], key=lambda x: -x[1])
    return [(docs[i], s) for i, s in scores[:top_k]]

query = "Who created Python?"
results = retrieve(query)
print(f"\nQuery: {query}")
for doc, score in results:
    print(f"  [{score:.4f}] {doc}")

context = "\n".join(doc for doc, _ in results)
r = requests.post(CHAT_URL, json={"model": MODEL, "messages": [
    {"role": "system", "content": f"Answer using only this context:\n{context}"},
    {"role": "user", "content": query}
], "stream": False})
print(f"\nAnswer: {r.json()['message']['content']}")
