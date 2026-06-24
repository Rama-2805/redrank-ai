def final_score(
    retrieval_score,
    experience,
    github,
    interview_rate,
    open_to_work,
    risk
):

    score = 0

    # Main retrieval score
    score += retrieval_score * 0.50

    # Experience
    score += min(
        experience * 2,
        20
    )

    # GitHub activity
    score += github * 0.15

    # Interview completion
    score += interview_rate * 10

    # Open to work bonus
    if open_to_work:
        score += 5

    # Fraud penalty
    score -= risk * 0.30

    return round(score, 2)