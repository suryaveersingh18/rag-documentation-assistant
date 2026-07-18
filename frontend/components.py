import streamlit as st


def show_sources(sources):

    if not sources:
        return

    st.markdown("### 📚 Sources")

    for source in sources:
        st.markdown(f"- {source}")