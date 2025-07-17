import logging
from typing import Dict
from src.state.states import state

# Setup Logging 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("graph-router")

def route_decision(state: Dict) -> str:
    """
    Routes based on the LLM's decision.

    Args:
        state (dict): The current state with `tool_choice` key.

    Returns:
        str: Either "tools" or "none", directing the graph path.
    """
    tool_choice = state.get("tool_choice", "none")
    logger.info(f"Routing decision based on tool_choice: {tool_choice}")
    return tool_choice
