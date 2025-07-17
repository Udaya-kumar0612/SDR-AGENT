import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langsmith import traceable
from src.state.states import state
from src.graph.graph_builder import build_graph

# Load Environment Variables 
load_dotenv()

LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT_NAME = os.getenv("LANGSMITH_PROJECT_NAME")

# Setup Logging 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("SDR-Api")

# Initialize FastAPI 
app = FastAPI()

# Build the LangGraph 
graph = build_graph()
logger.info("Graph initialized successfully.")

# Enable CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Schema
class SDRRequest(BaseModel):
    input: dict | str

# Endpoint 
@app.post("/api/sdragent")
@traceable(name="run_agent", project_name=LANGSMITH_PROJECT_NAME)
async def run_agent(request: Request):
    try:
        logger.info("Received request at /api/sdragent")
        body = await request.json()
        userquery = body.get("input")
        format_type = body.get("format", "text")
        fields = body.get("fields", {})

        logger.info(f"User query: {userquery}")
        logger.info(f"Requested format: {format_type}")
        logger.debug(f"Fields: {fields}")

        input_state: state = {
            "input": userquery,
            "format": format_type,
            "fields": fields,
            "tool_response": None,
            "output": None
        }

        logger.info("Invoking LangGraph...")
        final_state = graph.invoke(
            input_state,
            config={"tracing": True, "project_name": LANGSMITH_PROJECT_NAME}
        )
        logger.info("Graph execution completed successfully.")
        return final_state

    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        return {"success": False, "error": f"ValueError: {str(ve)}"}
    except KeyError as ke:
        logger.error(f"Missing key: {ke}")
        return {"success": False, "error": f"Missing key: {str(ke)}"}
    except Exception as e:
        logger.exception("Unexpected error occurred")
        return {"success": False, "error": str(e)}
