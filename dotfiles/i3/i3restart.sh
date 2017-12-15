#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}


function hack_no_transparency {
    xdotool search --onlyvisible --class "$1" | while read -r line; do
        transset-df --id "$line" 1.0
    done
}

i3-msg restart
killall dunst
sleep 0.3
transset-df -n "Notes.txt - (~)" 0.8

hack_no_transparency "Thunderbird"
hack_no_transparency "Firefox"
hack_no_transparency "Rambox"
