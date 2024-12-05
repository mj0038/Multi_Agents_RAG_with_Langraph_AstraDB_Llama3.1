from src.search.vectorstore import query_vectorstore

def test_vectorstore():
    """
    Test the vector store query functionality.
    """
    result = query_vectorstore("Tell me about agents", retriever="dummy_retriever")
    assert isinstance(result, list)
