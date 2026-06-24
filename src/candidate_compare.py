def compare_candidates(c1, c2):

    score1 = (
        c1["github"]
        + (c1["interview_rate"] * 100)
        + (c1["experience"] * 5)
    )

    score2 = (
        c2["github"]
        + (c2["interview_rate"] * 100)
        + (c2["experience"] * 5)
    )

    winner = c1["title"]

    if score2 > score1:
        winner = c2["title"]

    return {
        "winner": winner,
        "score1": round(score1, 2),
        "score2": round(score2, 2)
    }