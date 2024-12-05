from src.router.routing import route_question

def test_routing():
    result = route_question("Tell me about Avengers", groq_api_key="dummy_key")
    assert result.datasource in ["vectorstore", "wikisearch"]
