#!/bin/bash
# {{@@ env['dotdrop_warning'] @@}}

#!/bin/bash

echo "open -t https://www.dict.cc/?s=$QUTE_SELECTED_TEXT" >> "$QUTE_FIFO"
