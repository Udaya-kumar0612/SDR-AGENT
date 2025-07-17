import os
import requests
import logging
from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode
from src.state.states import state

# Load environment variables 
load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Setup Logging 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("serper-tool")

def google_serper_search(query: str) -> str:
    """
    Search Google using the Serper API and return a summarized snippet.
    """
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json",
    }
    data = {"q": query}

    try:
        logger.info(f"Sending Serper search request for query: {query}")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        results = response.json()
        logger.debug(f"Raw Serper response: {results}")

        if results.get("organic"):
            top_results = results["organic"][:5]
            snippets = [res.get("snippet", "") for res in top_results if res.get("snippet")]
            combined = "\n".join(f"- {s}" for s in snippets)
            logger.info("Successfully retrieved and summarized search snippets.")
            return combined or "No relevant snippets found."

        logger.warning("Serper returned no organic results.")
        return "No relevant results found."

    except requests.RequestException as e:
        logger.error(f"Serper API request failed: {e}")
        return f"Request failed: {str(e)}"
    except Exception as e:
        logger.exception("Unexpected error in Serper search.")
        return f"Unexpected error: {str(e)}"

def create_tool_node(tools):
    """
    Wrap tools into a LangGraph ToolNode.
    """
    logger.info("Creating ToolNode with provided tools.")
    return ToolNode(tools=tools)
