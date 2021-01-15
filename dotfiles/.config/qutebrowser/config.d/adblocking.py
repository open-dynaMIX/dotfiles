# {{@@ header() @@}}
# flake8: noqa: E266


c = c  # noqa
config = config  # noqa

## List of URLs to ABP-style adblocking rulesets.  Only used when Brave's
## ABP-style adblocker is used (see `content.blocking.method`).  You can
## find an overview of available lists here:
## https://adblockplus.org/en/subscriptions - note that the special
## `subscribe.adblockplus.org` links aren't handled by qutebrowser, you
## will instead need to find the link to the raw `.txt` file (e.g. by
## extracting it from the `location` parameter of the subscribe URL and
## URL-decoding it).
## Type: List of Url
# c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt']

## Enable the ad/host blocker
## Type: Bool
# c.content.blocking.enabled = True

## List of URLs to host blocklists for the host blocker.  Only used when
## the simple host-blocker is used (see `content.blocking.method`).  The
## file can be in one of the following formats:  - An `/etc/hosts`-like
## file - One host per line - A zip-file of any of the above, with either
## only one file, or a file   named `hosts` (with any extension).  It's
## also possible to add a local file or directory via a `file://` URL. In
## case of a directory, all files in the directory are read as adblock
## lists.  The file `~/.config/qutebrowser/blocked-hosts` is always read
## if it exists.
## Type: List of Url
# c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']

## Which method of blocking ads should be used.  Support for Adblock Plus
## (ABP) syntax blocklists using Brave's Rust library requires the
## `adblock` Python package to be installed, which is an optional
## dependency of qutebrowser. It is required when either `adblock` or
## `both` are selected.
## Type: String
## Valid values:
##   - auto: Use Brave's ABP-style adblocker if available, host blocking otherwise
##   - adblock: Use Brave's ABP-style adblocker
##   - hosts: Use hosts blocking
##   - both: Use both hosts blocking and Brave's ABP-style adblocker
# c.content.blocking.method = 'auto'

## A list of patterns that should always be loaded, despite being blocked
## by the ad-/host-blocker. Local domains are always exempt from
## adblocking. Note this whitelists otherwise blocked requests, not
## first-party URLs. As an example, if `example.org` loads an ad from
## `ads.example.org`, the whitelist entry could be
## `https://ads.example.org/*`. If you want to disable the adblocker on a
## given page, use the `content.blocking.enabled` setting with a URL
## pattern instead.
## Type: List of UrlPattern
# c.content.blocking.whitelist = []
