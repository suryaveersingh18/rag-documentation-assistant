from app.ingestion.loader import DocumentLoader
from app.ingestion.splitter import get_text_splitter
from app.services.vector_store import get_vector_store


class IngestionPipeline:

    def __init__(self):
        self.vector_store = get_vector_store()
        self.splitter = get_text_splitter()

    def ingest(self, source: str):

        print(f"\nLoading: {source}")

        docs = DocumentLoader.load(source)

        print(f"Loaded {len(docs)} documents")

        chunks = self.splitter.split_documents(docs)

        print(f"Created {len(chunks)} chunks")


        self.vector_store.add_documents(chunks)

        print("Stored inside ChromaDB\n")