import json
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

candidate_ids = []
texts = []

with open("data/candidates.jsonl", "r") as f:

    for line in tqdm(f):

        candidate = json.loads(line)

        profile = candidate.get("profile", {})

        headline = profile.get("headline", "")
        summary = profile.get("summary", "")

        skills = " ".join(
            s.get("name", "")
            for s in candidate.get("skills", [])
        )

        career = " ".join(
            job.get("description", "")
            for job in candidate.get("career_history", [])
        )

        text = f"""
        {headline}
        {summary}

        Skills:
        {skills}

        Career:
        {career}
        """

        texts.append(text)
        candidate_ids.append(candidate["candidate_id"])

print(f"\nEncoding {len(texts)} candidates...\n")

embeddings = model.encode(
    texts,
    batch_size=128,
    show_progress_bar=True,
    convert_to_numpy=True,
    normalize_embeddings=True
)

np.save(
    "artifacts/candidate_embeddings.npy",
    embeddings
)

with open(
    "artifacts/candidate_ids.txt",
    "w"
) as f:

    for cid in candidate_ids:
        f.write(cid + "\n")

print("\nDone.")
print("Shape:", embeddings.shape)