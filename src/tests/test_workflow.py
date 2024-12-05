from src.workflows.workflow import build_workflow

def test_workflow():
    workflow = build_workflow(route_question, wiki_search, vectorstore_search)
    assert workflow
