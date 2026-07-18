import os
from pathlib import Path

os.environ.setdefault(
    "USER_AGENT",
    "RAG-Technical-Documentation-Assistant/1.0",
)

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
)


class DocumentLoader:

    @staticmethod
    def load_pdf(file_path: str):
        loader = PyPDFLoader(file_path)
        return loader.load()

    @staticmethod
    def load_markdown(file_path: str):
        loader = TextLoader(file_path, encoding="utf-8")
        return loader.load()

    @staticmethod
    def load_website(url: str):
        loader = WebBaseLoader(url)
        return loader.load()

    @staticmethod
    def load(source: str):
        """
        Automatically detect document type.
        """

        if source.startswith("http://") or source.startswith("https://"):
            return DocumentLoader.load_website(source)

        suffix = Path(source).suffix.lower()

        if suffix == ".pdf":
            return DocumentLoader.load_pdf(source)

        if suffix in [".md", ".txt"]:
            return DocumentLoader.load_markdown(source)

        raise ValueError(f"Unsupported document type: {suffix}")