#!/usr/bin/bash
# {{@@ header() @@}}
#

# handling arguments
arglist=("--swap" "--unclut" "--both")
if ! [[ "${arglist[@]}" =~ $1 ]] || ! [ -n "$2" ]; then
    printf "Usage: ./wrapper.sh [--swap|--unclut|--both] COMMAND [ARGUMENTS]
--swap   =  swap the mouse-buttons
--unclut =  kill unclutter
--both   =  do both\n"
    if [[ "$1" =~ ^(-h|--help)$ ]]; then
        exit 0
    else
        exit 1
    fi
fi

# pre command
if [[ "$1" =~ ^(--swap|--both)$ ]]; then
    echo "Switching mouse-buttons"
    {%@@ if profile == "fuckup" @@%}
    xmodmap -e "pointer = 1 2 3"
    {%@@ endif @@%}
    synclient TapButton1=1 TapButton2=3 TapButton3=2
fi

if [[ "$1" =~ ^(--unclut|--both)$ ]]; then
    unclutrun=false
    if pgrep unclutter; then
        unclutrun=true
        echo "Kill unclutter"
        killall unclutter
    else
        echo "Unclutter is not running. Hence not killing and restarting it."
    fi
fi

# command
echo "Running command..."
"${@:2}"

# post command
if [[ "$1" =~ ^(--swap|--both)$ ]]; then
    echo "Switching back mouse-buttons"
    {%@@ if profile == "fuckup" @@%}
    xmodmap -e "pointer = 3 2 1"
    {%@@ endif @@%}
    synclient TapButton1=3 TapButton2=1 TapButton3=2
fi

if [[ "$1" =~ ^(--unclut|--both)$ ]]; then
    if $unclutrun; then
        echo "Start unclutter"
        unclutter {{@@ unclutter_args @@}} &
    fi
fi
