#!/usr/bin/env python
# {{@@ env['dotdrop_warning'] @@}}

import os
import sys
from urllib.parse import urlparse, parse_qs


qute_url = os.environ.get("QUTE_URL")
qute_fifo = os.environ.get("QUTE_FIFO")

if (
    not qute_url
    or not qute_url.startswith("https://start.duckduckgo.com")
    or not qute_fifo
):
    sys.exit(0)

search = parse_qs(urlparse(qute_url).query)["q"][0]

with open(qute_fifo, "w") as fifo:
    fifo.write(f"open g {search}")
