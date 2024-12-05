"""
Module for defining LangGraph workflows.
"""
from langgraph.graph import StateGraph, START, END

def build_workflow(route_question, wiki_search, vectorstore_search):
    """
    Build and compile the LangGraph workflow.

    Args:
        route_question (function): Function to route the question.
        wiki_search (function): Wikipedia search function.
        vectorstore_search (function): Vectorstore search function.

    Returns:
        StateGraph: Compiled workflow object.
    """
    workflow = StateGraph()
    workflow.add_node("wiki_search", wiki_search)
    workflow.add_node("vectorstore", vectorstore_search)

    workflow.add_conditional_edges(
        START, route_question, {
            "wikisearch": "wiki_search",
            "vectorstore": "vectorstore",
        }
    )

    workflow.add_edge("wiki_search", END)
    workflow.add_edge("vectorstore", END)
    return workflow.compile()
