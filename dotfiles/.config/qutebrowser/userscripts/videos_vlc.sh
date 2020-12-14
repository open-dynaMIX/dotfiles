#!/bin/bash
# {{@@ header() @@}}

if echo "$QUTE_URL" | grep "youtube.com"; then
    vlc "$QUTE_URL"
else
    xterm -hold -e "youtube-dl -o - ${QUTE_URL} | vlc -"
fi
