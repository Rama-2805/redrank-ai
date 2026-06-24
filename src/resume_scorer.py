def score_resume(resume_skills, candidate_skills):

    matches = 0

    for skill in candidate_skills:
        if skill.lower() in [
            s.lower()
            for s in resume_skills
        ]:
            matches += 1

    if len(candidate_skills) == 0:
        return 0

    score = (
        matches /
        len(candidate_skills)
    ) * 100

    return round(score, 2)