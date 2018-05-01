#!/usr/bin/env bash

file="$1"
for file in "$@"; do
    if [[ "$file" == *.bak ]]; then
        mv "$file" "${file::-4}"
    else
        mv "$file" "${file}.bak"
    fi
done

if echo "$file" | grep -q "sftp:host="; then
    sleep .1 && xdotool key F5
fi
