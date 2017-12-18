#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}
# If this is executed directly from within qutebrowser with spawn,
# the browser crashes.

youtube-dl -o - "$1" | vlc -
