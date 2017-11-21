#!/usr/bin/bash

repo=$(checkupdates)
aur=$(pacaur -k)

if [ -n "$repo" ]; then
    echo "Repo:"
    echo "$repo"
fi

if [ -n "$aur" ]; then
    echo "Aur:"
    pacaur -k
fi

if ! [ -n "$repo" ] && ! [ -n "$aur" ]; then
    echo "No updates available."
fi
