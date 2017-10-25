#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}

/usr/bin/i3lock -t -c 000000 -i {{@@ env['i3lock_wallpaper'] @@}}
{%@@ if env['multiple_keylayouts'] == 'true' @@%}
sleep .8
/usr/bin/setxkbmap ch
{%@@ endif @@%}
