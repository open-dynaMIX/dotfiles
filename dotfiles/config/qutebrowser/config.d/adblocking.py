# {{@@ env['dotdrop_warning'] @@}}
# flake8: noqa: E266


c = c  # noqa
config = config  # noqa

## List of URLs of lists which contain hosts to block.  The file can be
## in one of the following formats:  - An `/etc/hosts`-like file - One
## host per line - A zip-file of any of the above, with either only one
## file, or a file named   `hosts` (with any extension).
## Type: List of Url
# c.content.host_blocking.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']
c.content.host_blocking.lists = ['file:///home/{{@@ env["USER"] @@}}/.config/qutebrowser/blocked_hosts', 'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']

## List of domains that should always be loaded, despite being ad-
## blocked. Domains may contain * and ? wildcards and are otherwise
## required to exactly match the requested domain. Local domains are
## always exempt from hostblocking.
## Type: List of String
# c.content.host_blocking.whitelist = ['piwik.org']
