import json
from collections import Counter
from tqdm import tqdm

DATASET_PATH = "data/candidates.jsonl"

countries = Counter()
titles = Counter()
skills = Counter()

candidate_count = 0

with open(DATASET_PATH, "r") as f:
    for line in tqdm(f):
        candidate = json.loads(line)

        profile = candidate.get("profile", {})

        countries[profile.get("country", "Unknown")] += 1

        titles[profile.get("current_title", "Unknown")] += 1

        for skill in candidate.get("skills", []):
            skills[skill.get("name", "")] += 1

        candidate_count += 1

print("\nTotal Candidates:", candidate_count)

print("\nTop Countries")
for country, count in countries.most_common(10):
    print(country, count)

print("\nTop Titles")
for title, count in titles.most_common(20):
    print(title, count)

print("\nTop Skills")
for skill, count in skills.most_common(30):
    print(skill, count)