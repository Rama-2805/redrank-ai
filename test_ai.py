from src.recruiter_ai import ask_recruiter

answer = ask_recruiter(
    """
    Why is a candidate with RAG, FAISS,
    BM25, Learning-to-Rank and
    7 years experience valuable
    for recruiter search systems?
    """
)

print(answer)
