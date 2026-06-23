import pickle
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

candidate_db = pickle.load(
    open("artifacts/candidate_db.pkl", "rb")
)

with open("artifacts/candidate_ids.txt") as f:
    candidate_ids = [x.strip() for x in f]

index = faiss.read_index(
    "artifacts/faiss.index"
)

JD = """
Senior AI Engineer

Python
FAISS
Embeddings
RAG
Pinecone
Vector Search
Ranking
Retrieval
LLMs
Fine-tuning

Experience: 5-9 years
"""

query_embedding = model.encode(
    [JD],
    normalize_embeddings=True
)

scores, indices = index.search(
    query_embedding.astype("float32"),
    3000
)

results = []

for semantic_score, idx in zip(
    scores[0],
    indices[0]
):

    candidate_id = candidate_ids[idx]

    candidate = candidate_db[candidate_id]

    profile = candidate["profile"]

    years = profile.get(
        "years_of_experience",
        0
    )

    heuristic = 0

    if 5 <= years <= 9:
        heuristic += 20

    title = profile.get(
        "current_title",
        ""
    ).lower()

    if "ai" in title:
        heuristic += 20

    if "machine learning" in title:
        heuristic += 20

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    behavioral = 0

    behavioral += (
        signals.get(
            "recruiter_response_rate",
            0
        ) * 20
    )

    behavioral += (
        signals.get(
            "interview_completion_rate",
            0
        ) * 20
    )

    behavioral += (
        signals.get(
            "github_activity_score",
            0
        ) / 10
    )

    final_score = (
        semantic_score * 100 * 0.45
        + heuristic * 0.35
        + behavioral * 0.20
    )

    results.append(
        (
            candidate_id,
            round(final_score, 3),
            profile["current_title"],
            years
        )
    )

results.sort(
    key=lambda x: x[1],
    reverse=True
)

for row in results[:100]:
    print(row)