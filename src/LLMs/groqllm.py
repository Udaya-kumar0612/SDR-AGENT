import os
from langchain_groq import ChatGroq

# Fetch API key from environment variable
API_KEY = os.getenv("GROQ_API_KEY")

def get_llm_model():
    """
    Returns an instance of ChatGroq LLM using the Gemma-2 9B model.
    Raises a ValueError if key is missing or connection fails.
    """
    try:
        if not API_KEY:
            raise ValueError("GROQ_API_KEY is missing. Please set it in your environment.")
        
        # Instantiate the LLM (Gemma-2 9B Instruct)
        llm = ChatGroq(model="gemma2-9b-it", api_key=API_KEY)
        return llm

    except Exception as e:
        raise ValueError(f" Error connecting to Groq LLM: {e}")
