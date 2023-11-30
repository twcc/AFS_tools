#!/bin/bash
WORKING_DIR=/home/ubuntu/AFS_tools/use_cases/webcrawler_chatbot
COMMAND=${1:-start}

case "$COMMAND" in
  start)
    if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
      echo "port 8000 used"
    else
      cd $WORKING_DIR
      uvicorn chat_api_server:app --host 0.0.0.0 --port 8000&
    fi
    ;;
  stop)
    kill $(lsof -t -i:8000)
    ;;
  restart)
    kill $(lsof -t -i:8000)
    sleep 2
    cd $WORKING_DIR
    uvicorn chat_api_server:app --host 0.0.0.0 --port 8000&
    ;;
  status)
    if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
      echo "API Server is running"
    else
      echo "API Server is not running"
    fi
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|status}"
    exit 1
esac