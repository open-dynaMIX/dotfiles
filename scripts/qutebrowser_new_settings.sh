#!/usr/bin/bash
# Parse qutebrowsers settings.html
# to find settings not present in local config

conf="$HOME/dotfiles/dotfiles/config/qutebrowser/config.d/"


function read_list {
PYTHON_ARG="$1" python - <<END
import os
import qutebrowser
from bs4 import BeautifulSoup
file = os.path.join(qutebrowser.basedir, 'html/doc/settings.html')
with open(file) as f:
    soup = BeautifulSoup(f.read(), 'lxml')
tbody = soup.find('tbody').findAll('td')
for item in tbody:
    link = item.find('a')
    if link:
        print(link.contents[0])
END
}

if [ -d "$conf" ]; then
    grep="grep -Enqr"
elif [ -f "$conf" ]; then
    grep="grep -Enq"
else
    >&2 echo "Config not found!"
    exit 1
fi

while read -r line; do
    if ! $grep "(# )?(c|config)\\.$line" "$conf"; then
        echo "$line"
    fi
done <<< "$(read_list "$@")"
