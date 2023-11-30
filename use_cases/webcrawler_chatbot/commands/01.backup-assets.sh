#! bin/bash

WORKING_DIR=/home/ubuntu/AFS_tools/use_cases/webcrawler_chatbot

# Get the current date and time
CURRENT_DATE=$(date +"%Y%m%d%H%M%S")
# Define the backup directory with date and time stamp
BACKUP_DIR="$WORKING_DIR/backup/generated_$CURRENT_DATE"

# Create the backup directory
mkdir -p $BACKUP_DIR
# Copy the contents of the generated directory to the backup directory
cp -r $WORKING_DIR/generated/* $BACKUP_DIR/
# Remove the contents of the generated directory
rm -rf $WORKING_DIR/generated/*
