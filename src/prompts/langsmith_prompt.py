import logging
from langsmith.client import Client
from config import LANGSMITH_API_KEY

# Setup logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("prompt-loader")

# Initialize LangSmith client
client = Client(api_key=LANGSMITH_API_KEY)

def get_prompt():
    """
    Pulls the default prompt template used for text-based responses.
    Returns:
        ChatPromptTemplate: LangChain-compatible prompt object for normal queries.
    """
    try:
        logger.info("Fetching prompt: 'sdragent_prompt'")
        return client.pull_prompt("sdragent_prompt")
    except Exception as e:
        logger.error(f"Failed to fetch 'sdragent_prompt': {e}")
        raise

def get_prompt_for_json():
    """
    Pulls the prompt template used for structured JSON extraction.
    Returns:
        ChatPromptTemplate: LangChain-compatible prompt object for JSON mode.
    """
    try:
        logger.info("Fetching prompt: 'sdragent_json_prompt'")
        return client.pull_prompt("sdragent_json_prompt")
    except Exception as e:
        logger.error(f"Failed to fetch 'sdragent_json_prompt': {e}")
        raise
