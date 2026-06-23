import json
from tqdm import tqdm

AI_SKILLS = {
    "Fine-tuning LLMs",
    "Embeddings",
    "Sentence Transformers",
    "FAISS",
    "Pinecone",
    "RAG",
    "MLOps",
    "QLoRA",
    "LoRA",
    "LangChain",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "TensorFlow",
    "PyTorch",
    "Milvus",
    "Qdrant",
    "Weaviate"
}

top_candidates = []

with open("data/candidates.jsonl") as f:
    for line in tqdm(f):
        candidate = json.loads(line)

        skills = {
            s.get("name", "")
            for s in candidate.get("skills", [])
        }

        ai_matches = len(skills.intersection(AI_SKILLS))

        if ai_matches >= 5:
            top_candidates.append(
                (
                    candidate["candidate_id"],
                    ai_matches,
                    candidate["profile"]["current_title"],
                    candidate["profile"]["years_of_experience"]
                )
            )

top_candidates.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nTop Candidates\n")

for row in top_candidates[:50]:
    print(row)