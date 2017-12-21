#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}
# If this is executed directly from within qutebrowser with spawn,
# the browser crashes.

if echo "$QUTE_URL" | grep "youtube.com"; then
    vlc "$QUTE_URL"
else
    xterm -hold -e "youtube-dl -o - ${QUTE_URL} | vlc -"
fi
