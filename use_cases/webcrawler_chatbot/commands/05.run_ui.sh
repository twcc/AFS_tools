#! bin/bash
WORKING_DIR=/home/ubuntu/AFS_tools/use_cases/webcrawler_chatbot
if lsof -Pi :80 -sTCP:LISTEN -t >/dev/null ; then
  echo "port 80 used"
else
  cd $WORKING_DIR
  python -m streamlit run chat_ui_server.py --server.port 80&
fi
