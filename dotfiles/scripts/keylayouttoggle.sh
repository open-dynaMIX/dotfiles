#!/usr/bin/bash
# {{@@ env['dotdrop_warning'] @@}}
#

if setxkbmap -query | grep layout | grep -q ch; then
    setxkbmap el
else
    setxkbmap ch
fi
