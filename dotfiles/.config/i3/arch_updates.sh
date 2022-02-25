#!/usr/bin/bash
# {{@@ header() @@}}

IFS=$'\n'
repo_dirty=("$(checkupdates)")
aur_dirty=("$(yay --query --upgrades --aur)")
unset IFS

repo=()
aur=()
for value in "${repo_dirty[@]}"; do
    [[ $value != "" ]] && repo+=("$value")
done
for value in "${aur_dirty[@]}"; do
    [[ $value != "" ]] && aur+=("$value")
done

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
        echo "$package" | awk '{print $1}'
    done
fi

if [ "${#repo[@]}" -lt 1 ] && [ "${#aur[@]}" -lt 1 ]; then
    echo "No updates available."
fi
