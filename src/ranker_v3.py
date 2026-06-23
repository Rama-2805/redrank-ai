import pickle
import faiss
import pandas as pd

from sentence_transformers import SentenceTransformer

# --------------------------
# LOAD MODELS & DATA
# --------------------------

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

# --------------------------
# JOB DESCRIPTION
# --------------------------

JD = """
Senior AI Engineer

Python
Embeddings
FAISS
Vector Search
Ranking
Retrieval
RAG
LLMs
Fine Tuning
Candidate Matching
Learning To Rank

Experience: 5 to 9 years
"""

# --------------------------
# SEMANTIC RETRIEVAL
# --------------------------

query_embedding = model.encode(
    [JD],
    normalize_embeddings=True
)

scores, indices = index.search(
    query_embedding.astype("float32"),
    3000
)

# --------------------------
# HIGH VALUE TERMS
# --------------------------

HIGH_VALUE_TERMS = [
    "retrieval",
    "ranking",
    "learning-to-rank",
    "candidate",
    "candidate matching",
    "candidate-jd",
    "recruiter",
    "vector search",
    "embeddings",
    "recommendation",
    "behavioral",
    "reranking",
    "faiss",
    "rag",
    "bm25",
    "ndcg",
    "mrr",
    "dense retrieval",
    "hybrid retrieval"
]

results = []

# --------------------------
# RANKING LOOP
# --------------------------

for semantic_score, idx in zip(
    scores[0],
    indices[0]
):

    candidate_id = candidate_ids[idx]

    candidate = candidate_db[candidate_id]

    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})

    years = profile.get(
        "years_of_experience",
        0
    )

    title = profile.get(
        "current_title",
        ""
    ).lower()

    headline = profile.get(
        "headline",
        ""
    ).lower()

    summary = profile.get(
        "summary",
        ""
    ).lower()

    skills_text = " ".join([
        s.get("name", "")
        for s in candidate.get("skills", [])
    ]).lower()

    career_text = " ".join([
        c.get("description", "")
        for c in candidate.get(
            "career_history",
            []
        )
    ]).lower()

    full_text = (
        headline
        + " "
        + summary
        + " "
        + skills_text
        + " "
        + career_text
    )

    # ------------------
    # Keyword Score
    # ------------------

    keyword_score = 0

    for term in HIGH_VALUE_TERMS:

        if term in full_text:
            keyword_score += 5

    # ------------------
    # Experience Score
    # ------------------

    if 5 <= years <= 9:
        experience_score = 100
    elif 4 <= years < 5:
        experience_score = 60
    elif 9 < years <= 11:
        experience_score = 60
    else:
        experience_score = 20

    # ------------------
    # Title Score
    # ------------------

    title_score = 0

    if "ai" in title:
        title_score += 50

    if "machine learning" in title:
        title_score += 50

    if "search" in title:
        title_score += 50

    if "recommendation" in title:
        title_score += 50

    title_score = min(
        title_score,
        100
    )

    # ------------------
    # Behavioral Score
    # ------------------

    behavioral_score = 0

    behavioral_score += (
        signals.get(
            "recruiter_response_rate",
            0
        ) * 30
    )

    behavioral_score += (
        signals.get(
            "interview_completion_rate",
            0
        ) * 30
    )

    behavioral_score += (
        signals.get(
            "github_activity_score",
            0
        ) / 2.5
    )

    behavioral_score = min(
        behavioral_score,
        100
    )

    # ------------------
    # FINAL SCORE
    # ------------------

    final_score = (
        semantic_score * 100 * 0.35
        + keyword_score * 0.25
        + behavioral_score * 0.20
        + experience_score * 0.10
        + title_score * 0.10
    )

    results.append(
        (
            candidate_id,
            round(float(final_score), 3),
            profile.get(
                "current_title",
                ""
            ),
            years
        )
    )

results.sort(
    key=lambda x: x[1],
    reverse=True
)

# --------------------------
# SAVE CSV
# --------------------------

df = pd.DataFrame(
    results[:100],
    columns=[
        "candidate_id",
        "score",
        "title",
        "years"
    ]
)

df.to_csv(
    "submission_top100.csv",
    index=False
)

print("\nTOP 20\n")

for row in results[:20]:
    print(row)

print(
    "\nSaved: submission_top100.csv"
)