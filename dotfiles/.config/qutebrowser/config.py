# {{@@ header() @@}}
# flake8: noqa: E266
## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html

from urllib.parse import urlencode


c = c  # noqa
config = config  # noqa

STARTPAGE = 'file:///home/{{@@ env["USER"] @@}}/.config/qutebrowser/home.html'
PURPLE = '#470f77'

def get_ddg():
    ddg_config = {
        "k1": "-1",
        "k7": "111111",
        "k8":"b8b8b8",
        "k9":"b8b8b8",
        "ka": "Fira Code",
        "kae": "d",
        "kah": "ch-de",
        "kaj": "m",
        "kak": "-1",
        "kal": "-1",
        "kam": "osm",
        "kao": "-1",
        "kap": "-1",
        "kaq": "-1",
        "kau": "-1",
        "kav": "1",
        "kax": "-1",
        "kg": "g",
        "kk": "-1",
        "kp": "-2",
        "kt": "Fira Sans",
        "ku": "1",
        "kx":"c6c6c6",
    }
    return f"https://start.duckduckgo.com/?q={{}}&{urlencode(ddg_config)}"


DDG = get_ddg()

## This is here so configs done via the GUI are still loaded.
## Remove it to not load settings done via the GUI.
config.load_autoconfig(False)

## Aliases for commands. The keys of the given dictionary are the
## aliases, while the values are the commands they map to.
## Type: Dict
# c.aliases = {'w': 'session-save', 'q': 'close', 'qa': 'quit', 'wq': 'quit --save', 'wqa': 'quit --save'}
c.aliases = {'q': 'close',
             'qa': 'quit',
             'wq': 'quit --save',
             'youtube-dl': 'spawn yt-dlp -o "$HOME/Downloads/%(title)s-%(id)s.%(ext)s" {url}',
             'vlc': 'spawn --userscript ~/.config/qutebrowser/userscripts/videos_vlc.sh'}
c.aliases["yt-dlp"] = c.aliases["youtube-dl"]

## Always restore open sites when qutebrowser is reopened.
## Type: Bool
# c.auto_save.session = False
c.auto_save.session = True

## When to show a changelog after qutebrowser was upgraded.
## Type: String
## Valid values:
##    - major: Show changelog for major upgrades (e.g. v2.0.0 → v3.0.0).
##    - minor: Show changelog for major and minor upgrades (e.g. v2.0.0 → v2.1.0).
##    - patch: Show changelog for major, minor and patch upgrades (e.g. v2.0.0 → v2.0.1).
##    - never: Never show changelog after upgrades.
# c.changelog_after_upgrade = "minor"
c.changelog_after_upgrade = "patch"

## Whether quitting the application requires a confirmation.
## Type: ConfirmQuit
## Valid values:
##   - always: Always show a confirmation.
##   - multiple-tabs: Show a confirmation if multiple tabs are opened.
##   - downloads: Show a confirmation if downloads are running
##   - never: Never show a confirmation.
# c.confirm_quit = ['never']
c.confirm_quit = ['downloads']

## Automatically start playing <video> elements.
## Note this option needs a restart with QtWebEngine on Qt < 5.11.
## Type: Bool
## On QtWebEngine, this setting requires Qt 5.10 or newer.
## On QtWebKit, this setting is unavailable.
# c.content.autoplay = True
c.content.autoplay = False

## Control which cookies to accept.
## Type: String
## Valid values:
##   - all: Accept all cookies.
##   - no-3rdparty: Accept cookies from the same origin only.
##   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain.
##   - never: Don't accept cookies at all.
# c.content.cookies.accept = 'all'
c.content.cookies.accept = 'no-3rdparty'

# Default encoding to use for websites. The encoding must be a string
# describing an encoding such as _utf-8_, _iso-8859-1_, etc.
# Type: String
# c.content.default_encoding = 'iso-8859-1'
c.content.default_encoding = 'utf-8'

## Value to send in the `Accept-Language` header.
## Type: String
# c.content.headers.accept_language = 'en-US,en;q=0.9'
c.content.headers.accept_language = 'en-US,en;q=0.5'

## Enable pdf.js to view PDF files in the browser. Note that the files
## can still be downloaded by clicking the download button in the pdf.js
## viewer.
## Type: Bool
# c.content.pdfjs = False
c.content.pdfjs = True

## Enables or disables plugins in Web pages.
## Type: Bool
# c.content.plugins = False
c.content.plugins = True

## The editor (and arguments) to use for the `open-editor` command. `{}`
## gets replaced by the filename of the file to be edited.
## Type: ShellCommand
# c.editor.command = ['gvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']
c.editor.command = ['subl', '-a', '{}']

