# {{@@ header() @@}}
# This file loads all the configfiles from ~/.config/qutebrowser/config.d/
# flake8: noqa: E266
## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html


import os


config = config  # noqa
config.load_autoconfig(False)


CONF_DIR = os.path.expanduser("~/.config/qutebrowser/config.d/")
for file in os.listdir(CONF_DIR):
    if file.endswith(".py"):
        config.source(os.path.join(CONF_DIR, file))
