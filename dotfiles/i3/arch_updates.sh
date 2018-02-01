#!/usr/bin/bash
# {{@@ env['dotdrop_warning'] @@}}


IFS=$'\n'
repo=("$(checkupdates)")
aur=("$(cower -u)")
unset IFS

if [ "${#repo[@]}" -gt 0 ]; then
    echo "Repo:"
    echo "===="
    for package in "${repo[@]}"; do
        echo "$package" | awk '{print $1}'
    done
fi

if [ "${#aur[@]}" -gt 0 ]; then
    echo -e "\\nAur:"
    echo "==="
    for package in "${aur[@]}"; do
        echo "$package" | awk '{print $2}'
    done
fi

if [ "${#repo[@]}" -lt 1 ] && [ "${#aur[@]}" -lt 1 ]; then
    echo "No updates available."
fi
