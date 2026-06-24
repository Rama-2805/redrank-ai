def fraud_score(candidate):

    risk = 0

    if candidate["github"] < 10 and candidate["experience"] > 10:
        risk += 40

    if len(candidate["skills"]) > 40:
        risk += 30

    return risk