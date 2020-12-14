# {{@@ header() @@}}
# flake8: noqa: E266


c = c  # noqa
config = config  # noqa

## List of URLs of lists which contain hosts to block.
## The file can be in one of the following formats:
##  - An /etc/hosts-like file
##  - One host per line
##  - A zip-file of any of the above, with either only one file, or a file
##    named hosts (with any extension).
## It’s also possible to add a local file or directory via a file:// URL.
## In case of a directory, all files in the directory are read as adblock lists.
## The file ~/.config/qutebrowser/blocked-hosts is always read if it exists.
# c.content.host_blocking.lists = ["https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"]

## A list of patterns that should always be loaded, despite being ad-blocked.
## Note this whitelists blocked hosts, not first-party URLs. As an example,
## if example.org loads an ad from ads.example.org, the whitelisted host
## should be ads.example.org. If you want to disable the adblocker on a given
## page, use the content.host_blocking.enabled setting with a URL pattern
## instead. Local domains are always exempt from hostblocking.
## Type: List of UrlPattern
# c.content.host_blocking.whitelist = []
