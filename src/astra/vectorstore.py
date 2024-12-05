"""
Module for querying Astra DB (vectorstore).
"""
from langchain_community.vectorstores import Cassandra
from langchain_huggingface import HuggingFaceEmbeddings
from cassio import init
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_ID = os.getenv("ASTRA_DB_ID")

# Initialize Cassio for AstraDB
init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

# Initialize the embedding function
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize the Astra DB vector store
astra_vector_store = Cassandra(
    embedding=embedding_function,
    table_name="qa_mini_demo",
    session=None,  # Cassio will handle session management
    keyspace=None
)

# Function to query Astra DB
def query_astra_db(question: str, retriever):
    """
    Query the vector store for relevant documents.

    Args:
        question (str): The user query.
        retriever: The Astra DB retriever object.

    Returns:
        list: Retrieved documents from Astra DB.
    """
    try:
        documents = retriever.invoke(question)
        return documents
    except Exception as e:
        raise RuntimeError(f"Error querying Astra DB: {e}")
