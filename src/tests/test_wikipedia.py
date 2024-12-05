from src.search.wikipedia import query_wikipedia

def test_wikipedia():
    """
    Test the Wikipedia query functionality.
    """
    result = query_wikipedia("Tell me about agents")
    assert isinstance(result, str)
