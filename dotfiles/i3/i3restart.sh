#!/bin/bash
# This file is managed by dotdrop, do not edit!

i3-msg restart
sleep 0.3
{%@@ if profile == "ant" @@%}
transset-df -n "tracker.txt - (~/Init7/Administration)" 0.8
{%@@ endif @@%}
transset-df -n "Mozilla Thunderbird$" 1.0
