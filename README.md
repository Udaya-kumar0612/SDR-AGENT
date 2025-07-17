🤖 SDR Assistant – Outbound Technical Test Solution
Enhance your AI agents with real-time data extraction and intelligent decision-making. This SDR Assistant is designed to demonstrate tool-augmented reasoning using a LangGraph-based single-turn agent, integrated with the Serper API for web search.

🌟 Overview
This project is a fully working Single-Turn SDR Assistant that uses OpenAI (or Anthropic), LangGraph, and LangChain. It can:

✨ Answer user queries directly via LLM

🔍 Route queries to a Serper Google Search Tool when company or profile data is needed

📦 Return responses in plain text or structured JSON format

🧠 Perform schema-driven field extraction from unstructured web data

Supports a plug-and-play Streamlit UI for demo.

🎬 Demo
Try it live via the Streamlit UI:

🔗 Run backend: http://127.0.0.1:8000/run

💻 Run UI: http://localhost:8501

Use dropdown to switch between text or json output modes and test structured query understanding.

✨ Features
⚙️ LangGraph-based decision-making

📡 Serper API integration (real-time Google Search)

🧠 JSON Schema-Aware response generation

💬 Streamlit chatbot interface with format toggle

🚀 FastAPI backend endpoint for automation or integration

🚀 Quickstart
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-repo/sdr-ai-assistant.git
cd sdr-ai-assistant
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Dependencies Used:
langchain, langgraph, openai or anthropic

fastapi, uvicorn, streamlit

requests, pydantic, python-dotenv

3. Set Environment Variables
Create a .env file:

ini
Copy
Edit
SERPER_API_KEY=your-serper-api-key
OPENAI_API_KEY=your-openai-key
🔧 Running the Application
A. Run Backend (FastAPI)
bash
Copy
Edit
uvicorn src.main:app --reload
Runs on: http://127.0.0.1:8000/run

B. Run UI (Streamlit)
bash
Copy
Edit
streamlit run ui.py
💡 How to Use
🗣️ text Mode
Simple Q&A powered by LLMs:

json
Copy
Edit
{
  "input": "What does Freshworks do?",
  "format": "text"
}
Returns natural language answer.

📋 json Mode
Extract structured values into a schema:

Input:

json
Copy
Edit
{
  "input": "Get me company details for Freshworks",
  "format": "json",
  "fields": {
    "company_name": "string",
    "industry": "string",
    "hq_location": "string",
    "short_description": "string"
  }
}
Output:

json
Copy
Edit
{
  "company_name": "Freshworks",
  "industry": "Software",
  "hq_location": "San Mateo, California",
  "short_description": "Freshworks is a customer engagement SaaS company."
}
If data is not found, the value will be null.

🧪 Sample JSON Prompts
Paste this into the Streamlit JSON schema field:

json
Copy
Edit
{
  "full_name": "string",
  "position": "string",
  "company": "string",
  "years_of_experience": "number",
  "industry_expertise": "string"
}
📦 Endpoint Summary
URL	Method	Description
/run	POST	Accepts input, returns response

🔐 Security Note
Always validate and sanitize web-sourced data.

Avoid inserting raw scraped text directly into prompts.

Use structured formats where possible.

🛠 Future Improvements
Add memory for multi-turn dialogue

Add more tools (e.g. Crunchbase, LinkedIn scraping)

Add LangSmith tracing

Extend output types (e.g. markdown, CSV)

📞 Support
If you need help or want to contribute, raise an issue or reach out via the project repository.