#!/usr/bin/bash
# Parse https://www.qutebrowser.org/doc/help/settings.html
# to find settings not present in local config


function get_list {
PYTHON_ARG="$1" python - <<END
from bs4 import BeautifulSoup
import requests
import os
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
req = requests.get('https://www.qutebrowser.org/doc/help/settings.html', None)
soup = BeautifulSoup(req.content, 'lxml')
tbody = soup.find('tbody').findAll('td')
for item in tbody:
    link = item.find('a')
    if link:
        print(link.contents[0])
END
}

while read -r line; do
    if ! grep -nrq "# c.*\\.$line" "$HOME/dotfiles/dotfiles/config/qutebrowser/config.d/"; then
        echo "$line"
    fi
done <<< "$(get_list "$@")"
