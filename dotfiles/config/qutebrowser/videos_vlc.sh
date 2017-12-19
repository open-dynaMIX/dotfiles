#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}
# If this is executed directly from within qutebrowser with spawn,
# the browser crashes.

if echo "$1" | grep "youtube.com"; then
    vlc "$1"
else
    xterm -hold -e "youtube-dl -o - ${1} | vlc -"
fi
