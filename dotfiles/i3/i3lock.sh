#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}

# suspend message display
killall -SIGUSR1 dunst

/usr/bin/i3lock -n -t -c 000000 -i {{@@ env['i3lock_wallpaper'] @@}}

# resume message display
killall -SIGUSR2 dunst

{%@@ if env['multiple_keylayouts'] == 'true' @@%}
sleep 1.5
/usr/bin/setxkbmap ch
{%@@ endif @@%}
