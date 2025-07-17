import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# API Keys - Make sure to set these in your .env file
SERPER_API_KEY = os.getenv("SERPER_API_KEY")            # For Google search via Serper API
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")      # For loading prompts from LangSmith
GROQ_API_KEY = os.getenv("GROQ_API_KEY")                 # For using Groq's LLMs
LANGSMITH_PROJ_NAME=os.getenv("LANGSMITH_PROJECT_NAME")  # For tracing metrics in langsmith
