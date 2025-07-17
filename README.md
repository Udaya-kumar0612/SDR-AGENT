SDR Assistant – AI Agent Solution Using Langraph

Enhance your AI agent with real-time data extraction and intelligent routing. This SDR Assistant demonstrates tool-augmented reasoning using LangGraph and integrates the Serper API for web search.

Overview: 
This assistant is a single-turn LangGraph agent capable of:
•	Answering user queries directly via an LLM (OpenAI or Anthropic)
•	Routing queries to a Serper-powered Google Search Tool when external data is needed
•	Extracting structured values based on a user-defined schema (JSON format)
•	Supporting both plain text and JSON response formats
•	Providing a plug-and-play demo interface via Streamlit

Architecture:

The assistant uses LangGraph to route between an LLM node and a tool node based on the model's decision.

Langgraph Flow Diagram :

<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/8d759d42-d52d-4b31-962d-3d1bceda39ef" />

Features:

•	LangGraph-based decision-making
•	Real-time web search via Serper API
•	JSON Schema–aware structured response generation
•	FastAPI backend for API-level integration
•	Streamlit UI for testing and demo
•	LangSmith Tracing for observability and performance analysis



Setup Instructions:

1.	Clone the Repository
git clone https://github.com/Udaya-kumar0612/SDR-AGENT.git

Install Dependencies:

pip install -r requirements.txt
Required packages:
•	langchain, langgraph, openai or anthropic
•	fastapi, uvicorn, streamlit
•	requests, pydantic, python-dotenv

Environment Configuration:

Create a .env file with the following keys:

SERPER_API_KEY=”serper-api-key”
OPENAI_API_KEY=”openai-api-key”
LANGSMITH_API_KEY=”langsmith-api-key”
LANGSMITH_PROJECT_NAME=”Proj_name”

Running the Application

1. Start the Backend (FastAPI)
uvicorn src.main:app --reload
Runs at: http://127.0.0.1:8000/run
2. Start the Frontend (Streamlit UI)
streamlit run ui.py
Runs at: http://localhost:8501

Tracing & Observability:

LangSmith is integrated for tracing all agent runs, decisions, and tool usage.
•	View step-by-step flow of input through LangGraph
•	Debug model decisions and tool executions
•	Track performance metrics and token usage
Note: Tracing is enabled in the main.py FastAPI endpoint via the @traceable decorator to capture full pipeline execution.

Project Code Structure:
	 
<img width="909" height="703" alt="image" src="https://github.com/user-attachments/assets/11d32c6b-df67-4a29-aff0-b597a082d826" />


Usage:
1.	Text Query and Response
   <img width="940" height="124" alt="image" src="https://github.com/user-attachments/assets/3287ae70-e6f2-4d27-a5f1-4dbccac0703a" />
  Returns a Raw text response.

2.	JSON Query:
   <img width="940" height="232" alt="image" src="https://github.com/user-attachments/assets/a3c35938-17ec-426f-865d-8f2aac77eb16" />
   
  Json Response:
  <img width="943" height="190" alt="image" src="https://github.com/user-attachments/assets/e9c4e8fd-b9ea-411b-adeb-8e01e71f6a03" />

 

API Summary:

Endpoint :  /api/sdragent
Method : POST
Description : Accepts user input and returns formatted response

Security Notes:

•	Always validate and sanitize input and output.
•	Avoid passing raw unstructured search results into prompts.
•	Use structured schema wherever possible.	  
	





