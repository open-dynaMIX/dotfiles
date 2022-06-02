#!/usr/bin/bash
# {{@@ header() @@}}

i3-msg 'split h'
i3-msg 'exec alacritty'
i3-msg 'exec alacritty'
sleep .3
i3-msg 'focus left'
i3-msg 'split v'
i3-msg 'exec alacritty'
sleep .3
i3-msg 'focus right'
i3-msg 'split v'
i3-msg 'exec alacritty'
