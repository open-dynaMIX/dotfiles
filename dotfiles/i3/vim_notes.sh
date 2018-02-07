#!/usr/bin/bash
# {{@@ env['dotdrop_warning'] @@}}

termite -t vim_notes --geometry 720x550 -e "vim -c 'set wrap' -c 'set colorcolumn=0' $HOME/Notes.txt"
