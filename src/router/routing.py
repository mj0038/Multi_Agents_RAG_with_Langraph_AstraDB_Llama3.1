"""
Module for routing user queries to either Astra DB (vectorstore) or Wikipedia.
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_groq import ChatGroq
from typing import Literal

class RouteQuery(BaseModel):
    """
    Schema for routing user queries to the most relevant datasource.
    """
    datasource: Literal["vectorstore", "wikisearch"] = Field(
        ..., description="Route query to either vectorstore or Wikipedia search."
    )

def route_question(question: str, groq_api_key: str) -> RouteQuery:
    """
    Routes a user's question to either the vectorstore or Wikipedia.

    Args:
        question (str): The user query.
        groq_api_key (str): API key for the LLM.

    Returns:
        RouteQuery: Decision between "vectorstore" or "wikisearch".
    """
    try:
        llm = ChatGroq(groq_proxy=groq_api_key, model_name="Llama-3.1-70b-Versatile")
        structured_llm_router = llm.with_structured_output(RouteQuery)

        route_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "Route user questions to either vectorstore or Wikipedia."),
                ("human", "{question}")
            ]
        )

        question_router = route_prompt | structured_llm_router
        return question_router.invoke({"question": question})
    except Exception as e:
        raise RuntimeError(f"Failed to route the question: {e}")
