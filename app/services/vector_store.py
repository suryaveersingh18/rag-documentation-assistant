from functools import lru_cache

from langchain_chroma import Chroma

from app.core.config import get_settings
from app.services.embeddings import get_embedding_model


@lru_cache
def get_vector_store():
    """
    Singleton Chroma vector store.
    """

    settings = get_settings()

    embedding_model = get_embedding_model()

    return Chroma(
        persist_directory=settings.chroma_db,
        embedding_function=embedding_model,
        collection_name=settings.collection_name,
    )