#! bin/bash

WORKING_DIR=/home/ubuntu/AFS_tools/use_cases/webcrawler_chatbot
COMMAND_DIR=$WORKING_DIR/commands


bash $COMMAND_DIR/01.backup-assets.sh  
bash $COMMAND_DIR/02.crawling.sh  
bash $COMMAND_DIR/03.build_embedding.sh  
bash $COMMAND_DIR/04.run_api.sh  
bash $COMMAND_DIR/05.run_ui.sh

sleep infinity
