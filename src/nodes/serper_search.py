import logging
import json
from typing import Dict
from src.state.states import state
from src.tools.search_tool import google_serper_search
from src.LLMs.groqllm import get_llm_model
from langchain_core.runnables import RunnableLambda
from src.prompts.langsmith_prompt import get_prompt, get_prompt_for_json
from langchain_core.language_models import BaseChatModel


# Setup Logger

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger("assistant-module")


#  Google Search Agent

def google_search_agent(state: state) -> state:
    query = state["input"]
    logger.info(f"Running Google search for query: {query}")
    results = google_serper_search(query)
    logger.info(f"Search completed. Results: {results[:100]}...")  # Truncate for readability
    state["search_results"] = results
    state["graph_info"] = "Google search complete with real data."
    return state


#  Assistant Router

def create_assistant(llm: BaseChatModel, tools: list):
    text_prompt = get_prompt()
    json_prompt = get_prompt_for_json()

    def router(state):
        input_text = state.get("input", "")
        format_type = state.get("format", "text")
        fields = state.get("fields", {})

        logger.info(f"Routing input: format={format_type}, fields={fields}")

        if format_type == "json" and fields:
            structured_chain = json_prompt | llm
            try:
                logger.info("Invoking JSON prompt chain...")
                result = structured_chain.invoke({
                    "input": input_text,
                    "fields": fields
                }).content
                result_parsed = json.loads(result)
                logger.info("Structured JSON response parsed successfully.")
            except json.JSONDecodeError as e:
                logger.error(f"JSON decode error: {e}")
                result_parsed = {key: None for key in fields}

            final_output = {
                key: result_parsed.get(key, None) for key in fields
            }

            return {
                "tool_choice": "none",
                "format": format_type,
                "output": final_output
            }

        else:
            chain = text_prompt | llm
            logger.info("Invoking text prompt chain for tool routing...")
            tool_decision = chain.invoke({"input": input_text}).content.lower().strip()
            logger.info(f"Tool decision: {tool_decision}")
            return {
                "tool_choice": tool_decision,
                "format": format_type
            }

    return RunnableLambda(router)


#  Tool Execution Node
def google_tool_node(state: Dict) -> Dict:
    query = state["input"]
    format_type = state.get("format", "text")
    fields = state.get("fields", {})

    logger.info(f"[TOOL NODE] Format: {format_type} | Fields: {fields}")

    if format_type == "json" and fields:
        enriched = {}
        for key, dtype in fields.items():
            search_query = f"{key.replace('_', ' ')} of {query}"
            logger.info(f"→ Searching for: {search_query}")
            result = google_serper_search(search_query)
            enriched[key] = result if result else None
        state["output"] = enriched
    else:
        logger.info("→ Performing basic search...")
        result = google_serper_search(query)
        state["output"] = result

    logger.info("Tool node completed.")
    return state
