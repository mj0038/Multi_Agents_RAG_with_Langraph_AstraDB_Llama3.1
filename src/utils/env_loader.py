from dotenv import load_dotenv
import os

# Function to load environment variables
def load_env_vars():
    """
    Load environment variables from the .env file.

    Returns:
        dict: Dictionary containing environment variables.
    """
    load_dotenv()
    return {
        "ASTRA_DB_APPLICATION_TOKEN": os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
        "ASTRA_DB_ID": os.getenv("ASTRA_DB_ID"),
        "GROQ_API_KEY": os.getenv("GROQ_API_KEY"),
    }
