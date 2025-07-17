SDR Assistant – Ai Agents
Enhance your AI agents with real-time data extraction and intelligent decision-making. This SDR Assistant demonstrates tool-augmented reasoning using a LangGraph-based single-turn agent, integrated with the Serper API for web search.

Overview
This project is a fully functional Single-Turn SDR Assistant built with:

OpenAI (or Anthropic)

LangGraph + LangChain

FastAPI + Streamlit

It can:

Answer user queries directly via an LLM

Route queries to a Google Search Tool (via Serper API) when real-world or company data is needed

Return responses in either plain text or structured JSON format

Perform schema-driven field extraction from unstructured web data

Run locally with a Streamlit UI for demonstration

Demo
You can test the assistant locally:

Run Backend: http://127.0.0.1:8000/run

Run UI: http://localhost:8501

Use the dropdown in the UI to switch between text and json modes to test schema-based output.

Features
LangGraph-based conditional execution with state management

Serper API integration for real-time search

Structured JSON output using prompt-guided extraction

Simple FastAPI backend

Streamlit UI for testing queries and schemas

LangSmith tracing enabled for observability

Local structured logging for debugging

