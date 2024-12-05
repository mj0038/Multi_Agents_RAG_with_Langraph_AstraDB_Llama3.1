"""
Module for querying Astra DB vectorstore.
"""
def query_vectorstore(question: str, retriever):
    """
    Query the vector store for relevant documents.

    Args:
        question (str): The user query.
        retriever: The vector store retriever object.

    Returns:
        list: Retrieved documents from Astra DB.
    """
    try:
        documents = retriever.invoke(question)
        return documents
    except Exception as e:
        raise RuntimeError(f"Error querying vector store: {e}")
