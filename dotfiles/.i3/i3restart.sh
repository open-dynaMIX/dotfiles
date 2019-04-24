#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}


function hack_no_transparency {
    xdotool search --onlyvisible --class "$1" | while read -r line; do
        transset-df --id "$line" 1.0
    done
}

i3-msg restart
killall dunst
kill "$(pgrep keepassxc)"
sleep 0.3
transset-df -n "Notes.txt - (~)" 0.8
transset-df -n "vim_notes" 0.8

hack_no_transparency "Thunderbird"
hack_no_transparency "Firefox"
hack_no_transparency "Rambox"
hack_no_transparency "Sublime_text"
hack_no_transparency "Nemo"
hack_no_transparency "Thunar"

keepassxc &
