from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import get_settings


@lru_cache
def get_embedding_model():
    """
    Singleton embedding model.
    """

    settings = get_settings()

    return HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        },
    )