#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}

i3-msg restart
killall dunst
sleep 0.3
transset-df -n "Notes.txt - (~)" 0.8
transset-df -n "Mozilla Thunderbird$" 1.0
xdotool search --onlyvisible --class "Firefox" | while read -r line; do
    transset-df --id "$line" 1
done
