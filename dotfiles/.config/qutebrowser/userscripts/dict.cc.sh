#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}

echo "open -t https://www.dict.cc/?s=$QUTE_SELECTED_TEXT" >> "$QUTE_FIFO"
