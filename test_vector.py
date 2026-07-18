from app.services.retriever import RetrieverService

retriever = RetrieverService()

query = "How do I create a FastAPI application?"

documents = retriever.retrieve(query)

print(f"\nFound {len(documents)} documents.\n")

for i, doc in enumerate(documents, start=1):
    print("=" * 80)
    print(f"Document {i}")

    if "source" in doc.metadata:
        print(f"Source : {doc.metadata['source']}")

    print("\nContent:\n")
    print(doc.page_content[:600])
    print("\n")