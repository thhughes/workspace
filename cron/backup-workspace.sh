#!/bin/bash

SOURCE_DIR="$_ws_mgr"
DEST_DIR="$_ws_staged"
_local_ws_log="$_ws_staged/logs/backup-workspace.log"

if [ -e "$_local_ws_log" ]; then
    rm $_local_ws_log
fi

if [ ! -d "$SOURCE_DIR" ]; then
    echo "$(date): Error: Source directory does not exist" >> $_local_ws_log
    exit 1
fi

ZIP_NAME=$(basename "$SOURCE_DIR").zip
ZIP_PATH="$DEST_DIR/$ZIP_NAME"
ZIP_BKP=$ZIP_PATH.bkp

if [ -f "$ZIP_BKP" ]; then
    rm "$ZIP_BKP"
    echo "$(date): Removed existing zip backup: $ZIP_BKP" >> $_local_ws_log
fi

if [ -f "$ZIP_PATH" ]; then
    mv "$ZIP_PATH" "$ZIP_BKP"
    echo "$(date): Moved $ZIP_PATH to $ZIP_BKP" >> $_local_ws_log
fi

if zip -r "$ZIP_PATH" "$SOURCE_DIR"; then
    echo "$(date): Successfully zipped $SOURCE_DIR to $ZIP_PATH" >> $_local_ws_log
else
    echo "$(date): Error: Failed to create zip file" >> $_local_ws_log
    exit 1
fi