## Forward unbound keys to the webview in normal mode.
## Type: String
## Valid values:
##   - all: Forward all unbound keys.
##   - auto: Forward unbound non-alphanumeric keys.
##   - none: Don't forward any keys.
# c.input.forward_unbound_keys = 'auto'
c.input.forward_unbound_keys = 'all'

## Automatically enter insert mode if an editable element is focused
## after loading the page.
## Type: Bool
# c.input.insert_mode.auto_load = False
c.input.insert_mode.auto_load = True

# Time (in ms) to show messages in the statusbar for. Set to 0 to never
# clear messages.
# Type: Int
# c.messages.timeout = 3000
c.messages.timeout = 5000

## Load a restored tab as soon as it takes focus.
## Type: Bool
# c.session.lazy_restore = False
c.session.lazy_restore = True

## Behavior when the last tab is closed.
## Type: String
## Valid values:
##   - ignore: Don't do anything.
##   - blank: Load a blank page.
##   - startpage: Load the start page.
##   - default-page: Load the default page.
##   - close: Close the window.
# c.tabs.last_close = 'ignore'
c.tabs.last_close = 'startpage'

## When switching tabs, what input mode is applied.
## Type: String
## Valid values:
##   - persist: Retain the current mode.
##   - restore: Restore previously saved mode.
##   - normal: Always revert to normal mode.
# c.tabs.mode_on_change = 'normal'
c.tabs.mode_on_change = 'restore'

## The page to open if :open -t/-b/-w is used without URL. Use
## `about:blank` for a blank page.
## Type: FuzzyUrl
# c.url.default_page = 'https://start.duckduckgo.com/'
c.url.default_page = STARTPAGE

## Open base URL of the searchengine if a searchengine shortcut is invoked
## without parameters.
## Type: Bool
# c.url.open_base_url = False
c.url.open_base_url = True

## The page(s) to open at the start.
## Type: List of FuzzyUrl, or FuzzyUrl
# c.url.start_pages = ['https://start.duckduckgo.com']
c.url.start_pages = [STARTPAGE]

##############################################################################
# SEARCH ENGINES
##############################################################################

## Definitions of search engines which can be used via the address bar.
## Maps a searchengine name (such as `DEFAULT`, or `ddg`) to a URL with a
## `{}` placeholder. The placeholder will be replaced by the search term,
## use `{{` and `}}` for literal `{`/`}` signs. The searchengine named
## `DEFAULT` is used when `url.auto_search` is turned on and something
## else than a URL was entered to be opened. Other search engines can be
## used by prepending the search engine name to the search term, e.g.
## `:open google qutebrowser`.
## Type: Dict
# c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}'}
ENGINES = {'DEFAULT': 'https://www.google.com/search?q={}',
           'a': 'https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}',
           'aur': 'https://aur.archlinux.org/packages/?O=0&K={}',
           'cc': 'https://www.dict.cc/?s={}',
           'ddg': DDG,
           'deepl': "https://www.deepl.com/en/translator#{}",  # Expects a string like `en/de/something`
           'g': 'https://www.google.com/search?q={}',
           'gh': 'https://github.com/search?utf8=%E2%9C%93&q={}&type=',
           'maps': 'https://www.google.ch/maps/place/{}',
           'osm': 'https://www.openstreetmap.org/search?query={}',
           'srf': 'https://www.srf.ch/play/suche?query={}',
           'w': 'https://en.wikipedia.org/wiki/{}',
           'wd': 'https://de.wikipedia.org/w/index.php?title=Spezial:Suche&search={}',
           'yt': 'https://www.youtube.com/results?search_query={}'}

# Add some searchengines from dotdrop .env-file
ENGINES.update({{@@ env['qutebrowser_search_engines'] @@}})

c.url.searchengines = ENGINES

##############################################################################
# ADBLOCKING
##############################################################################

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
c.content.blocking.method = 'both'


## List of URLs to ABP-style adblocking rulesets.
## Only used when Brave’s ABP-style adblocker is used
## (see content.blocking.method).
## You can find an overview of available lists here:
## https://adblockplus.org/en/subscriptions - note that the special
## subscribe.adblockplus.org links aren’t handled by qutebrowser, you will
## instead need to find the link to the raw .txt file (e.g. by extracting it
## from the location parameter of the subscribe URL and URL-decoding it).
## Type: List of Url
# c.content.blocking.adblock.lists = [
#     "https://easylist.to/easylist/easylist.txt",
#     "https://easylist.to/easylist/easyprivacy.txt",
# ]
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://easylist-downloads.adblockplus.org/easylistdutch.txt",
    "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
    "https://www.i-dont-care-about-cookies.eu/abp/",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
]

