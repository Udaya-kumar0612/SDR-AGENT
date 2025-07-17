SDR Assistant – AI Agent Solution using langraph

Enhance your AI agent with real-time data extraction and intelligent routing. This SDR Assistant demonstrates tool-augmented reasoning using LangGraph and integrates the Serper API for web search.

Overview: 
This assistant is a single-turn LangGraph agent capable of:

Answering user queries directly via an LLM (OpenAI or Anthropic)
Routing queries to a Serper-powered Google Search Tool when external data is needed
Extracting structured values based on a user-defined schema (JSON format)
Supporting both plain text and JSON response formats
Providing a plug-and-play demo interface via Streamlit

Architecture:
The assistant uses LangGraph to route between an LLM node and a tool node based on the model's decision.

LangGraph Flow Diagram
<img width="600" height="627" alt="image" src="https://github.com/user-attachments/assets/8d759d42-d52d-4b31-962d-3d1bceda39ef" />

Features:
LangGraph-based decision-making
Real-time web search via Serper API
JSON Schema–aware structured response generation
FastAPI backend for API-level integration
Streamlit UI for testing and demo

Setup Instructions
1. Clone the Repository
git clone https://github.com/your-org/sdr-assistant.git
cd sdr-assistant
