import json

TARGET_ID = "CAND_0018499"

with open("data/candidates.jsonl", "r") as f:
    for line in f:
        candidate = json.loads(line)

        if candidate["candidate_id"] == TARGET_ID:

            print("=" * 80)
            print("CANDIDATE ID:", candidate["candidate_id"])
            print("=" * 80)

            print("\nPROFILE")
            print(candidate.get("profile", {}))

            print("\nSKILLS")
            for skill in candidate.get("skills", []):
                print(skill)

            print("\nCAREER HISTORY")
            for job in candidate.get("career_history", []):
                print(job)

            print("\nREDROB SIGNALS")
            print(candidate.get("redrob_signals", {}))

            break