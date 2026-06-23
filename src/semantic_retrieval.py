import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

index = faiss.read_index(
    "artifacts/faiss.index"
)

with open(
    "artifacts/candidate_ids.txt"
) as f:

    candidate_ids = [
        line.strip()
        for line in f
    ]

jd = """
Senior AI Engineer

Required Skills:
Python
Embeddings
Retrieval
Ranking
Vector Databases
FAISS
Pinecone
RAG
LLMs
Fine-tuning
Production ML

Experience:
5 to 9 years
"""

query = model.encode(
    [jd],
    normalize_embeddings=True
)

scores, indices = index.search(
    query.astype("float32"),
    100
)

print("\nTOP SEMANTIC MATCHES\n")

for rank, (score, idx) in enumerate(
    zip(scores[0], indices[0]),
    start=1
):
    print(
        rank,
        candidate_ids[idx],
        round(float(score), 4)
    )