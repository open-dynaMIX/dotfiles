#!/usr/bin/env python
# {{@@ header() @@}}

import os
import sys
from urllib.parse import quote_plus, urlparse
from bs4 import BeautifulSoup


def parse_gl_gh(title_tag):
    orig_title = qute_soup.find(title_tag).get_text()
    source = "/".join(urlparse(qute_url).path.split("/")[1:3])
    title = f"[{source}] {orig_title}"
    return title


base_url = "{{@@ env['pm_gl_issues_url'] @@}}"
qute_url = os.environ.get("QUTE_URL")
qute_fifo = os.environ.get("QUTE_FIFO")
qute_html_file = os.environ.get("QUTE_HTML")
with open(qute_html_file, "r") as f:
    qute_soup = BeautifulSoup(f.read(), "html.parser")

title = description = qute_url

try:
    if qute_soup.find("meta", property="og:site_name")["content"] == "GitLab":
        title = parse_gl_gh(title_tag="h1")
    elif qute_soup.find("meta", property="og:site_name")["content"] == "GitHub":
        title = parse_gl_gh(title_tag="bdi")
except:
    pass

url = f"{base_url}issue[title]={quote_plus(title)}&issue[description]={quote_plus(description)}"


with open(qute_fifo, "w") as fifo:
    fifo.write(f"open -t {url}")
