from sentence_transformers import SentenceTransformer
from config.settings import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def create_embedding(text):

    return model.encode(
        text,
        normalize_embeddings=True
    )