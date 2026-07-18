import streamlit as st

from api import ask_question, ingest_source
from components import show_sources

st.set_page_config(
    page_title="RAG Technical Documentation Assistant",
    page_icon="📘",
    layout="wide"
)

st.title("📘 RAG Technical Documentation Assistant")

st.caption("Powered by FastAPI + LangGraph + Gemini + ChromaDB")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    st.header("📄 Ingest Documentation")

    source = st.text_input(
        "Website URL / PDF Path / Markdown Path"
    )

    if st.button("Ingest"):

        if source:

            with st.spinner("Indexing..."):

                result = ingest_source(source)
                if "error" in result:
                    st.error(
                        "Unable to ingest the documentation.\n\n"
                        "Please check the URL or file path."
                    )
                else:
                    st.success("Documentation indexed successfully!")

st.divider()

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            show_sources(
                message.get("sources", [])
            )

prompt = st.chat_input("Ask a question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = ask_question(prompt)

            answer = response["answer"]

            sources = response["sources"]

            st.markdown(answer)

            show_sources(sources)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources,
        }
    )