##############################################################################
# THEME
##############################################################################

## The rounding radius for the edges of prompts.
## Type: Int
# c.prompt.radius = 8
c.prompt.radius = 0

## The format to use for the tab title. The following placeholders are
## defined:
## * `{perc}`: Percentage as a string like [10%].
## * `{perc_raw}`: Raw percentage, e.g. 10.
## * `{current_title}`: Title of the current web page.
## * `{title_sep}`: The string ` - ` if a title is set, empty otherwise.
## * `{index}`: Index of this tab.
## * `{id}`: Internal tab ID of this tab.
## * `{scroll_pos}`: Page scroll position.
## * `{host}`: Host of the current web page.
## * `{backend}`: Either 'webkit’ or 'webengine'
## * `{private}`: Indicates when private mode is enabled.
## * `{current_url}`: URL of the current web page.
## * `{protocol}`: Protocol (http/https/…) of the current web page.
## * `{audio}`: Indicator for audio/mute status.
## Type: FormatString
# c.tabs.title.format = '{audio}{index}: {current_title}'
c.tabs.title.format = '{perc}{audio}{current_title}{title_sep}{host}'

## List of widgets displayed in the statusbar.
## Type: List of String
## Valid values:
##   - url: Current page URL.
##   - scroll: Percentage of the current page position like 10%.
##   - scroll_raw: Raw percentage of the current page position like 10.
##   - history: Display an arrow when possible to go back/forward in history.
##   - tabs: Current active tab, e.g. 2.
##   - keypress: Display pressed keys when composing a vi command.
##   - progress: Progress bar for the current page loading.
# statusbar.widgets = ['keypress', 'url', 'scroll', 'history', 'tabs']
c.statusbar.widgets = ['keypress', 'url', 'scroll', 'history', 'tabs', 'progress']

##############################################################################
# COLORS
##############################################################################

## Background color of the completion widget category headers.
## Type: QssColor
# c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #888888, stop:1 #505050)'
c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {0}, stop:1 {0})'.format(PURPLE)

## Background color of the selected completion item.
## Type: QssColor
# c.colors.completion.item.selected.bg = '#e8c000'
c.colors.completion.item.selected.bg = '#000000'

## Bottom border color of the selected completion item.
## Type: QssColor
# c.colors.completion.item.selected.border.bottom = '#bbbb00'
c.colors.completion.item.selected.border.bottom = '#000000'

## Top border color of the completion widget category headers.
## Type: QssColor
# c.colors.completion.item.selected.border.top = '#bbbb00'
c.colors.completion.item.selected.border.top = '#000000'

## Foreground color of the selected completion item.
## Type: QtColor
# c.colors.completion.item.selected.fg = 'black'
c.colors.completion.item.selected.fg = '#ffffff'

## Background color of the context menu’s selected item.
## If set to null, the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.selected.bg = None
c.colors.contextmenu.selected.bg = PURPLE

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
## Type: QssColor
# c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 0.8), stop:1 rgba(255, 197, 66, 0.8))'
c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(71, 15, 119, 0.8), stop:1 rgba(98, 22, 162, 0.8))'  # purple

## Font color for hints.
## Type: QssColor
# c.colors.hints.fg = 'black'
c.colors.hints.fg = '#ffffff'

## Font color for the matched part of hints.
## Type: QssColor
# c.colors.hints.match.fg = 'green'
c.colors.hints.match.fg = '#b97ff0'

## Rounding radius (in pixels) for the edges of the keyhint dialog.
## Type: Int
# c.keyhint.radius = 6
c.keyhint.radius = 0

## Background color of a warning message.
## Type: QssColor
# c.colors.messages.warning.bg = 'darkorange'
c.colors.messages.warning.bg = PURPLE

## Border color of a warning message.
## Type: QssColor
# c.colors.messages.warning.border = '#d47300'
c.colors.messages.warning.border = PURPLE

## Background color of the statusbar in caret mode.
## Type: QssColor
# c.colors.statusbar.caret.bg = 'purple'
c.colors.statusbar.caret.bg = PURPLE

## Background color of the statusbar in private browsing + command mode.
## Type: QssColor
# c.colors.statusbar.command.private.bg = 'darkslategray'
c.colors.statusbar.command.private.bg = 'red'

