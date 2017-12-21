#!/bin/bash
# This file is managed by dotdrop, only edit it in your dotdrop files!
# If this is executed directly from within qutebrowser with spawn,
# the browser crashes.

if echo "$1" | grep "youtube.com"; then
    vlc "$1"
else
    xterm -hold -e "youtube-dl -o - ${1} | vlc -"
fi
