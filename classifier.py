import faiss
import pickle

from src.embeddings import create_embedding

index = faiss.read_index(
    "data/models/index.faiss"
)

labels = pickle.load(
    open(
        "data/models/labels.pkl",
        "rb"
    )
)

def classify(text):

    embedding = create_embedding(text[:5000])

    D, I = index.search(
        embedding.reshape(1, -1),
        1
    )

    score = float(D[0][0])

    category = labels[I[0][0]]

    return category, score