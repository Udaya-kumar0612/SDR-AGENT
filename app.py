import streamlit as st
import requests
import json

# Set up page title and icon
st.set_page_config(page_title="SDR AI Assistant", page_icon="")
st.title("SDR Assistant Demo")

# User input for query and response format
query = st.text_input("Enter your question:")
format_option = st.selectbox("Select response format", ["text", "json"])

# Show JSON input only when JSON format is selected
fields_input = None
if format_option == "json":
    fields_input = st.text_area(
        "Paste your `fields` JSON here",
        height=200,
        placeholder='{\n  "company_name": "string",\n  "industry": "string",\n  "hq_location": "string",\n  "short_description": "string"\n}',
    )

# Handle form submission
if st.button("Ask"):
    if query.strip() == "":
        st.warning(" Please enter a query.")
    elif format_option == "json" and not fields_input.strip():
        st.warning("Please paste your `fields` JSON.")
    else:
        try:
            # Prepare request payload
            payload = {
                "input": query,
                "format": format_option
            }

            if format_option == "json":
                try:
                    fields = json.loads(fields_input)
                    payload["fields"] = fields
                except json.JSONDecodeError:
                    st.error("Invalid JSON format in `fields`. Please fix it.")
                    st.stop()

            # Send request to backend
            try:

                response = requests.post("http://127.0.0.1:8000/api/sdragent", json=payload)
                result = response.json()

            except requests.exceptions.RequestException as e:
                st.error("Unable to connect to the backend API. Please make sure the server is running.")

            # Display results
            if "error" in result:
                st.error(f" Error: {result['error']}")
            elif "output" in result:
                if result["format"] == "json":
                    st.json(result["output"])  # Pretty JSON render
                else:
                    st.success(result["output"])  # Plain text
            else:
                st.warning(" No response found.")

        except Exception as e:
            st.error(f"Request failed: {str(e)}")
