"""
Streamlit app module for the Question Answering application.
"""
import streamlit as st
from src.router.routing import route_question
from src.search.vectorstore import query_astra_db, astra_vector_store
from src.search.wikipedia import query_wikipedia


def main():
    st.title("Question Answering App")
    st.write("Ask a question and get answers from either Astra DB or Wikipedia.")

    # User input
    question = st.text_input("Enter your question:")

    # Perform search on button click
    if st.button("Search"):
        if not question.strip():
            st.warning("Please enter a valid question.")
            return

        # Route the question
        try:
            datasource = route_question(question, groq_api_key="YOUR_GROQ_API_KEY")
        except Exception as e:
            st.error(f"Routing error: {e}")
            return

        # Query the appropriate datasource
        if datasource.datasource == "vectorstore":
            st.write("Answer from Astra DB:")
            retriever = astra_vector_store.as_retriever()
            results = query_astra_db(question, retriever)
            if results:
                for idx, doc in enumerate(results):
                    st.write(f"Document {idx + 1}: {doc.page_content}")
            else:
                st.write("No relevant documents found in Astra DB.")
        elif datasource.datasource == "wikisearch":
            st.write("Answer from Wikipedia:")
            result = query_wikipedia(question)
            if result:
                st.write(result)
            else:
                st.write("No relevant results found on Wikipedia.")
