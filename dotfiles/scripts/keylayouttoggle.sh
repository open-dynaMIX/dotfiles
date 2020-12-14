#!/usr/bin/bash
# {{@@ header() @@}}
#

if setxkbmap -query | grep layout | grep -q ch; then
    setxkbmap el
else
    setxkbmap ch
fi
