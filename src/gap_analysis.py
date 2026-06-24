def gap_analysis(
    resume_skills,
    jd_skills
):

    resume_set = set(
        skill.lower()
        for skill in resume_skills
    )

    jd_set = set(
        skill.lower()
        for skill in jd_skills
    )

    missing = list(
        jd_set - resume_set
    )

    matched = list(
        resume_set & jd_set
    )

    score = 0

    if len(jd_set) > 0:

        score = round(
            (
                len(matched)
                / len(jd_set)
            ) * 100,
            2
        )

    return {
        "matched": matched,
        "missing": missing,
        "score": score
    }