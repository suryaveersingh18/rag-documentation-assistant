from app.graph.state import GraphState
from app.services.llm import get_llm
from app.services.retriever import RetrieverService

retriever = RetrieverService()
llm = get_llm()


def retrieve_documents(state: GraphState):

    question = state["question"]

    documents = retriever.retrieve(question)

    return {
        "documents": documents
    }


def generate_answer(state: GraphState):

    question = state["question"]
    documents = state["documents"]

    context = ""

    for i, doc in enumerate(documents, start=1):
        source = doc.metadata.get("source", "Unknown Source")

        context += f"""
Document {i}
Source: {source}

{doc.page_content}

-------------------------
"""

    prompt = f"""
You are an expert Technical Documentation Assistant.

Use ONLY the documentation below.

If the answer cannot be found in the documentation,
reply exactly:

I couldn't find that information in the documentation.

When answering:

- Be concise.
- Use bullet points where appropriate.
- Mention the source document if available.
- Never make up information.

Documentation:

{context}

Question:

{question}
"""

    response = llm.invoke(prompt)

    # Compatible with old and new LangChain versions
    if isinstance(response.content, list):
        answer = ""

        for block in response.content:
            if block.get("type") == "text":
                answer += block["text"]

    else:
        answer = response.content

    return {
        "answer": answer,
        "documents": documents,
    }