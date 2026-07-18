from typing import Annotated

from typing_extensions import TypedDict

from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    State shared across all graph nodes.
    """

    question: str

    documents: list[Document]

    answer: str