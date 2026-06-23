import json
from collections import Counter
from tqdm import tqdm

AI_KEYWORDS = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "LLM",
    "PyTorch",
    "TensorFlow",
    "Transformers",
    "Embeddings",
    "RAG",
    "FAISS",
    "Vector Database",
    "LoRA",
    "QLoRA",
    "Fine-tuning LLMs",
    "MLOps",
    "LangChain",
    "Milvus",
    "Pinecone",
    "Weaviate",
    "Qdrant"
]

counts = Counter()

with open("data/candidates.jsonl") as f:
    for line in tqdm(f):
        candidate = json.loads(line)

        for skill in candidate.get("skills", []):
            name = skill.get("name", "")

            for keyword in AI_KEYWORDS:
                if keyword.lower() in name.lower():
                    counts[name] += 1

print("\nAI Related Skills\n")

for skill, count in counts.most_common():
    print(f"{skill}: {count}")