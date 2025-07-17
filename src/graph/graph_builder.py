import os
import logging
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from src.state.states import state
from src.nodes.serper_search import google_search_agent, create_assistant, google_tool_node
from src.router.agent_route import route_decision
from src.LLMs.groqllm import get_llm_model

# Load environment variables
load_dotenv()


# Setup Logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger("graph-builder")

def build_graph():
    """
    Builds the main LangGraph execution pipeline.
    
    - Initializes assistant node with LLM.
    - Adds a Google Search tool node.
    - Conditionally routes based on model decision.
    - Exports Mermaid diagram for debugging/visualization.
    """
    logger.info("Starting to build LangGraph...")

    # Load Groq LLM
    llm = get_llm_model()
    logger.info(" Groq LLM loaded.")

    # Create assistant node
    assistant_node = create_assistant(llm, google_search_agent)
    logger.info("Assistant node created.")

    # Define tool node
    tool_node = google_tool_node
    logger.info("Tool node ready.")

    # Initialize LangGraph builder
    builder = StateGraph(state)

    # Add nodes
    builder.add_node("AI Assistant", assistant_node)
    builder.add_node("tools", tool_node)
    logger.info(" Nodes added to graph.")

    #  Add routing logic
    builder.add_edge(START, "AI Assistant")
    builder.add_conditional_edges(
        "AI Assistant",
        route_decision,
        {
            "tools": "tools",
            "none": END
        }
    )
    builder.add_edge("tools", END)
    logger.info("Edges and routing configured.")

    # Export Mermaid diagram
    graph_builder = builder.compile()

    #for graph Visualization
    """mermaid_str = graph_builder.get_graph().draw_mermaid()
    with open("graph.md", "w") as f:
        f.write("```mermaid\n" + mermaid_str + "\n```")
    logger.info("Mermaid graph exported to graph.md.")"""

    return graph_builder
