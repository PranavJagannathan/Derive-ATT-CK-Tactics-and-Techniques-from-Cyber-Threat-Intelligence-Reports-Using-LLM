# Derive-ATT-CK-Tactics-and-Techniques-from-Cyber-Threat-Intelligence-Reports-Using-LLM
🔍 Overview
The CTI Analyzer is a web-based tool that helps cybersecurity professionals analyze threat reports using AI. It extracts key information such as MITRE ATT&CK Tactics & Techniques, Indicators of Compromise (IOCs), and severity scores to generate structured intelligence reports.

✨ Features
✅ Upload cyber threat reports (CSV format)
✅ Extract MITRE ATT&CK Tactics & Techniques
✅ Identify Indicators of Compromise (IOCs)
✅ Generate structured threat intelligence reports
✅ AI-powered analysis using Gemini API 🤖
✅ Web-based Streamlit UI 🌐
✅ Flask backend with Ngrok tunneling 🛠️

🛠️ Technologies Used
🐍 Python
🌍 Flask
📊 Streamlit
🔗 Ngrok
🧠 Gemini AI Model
📡 Pyngrok
📑 Pandas

⚙️ Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-repo/cti-analyzer.git
cd cti-analyzer
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Start the Flask Server 🚀
bash
Copy
Edit
python app.py
4️⃣ Expose Server Using Ngrok 🌍
bash
Copy
Edit
ngrok http 5000
5️⃣ Run the Streamlit App 🎨
bash
Copy
Edit
streamlit run streamlit_app.py
📌 Usage
1️⃣ Open the Streamlit web UI in your browser.
2️⃣ Upload a cyber threat intelligence report (CSV file).
3️⃣ Click on the Analyze button.
4️⃣ View the extracted intelligence in a structured format.

❓ Troubleshooting
⚠️ Flask not running? Start Flask before running Ngrok.
⚠️ Ngrok errors? Restart with:

bash
Copy
Edit
ngrok kill
ngrok http 5000
⚠️ Dependency issues? Try updating:

bash
Copy
Edit
pip install --upgrade -r requirements.txt
