#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}

i3-msg restart
sleep 0.3
transset-df -n "Notes.txt - (~)" 0.8
transset-df -n "Mozilla Thunderbird$" 1.0
