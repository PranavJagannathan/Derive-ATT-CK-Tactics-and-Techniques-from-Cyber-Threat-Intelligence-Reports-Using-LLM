import streamlit as st
import requests
import json
from concurrent.futures import ThreadPoolExecutor

# Set up Streamlit UI
st.set_page_config(page_title="Cyber Threat Intelligence (CTI) Analyzer", layout="wide")
st.title("🔍 Cyber Threat Intelligence (CTI) Analyzer")

# Pre-fill the Ngrok URL (replace with actual Ngrok public URL)
NGROK_URL = "https://4641-35-240-206-219.ngrok-free.app"  # Replace with your actual Ngrok URL

# File uploader for CTI reports
uploaded_file = st.file_uploader("📂 Upload a Cyber Threat Report (TXT, CSV, JSON)", type=["txt", "csv", "json"])

def send_request(file_content):
    try:
        # ✅ Send request as JSON to the Flask API endpoint
        api_endpoint = f"{NGROK_URL}/analyze"
        response = requests.post(api_endpoint, json={"text": file_content}, timeout=180)  # Increase timeout to 180 seconds

        return response

    except requests.exceptions.RequestException as e:
        return f"⚠️ Error: {str(e)}"

if uploaded_file:
    st.info("📤 Processing File...")

    # Read file content as text
    file_content = uploaded_file.read().decode("utf-8")

    # Use ThreadPoolExecutor to avoid blocking the Streamlit app
    with ThreadPoolExecutor() as executor:
        future = executor.submit(send_request, file_content)
        response = future.result()

    if isinstance(response, requests.models.Response):
        if response.status_code == 200:
            st.success("✅ CTI Analysis Complete!")
            structured_report = response.json().get("structured_output", "No structured output available.")

            # Directly display the structured content (raw content)
            st.subheader("🛡️ Structured Threat Intelligence Output")
            st.text_area("📄 Structured Report", structured_report, height=400)

        else:
            st.error(f"❌ Error processing file! {response.text}")

    else:
        st.error(f"⚠️ Failed to process the file.\n\nError: {response}")

