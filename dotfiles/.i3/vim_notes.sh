#!/usr/bin/bash
# {{@@ env['dotdrop_warning'] @@}}

termite -t vim_notes -e "vim -c 'set wrap' -c 'set colorcolumn=0' $HOME/Notes.txt"
