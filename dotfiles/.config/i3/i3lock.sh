#!/bin/bash
# {{@@ header() @@}}

# suspend message display
killall -SIGUSR1 dunst

/usr/bin/i3lock -n -t -c 000000 -i {{@@ i3lock_wallpaper @@}}

# resume message display
killall -SIGUSR2 dunst
