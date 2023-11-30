#! bin/bash

WORKING_DIR=/home/ubuntu/AFS_tools/use_cases/webcrawler_chatbot
WEB_ASSET_FILE=$WORKING_DIR/generated/website.json

cd $WORKING_DIR/scrapy/; scrapy startproject website
cp $WORKING_DIR/assets/WebSpider.py $WORKING_DIR/scrapy/website/website/spiders/
cp $WORKING_DIR/assets/items.py $WORKING_DIR/scrapy/website/website/
cd $WORKING_DIR/scrapy/website/website/;scrapy crawl website -o $WEB_ASSET_FILE