## Background color of the statusbar in private browsing mode.
## Type: QssColor
# c.colors.statusbar.private.bg = '#666666'
c.colors.statusbar.private.bg = 'red'

## Background color of unselected even tabs.
## Type: QtColor
# c.colors.tabs.even.bg = 'darkgrey'
c.colors.tabs.even.bg = '#464646'

## Background color of unselected odd tabs.
## Type: QtColor
# c.colors.tabs.odd.bg = 'grey'
c.colors.tabs.odd.bg = '#333333'

## Background color of selected even tabs.
## Type: QtColor
# c.colors.tabs.selected.even.bg = 'black'
c.colors.tabs.selected.even.bg = PURPLE

## Background color of selected odd tabs.
## Type: QtColor
# c.colors.tabs.selected.odd.bg = 'black'
c.colors.tabs.selected.odd.bg = PURPLE

## Value to use for prefers-color-scheme: for websites. The "light" value is
## only available with QtWebEngine 5.15.2+. On older versions, it is the same
## as "auto". The "auto" value is broken on QtWebEngine 5.15.2 due to a Qt
## bug. There, it will fall back to "light" unconditionally.
## This setting requires a restart.
## Type: String
## Valid values:
##   - auto: Use the system-wide color scheme setting.
##   - light: Force a light theme.
##   - dark: Force a dark theme.
## On QtWebEngine, this setting requires Qt 5.14 or newer.
## On QtWebKit, this setting is unavailable.
# c.colors.webpage.preferred_color_scheme = "auto"
c.colors.webpage.preferred_color_scheme = "dark"

## CSS border value for hints.
## Type: String
# c.hints.border = '1px solid #E3BE23'
c.hints.border = '1px solid #ffffff'

##############################################################################
# HINTS
##############################################################################

## Chars used for hint strings.
## Type: UniqueCharString
# c.hints.chars = 'asdfghjkl'
c.hints.chars = 'werasdfyxc'

##############################################################################
# FONTS
##############################################################################

## Default font families to use. Whenever "default_family" is used in a font
## setting, it’s replaced with the fonts listed here. If set to an empty
## value, a system-specific monospace default is used.
## Type: List of Font, or Font
# c.fonts.default_family = []
c.fonts.default_family = ["Fira Code", "Droid Sans Mono", "xos4 Terminus", "Terminus", "Monospace", "DejaVu Sans Mono", "Monaco", "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", "Courier", "Liberation Mono", "monospace", "Fixed", "Consolas", "Terminal"]

## Default font size to use. Whenever "default_size" is used in a font
## setting, it’s replaced with the size listed here. Valid values are either
## a float value with a "pt" suffix, or an integer value with a "px" suffix.
## Type: String
# c.fonts.default_size = "10pt"
c.fonts.default_size = "12pt"

##############################################################################
# KEY BINDINGS
##############################################################################

## Bindings for normal mode
config.bind(',n', f'config-cycle --temp content.user_stylesheets ~/Linux/solarized-everything-css/css/solarized-all-sites-dark.css "" ;; reload')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('O', 'set-cmd-text :open {url:pretty}')
config.bind('T', 'set-cmd-text :open -t {url:pretty}')
config.bind('t', 'set-cmd-text -s :open -t')
config.bind('ä', 'back')
config.bind('$', 'forward')
config.bind('à', 'tab-prev')
config.bind('£', 'tab-next')
config.bind('cc', 'spawn --userscript ~/.config/qutebrowser/userscripts/dict.cc.sh')
config.bind('<Ctrl-Shift-PgUp>', 'tab-move -')
config.bind('<Ctrl-Shift-PgDown>', 'tab-move +')
config.bind('m', 'spawn mpv {url}')
config.bind('gt', 'open -t https://translate.google.com/translate?sl=auto&tl=en&hl=en&u={url}&client=webapp')

## Bindings for caret mode
config.bind('<LEFT>', 'scroll left', mode='caret')
config.bind('<DOWN>', 'scroll down', mode='caret')
config.bind('<UP>', 'scroll up', mode='caret')
config.bind('<RIGHT>', 'scroll right', mode='caret')
config.bind('<LEFT>', 'move-to-prev-char', mode='caret')
config.bind('<DOWN>', 'move-to-next-line', mode='caret')
config.bind('<UP>', 'move-to-prev-line', mode='caret')
config.bind('<RIGHT>', 'move-to-next-char', mode='caret')
config.bind('W', 'move-to-prev-word', mode='caret')

## Bindings for command mode
config.bind('<UP>', 'command-history-prev', mode='command')
config.bind('<DOWN>', 'command-history-next', mode='command')
