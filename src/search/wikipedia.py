"""
Module for querying Wikipedia for information.
"""
from langchain_community.utilities import WikipediaAPIWrapper

def query_wikipedia(question: str):
    """
    Query Wikipedia for relevant information.

    Args:
        question (str): The user query.

    Returns:
        str: Summary retrieved from Wikipedia.
    """
    try:
        api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
        return api_wrapper.run(question)
    except Exception as e:
        raise RuntimeError(f"Error querying Wikipedia: {e}")
