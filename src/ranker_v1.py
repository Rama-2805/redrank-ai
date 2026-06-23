import json
from tqdm import tqdm

DATASET = "data/candidates.jsonl"

AI_SKILLS = {
    "Python",
    "Embeddings",
    "Sentence Transformers",
    "FAISS",
    "Pinecone",
    "Milvus",
    "Qdrant",
    "Weaviate",
    "RAG",
    "MLOps",
    "NLP",
    "Machine Learning",
    "Deep Learning",
    "LLMs",
    "Fine-tuning LLMs",
    "LoRA",
    "QLoRA",
    "LangChain",
    "TensorFlow",
    "PyTorch"
}

GOOD_TITLES = {
    "Senior AI Engineer",
    "AI Engineer",
    "Machine Learning Engineer",
    "ML Engineer",
    "Applied ML Engineer",
    "Senior NLP Engineer",
    "Senior Machine Learning Engineer",
    "Data Scientist",
    "Senior Data Scientist",
    "Recommendation Systems Engineer",
    "Staff Machine Learning Engineer",
    "Senior Applied Scientist"
}

BAD_TITLES = {
    "Accountant",
    "HR Manager",
    "Sales Executive",
    "Customer Support",
    "Marketing Manager",
    "Content Writer"
}


def skill_score(candidate):
    skills = {
        s.get("name", "")
        for s in candidate.get("skills", [])
    }

    return len(skills.intersection(AI_SKILLS))


def experience_score(years):
    if 5 <= years <= 9:
        return 10

    if 4 <= years < 5:
        return 7

    if 9 < years <= 11:
        return 7

    return 2


def title_score(title):

    if title in GOOD_TITLES:
        return 10

    if title in BAD_TITLES:
        return -5

    return 0


def behavioral_score(candidate):

    signals = candidate.get("redrob_signals", {})

    score = 0

    if signals.get("open_to_work_flag"):
        score += 3

    score += signals.get("recruiter_response_rate", 0) * 5

    score += signals.get("interview_completion_rate", 0) * 5

    github = signals.get("github_activity_score", -1)

    if github > 0:
        score += github / 20

    return score


def final_score(candidate):

    profile = candidate.get("profile", {})

    years = profile.get("years_of_experience", 0)
    title = profile.get("current_title", "")

    score = 0

    score += skill_score(candidate) * 4
    score += experience_score(years)
    score += title_score(title)
    score += behavioral_score(candidate)

    return score


results = []

with open(DATASET) as f:

    for line in tqdm(f):

        candidate = json.loads(line)

        score = final_score(candidate)

        results.append(
            (
                candidate["candidate_id"],
                score,
                candidate["profile"]["current_title"],
                candidate["profile"]["years_of_experience"]
            )
        )

results.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nTOP 100\n")

for row in results[:100]:
    print(row)