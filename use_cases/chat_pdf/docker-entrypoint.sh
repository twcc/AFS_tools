#! bin/bash
cd /opt/app
pip install -r requirements.txt

streamlit run chat.py --server.port 8501