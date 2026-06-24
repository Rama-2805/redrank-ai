def ranking_reason(info):

    reasons = []

    if info["experience"] > 5:
        reasons.append(
            f"{info['experience']} years experience"
        )

    if info["github"] > 70:
        reasons.append(
            "Strong GitHub activity"
        )

    if info["interview_rate"] > 0.7:
        reasons.append(
            "High interview completion"
        )

    if info["open_to_work"]:
        reasons.append(
            "Open to work"
        )

    return reasons