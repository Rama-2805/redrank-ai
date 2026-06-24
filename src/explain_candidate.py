import pickle

DB_PATH = "artifacts/candidate_db.pkl"


def explain_candidate(candidate_id):

    with open(DB_PATH, "rb") as f:
        db = pickle.load(f)

    c = db[candidate_id]

    profile = c["profile"]
    skills = c["skills"]
    signals = c["redrob_signals"]

    top_skills = []

    important = [
        "FAISS",
        "RAG",
        "BM25",
        "Learning to Rank",
        "Embeddings",
        "LLMs",
        "LangChain",
        "NLP",
        "Vector Search"
    ]

    for s in skills:
        if s["name"] in important:
            top_skills.append(s["name"])

    return {
        "title": profile["current_title"],
        "experience": profile["years_of_experience"],
        "skills": top_skills[:5],
        "github": signals["github_activity_score"],
        "interview_rate": signals["interview_completion_rate"],
        "open_to_work": signals["open_to_work_flag"]
    }
