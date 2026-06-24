def extract_skills(text):

    skills_db = [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "RAG",
        "FAISS",
        "LangChain",
        "OpenCV",
        "NLP",
        "YOLO",
        "SQL",
        "MongoDB",
        "AWS",
        "Docker",
        "FastAPI"
    ]

    found = []

    text = text.lower()

    for skill in skills_db:

        if skill.lower() in text:
            found.append(skill)

    return found