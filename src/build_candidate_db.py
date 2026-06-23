import json
import pickle
from tqdm import tqdm

candidate_db = {}

with open("data/candidates.jsonl") as f:
    for line in tqdm(f):
        c = json.loads(line)
        candidate_db[c["candidate_id"]] = c

with open("artifacts/candidate_db.pkl", "wb") as f:
    pickle.dump(candidate_db, f)

print("Saved:", len(candidate_db))