import requests, time
import numpy as np

EMBED_URL = "http://localhost:11434/api/embeddings"
CHAT_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

def get_embedding(text):
    return requests.post(EMBED_URL, json={"model": "nomic-embed-text", "prompt": text}).json()["embedding"]

def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

class SemanticCache:
    def __init__(self, threshold=0.9):
        self.cache = []  # [(embedding, query, response)]
        self.threshold = threshold

    def get(self, query):
        q_emb = get_embedding(query)
        for emb, cached_query, response in self.cache:
            if cosine_sim(q_emb, emb) >= self.threshold:
                return response, cached_query
        return None, None

    def set(self, query, response):
        self.cache.append((get_embedding(query), query, response))

cache = SemanticCache(threshold=0.85)

def ask(query):
    print(f"\nQuery: {query}")
    start = time.time()

    cached, matched = cache.get(query)
    if cached:
        print(f"  ⚡ CACHE HIT (matched: '{matched}')")
        print(f"  Answer: {cached}")
        print(f"  Time: {time.time()-start:.2f}s")
        return

    r = requests.post(CHAT_URL, json={"model": MODEL, "messages": [{"role": "user", "content": query}], "stream": False})
    answer = r.json()["message"]["content"]
    cache.set(query, answer)
    print(f"  🔄 CACHE MISS (stored)")
    print(f"  Answer: {answer}")
    print(f"  Time: {time.time()-start:.2f}s")

ask("What is Python?")
ask("Tell me about Python")  # Should hit cache (semantically similar)
ask("What is JavaScript?")   # Should miss (different topic)
ask("Explain Python to me")  # Should hit cache
