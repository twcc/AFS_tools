#! bin/bash
cd /home/ubuntu
if [ -d "AFS_tools" ]; then
  echo "AFS_tools exist"
else
  git clone https://github.com/twcc/AFS_tools.git
  cd AFS_tools/use_cases/webcrawler_chatbot/scrapy/
  pip install -r requirements.txt
  sudo apt install python3-scrapy
  scrapy startproject website
  cd /home/ubuntu
  cp AFS_tools/use_cases/webcrawler_chatbot/assets/WebSpider.py AFS_tools/use_cases/webcrawler_chatbot/scrapy/website/website/spiders/
  cp AFS_tools/use_cases/webcrawler_chatbot/assets/items.py AFS_tools/use_cases/webcrawler_chatbot/scrapy/website/website/
  cd AFS_tools/use_cases/webcrawler_chatbot/scrapy/website/website/
  scrapy crawl website -o website.json
  cd /home/ubuntu/AFS_tools/use_cases/webcrawler_chatbot
  apk add build-base libressl-dev libffi-dev
  pip install -r requirements.txt
  python load_embedding_website.py
  
fi
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
  echo "port 8000 used"
else
  uvicorn chat_api_server:app --host 0.0.0.0 --port 8000&
fi
if lsof -Pi :80 -sTCP:LISTEN -t >/dev/null ; then
  echo "port 80 used"
else
  python -m streamlit run chat_ui_server.py --server.port 80&
fi
sleep infinity
