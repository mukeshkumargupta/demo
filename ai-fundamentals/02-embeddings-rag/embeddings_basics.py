import requests
import numpy as np

def get_embedding(text):
    r = requests.post("http://localhost:11434/api/embeddings", json={"model": "nomic-embed-text", "prompt": text})
    return r.json()["embedding"]

def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

texts = ["Python is a programming language", "JavaScript runs in browsers", "I love pizza"]
embeddings = [get_embedding(t) for t in texts]
print(f"Embedding dimension: {len(embeddings[0])}")

for i in range(len(texts)):
    for j in range(i + 1, len(texts)):
        print(f"'{texts[i]}' vs '{texts[j]}': {cosine_sim(embeddings[i], embeddings[j]):.4f}")
