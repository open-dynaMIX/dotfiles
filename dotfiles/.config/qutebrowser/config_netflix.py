# {{@@ header() @@}}
# flake8: noqa: E266
## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html

from pathlib import Path



config.source("{{@@ env['HOME'] @@}}/.config/qutebrowser/config.py")

c = c  # noqa
config = config  # noqa

c.url.default_page = "https://netflix.com"

c.tabs.show = "never"
c.statusbar.show = "never"
c.scrolling.bar = "never"
c.auto_save.session = False
c.content.notifications.enabled = True
c.content.autoplay = True
c.input.mode_override = "passthrough"
