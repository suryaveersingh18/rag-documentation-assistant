from langchain_core.documents import Document

from app.core.config import get_settings
from app.services.vector_store import get_vector_store


class RetrieverService:

    def __init__(self):
        self.settings = get_settings()

        self.vector_store = get_vector_store()

    def retrieve(
        self,
        query: str,
    ) -> list[Document]:

        retriever = self.vector_store.as_retriever(
            search_kwargs={
                "k": self.settings.top_k
            }
        )

        return retriever.invoke(query)