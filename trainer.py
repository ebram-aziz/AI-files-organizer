import os
import json
import pickle
import faiss
import numpy as np

from src.extractor import *
from src.ocr import ocr_pdf
from src.embeddings import create_embedding

DIMENSION = 384

def train():

    vectors = []
    labels = []

    with open("config/categories.json") as f:
        categories = json.load(f)

    for category in categories:

        folder = f"training_data/{category}"

        if not os.path.exists(folder):
            continue

        for file in os.listdir(folder):

            path = os.path.join(folder, file)

            text = ""

            if file.endswith(".pdf"):
                text = extract_pdf(path)

                if len(text.strip()) < 50:
                    text = ocr_pdf(path)

            if not text:
                continue

            embedding = create_embedding(text[:5000])

            vectors.append(embedding)
            labels.append(category)

    vectors = np.array(vectors).astype("float32")

    index = faiss.IndexFlatIP(DIMENSION)
    index.add(vectors)

    faiss.write_index(
        index,
        "data/models/index.faiss"
    )

    with open("data/models/labels.pkl", "wb") as f:
        pickle.dump(labels, f)