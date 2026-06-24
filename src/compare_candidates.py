def compare_candidates(c1, c2):

    return f"""
### Candidate Comparison

Candidate 1
------------
Title: {c1['title']}
Experience: {c1['experience']} years
Skills: {', '.join(c1['skills'])}

Candidate 2
------------
Title: {c2['title']}
Experience: {c2['experience']} years
Skills: {', '.join(c2['skills'])}

Recommendation:
Choose the candidate whose skills align most closely with the job requirements.
"""