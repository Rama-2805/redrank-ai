import faiss
import numpy as np

print("Loading embeddings...")

embeddings = np.load(
    "artifacts/candidate_embeddings.npy"
).astype("float32")

print("Shape:", embeddings.shape)

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

print("Building index...")

index.add(embeddings)

print("Total vectors:", index.ntotal)

faiss.write_index(
    index,
    "artifacts/faiss.index"
)

print("Index saved.")