def calculate_match(info, score):

    skills_score = min(
        len(info["skills"]) * 15,
        100
    )

    exp_score = min(
        info["experience"] * 12,
        100
    )

    title_score = 90

    recruiter_score = (
        info["github"] +
        info["interview_rate"] * 100
    ) / 2

    return {
        "skills": round(skills_score, 1),
        "experience": round(exp_score, 1),
        "title": round(title_score, 1),
        "recruiter": round(recruiter_score, 1),
        "overall": round(score, 2)
    }