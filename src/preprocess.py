import json
from tqdm import tqdm

DATASET_PATH = "data/candidates.jsonl"

def build_candidate_text(candidate):
    profile = candidate.get("profile", {})

    headline = profile.get("headline", "")
    summary = profile.get("summary", "")

    skills = []
    for skill in candidate.get("skills", []):
        skills.append(skill.get("name", ""))

    career_text = []
    for job in candidate.get("career_history", []):
        career_text.append(
            f"{job.get('title','')} "
            f"{job.get('description','')}"
        )

    combined_text = f"""
    {headline}

    {summary}

    Skills:
    {' '.join(skills)}

    Career:
    {' '.join(career_text)}
    """

    return combined_text.strip()


def main():
    count = 0

    with open(DATASET_PATH, "r") as f:
        for line in tqdm(f):
            candidate = json.loads(line)

            text = build_candidate_text(candidate)

            if count < 3:
                print("=" * 80)
                print(candidate["candidate_id"])
                print(text[:1000])

            count += 1

    print(f"\nLoaded {count} candidates")


if __name__ == "__main__":
    main()