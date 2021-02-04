# {{@@ header() @@}}
# flake8: noqa: E266
## Autogenerated config.py
## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html


STARTPAGE = 'file:///home/{{@@ env["USER"] @@}}/.config/qutebrowser/home.html'
# STARTPAGE = 'qute://help/img/cheatsheet-big.png'

c = c  # noqa
config = config  # noqa

## This is here so configs done via the GUI are still loaded.
## Remove it to not load settings done via the GUI.
# config.load_autoconfig()

## Aliases for commands. The keys of the given dictionary are the
## aliases, while the values are the commands they map to.
## Type: Dict
# c.aliases = {'w': 'session-save', 'q': 'close', 'qa': 'quit', 'wq': 'quit --save', 'wqa': 'quit --save'}
c.aliases = {'q': 'close',
             'qa': 'quit',
             'wq': 'quit --save',
             'youtube-dl': 'spawn youtube-dl -o "$HOME/Downloads/%(title)s-%(id)s.%(ext)s" {url}',
             'vlc': 'spawn --userscript ~/.config/qutebrowser/userscripts/videos_vlc.sh'}

## How often (in milliseconds) to auto-save config/cookies/etc.
## Type: Int
# c.auto_save.interval = 15000

## Always restore open sites when qutebrowser is reopened.
## Type: Bool
# c.auto_save.session = False
c.auto_save.session = True

## The backend to use to display websites. qutebrowser supports two
## different web rendering engines / backends, QtWebKit and QtWebEngine.
## QtWebKit was discontinued by the Qt project with Qt 5.6, but picked up
## as a well maintained fork: https://github.com/annulen/webkit/wiki -
## qutebrowser only supports the fork. QtWebEngine is Qt's official
## successor to QtWebKit. It's slightly more resource hungry that
## QtWebKit and has a couple of missing features in qutebrowser, but is
## generally the preferred choice. This setting requires a restart.
## Type: String
## Valid values:
##   - webengine: Use QtWebEngine (based on Chromium)
##   - webkit: Use QtWebKit (based on WebKit, similar to Safari)
# c.backend = 'webengine'

## When to show a changelog after qutebrowser was upgraded.
## Type: String
## Valid values:
##    - major: Show changelog for major upgrades (e.g. v2.0.0 → v3.0.0).
##    - minor: Show changelog for major and minor upgrades (e.g. v2.0.0 → v2.1.0).
##    - patch: Show changelog for major, minor and patch upgrades (e.g. v2.0.0 → v2.0.1).
##    - never: Never show changelog after upgrades.
# c.changelog_after_upgrade = "minor"
c.changelog_after_upgrade = "patch"

## How many commands to save in the command history. 0: no history / -1:
## unlimited
## Type: Int
# c.completion.cmd_history_max_items = 100

## Delay (in milliseconds) before updating completions after typing a
## character.
## Type: Int
# c.completion.delay = 0

## Default filesystem autocomplete suggestions for :open. The elements of this
## list show up in the completion window under the Filesystem category when
## the command line contains :open but no argument.
## Type: List of String
# c.completion.favorite_paths = []

## Height (in pixels or as percentage of the window) of the completion.
## Type: PercOrInt
# c.completion.height = '50%'

## Minimum amount of characters needed to update completions.
## Type: Int
# c.completion.min_chars = 1


## Which categories to show (in which order) in the :open completion.
## Type: FlagList
## Valid values:
##   - searchengines
##   - quickmarks
##   - bookmarks
##   - history
##   - filesystem
# c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

## Move on to the next part when there's only one possible completion
## left.
## Type: Bool
# c.completion.quick = True

## When to show the autocompletion window.
## Type: String
## Valid values:
##   - always: Whenever a completion is available.
##   - auto: Whenever a completion is requested.
##   - never: Never.
# c.completion.show = 'always'

## How to format timestamps (e.g. for the history completion).
## Type: TimestampTemplate
# c.completion.timestamp_format = '%Y-%m-%d %H:%M'

## Execute the best-matching command on a partial match.
## Type: Bool
# c.completion.use_best_match = False

## A list of patterns which should not be shown in the history.
## This only affects the completion. Matching URLs are still saved in the
## history (and visible on the qute://history page), but hidden in the
## completion. Changing this setting will cause the completion history to be
## regenerated on the next start, which will take a short while.
## This setting requires a restart.
## Type: List of UrlPattern
# c.completion.web_history.exclude = []

## How many URLs to show in the web history. 0: no history / -1:
## unlimited
## Type: Int
# c.completion.web_history.max_items = -1

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

## Whether support for the HTML 5 web application cache feature is
## enabled. An application cache acts like an HTTP cache in some sense.
## For documents that use the application cache via JavaScript, the
## loader engine will first ask the application cache for the contents,
## before hitting the network.
## Type: Bool
# c.content.cache.appcache = True

## The maximum number of pages to hold in the global memory page cache.
## The Page Cache allows for a nicer user experience when navigating
## forth or back to pages in the forward/back history, by pausing and
## resuming up to _n_ pages. For more information about the feature,
## please refer to: http://webkit.org/blog/427/webkit-page-cache-i-the-
## basics/
## Type: Int
# c.content.cache.maximum_pages = 0

## Size of the HTTP network cache. Null to use the default value. With
## QtWebEngine, the maximum supported value is 2147483647 (~2 GB).
## Type: Int
# c.content.cache.size = None


## Allow websites to read canvas elements.
## Note this is needed for some websites to work properly.
## This setting requires a restart.
## Type: Bool
## This setting is only available with the QtWebEngine backend
# c.content.canvas_reading = True

## Control which cookies to accept.
## Type: String
## Valid values:
##   - all: Accept all cookies.
##   - no-3rdparty: Accept cookies from the same origin only.
##   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain.
##   - never: Don't accept cookies at all.
# c.content.cookies.accept = 'all'
c.content.cookies.accept = 'no-3rdparty'

## Store cookies. Note this option needs a restart with QtWebEngine on Qt
## < 5.9.
## Type: Bool
# c.content.cookies.store = True

# Default encoding to use for websites. The encoding must be a string
# describing an encoding such as _utf-8_, _iso-8859-1_, etc.
# Type: String
# c.content.default_encoding = 'iso-8859-1'
c.content.default_encoding = 'utf-8'


## Allow websites to share screen content. On Qt < 5.10, a dialog box is
## always displayed, even if this is set to "true".
## Type: BoolAsk
## Valid values:
## - true
## - false
## - ask
# c.content.desktop_capture = 'ask'

## Try to pre-fetch DNS entries to speed up browsing.
## Type: Bool
# c.content.dns_prefetch = True

## Expand each subframe to its contents. This will flatten all the frames
## to become one scrollable page.
## Type: Bool
# c.content.frame_flattening = False

## Allow websites to request geolocations.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
# c.content.geolocation = 'ask'

## Value to send in the `Accept-Language` header.
## Type: String
# c.content.headers.accept_language = 'en-US,en;q=0.9'
c.content.headers.accept_language = 'en-US,en;q=0.5'

## Set custom headers for qutebrowser HTTP requests.
## Type: Dict
# c.content.headers.custom = {}

## Value to send in the `DNT` header. When this is set to true,
## qutebrowser asks websites to not track your identity. If set to null,
## the DNT header is not sent at all.
## Type: Bool
# c.content.headers.do_not_track = True

## Send the Referer header. The Referer header tells websites from which
## website you were coming from when visting them.
## Type: String
## Valid values:
##   - always: Always send the Referer.
##   - never: Never send the Referer. This is not recommended, as some sites may break.
##   - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites.
# c.content.headers.referer = 'same-domain'

## User agent to send.
## The following placeholders are defined:
##  - {os_info}: Something like "X11; Linux x86_64".
##  - {webkit_version}: The underlying WebKit version (set to a fixed value with QtWebEngine).
##  - {qt_key}: "Qt" for QtWebKit, "QtWebEngine" for QtWebEngine.
##  - {qt_version}: The underlying Qt version.
##  - {upstream_browser_key}: "Version" for QtWebKit, "Chrome" for QtWebEngine.
##  - {upstream_browser_version}: The corresponding Safari/Chrome version.
##  - {qutebrowser_version}: The currently running qutebrowser version.
## The default value is equal to the unchanged user agent of QtWebKit/QtWebEngine.
## Note that the value read from JavaScript is always the global value.
## This setting supports URL patterns.
## Type: FormatString
# c.content.headers.user_agent = "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}"

## Enable or disable hyperlink auditing (`<a ping>`).
## Type: Bool
# c.content.hyperlink_auditing = False

## Whether images are automatically loaded in web pages.
## Type: Bool
# c.content.images = True

## Show javascript alerts.
## Type: Bool
# c.content.javascript.alert = True

## Whether JavaScript can read from or write to the clipboard. With
## QtWebEngine, writing the clipboard as response to a user interaction
## is always allowed.
## Type: Bool
# c.content.javascript.can_access_clipboard = False

## Whether JavaScript can close tabs.
## Type: Bool
# c.content.javascript.can_close_tabs = False

## Whether JavaScript can open new tabs without user interaction.
## Type: Bool
# c.content.javascript.can_open_tabs_automatically = False

## Enables or disables JavaScript.
## Type: Bool
# c.content.javascript.enabled = True

## Log levels to use for JavaScript console logging messages. When a
## JavaScript message with the level given in the dictionary key is
## logged, the corresponding dictionary value selects the qutebrowser
## logger to use. On QtWebKit, the "unknown" setting is always used.
## Type: Dict
# c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}

## Use the standard JavaScript modal dialog for `alert()` and `confirm()`
## Type: Bool
# c.content.javascript.modal_dialog = False

## Show javascript prompts.
## Type: Bool
# c.content.javascript.prompt = True

## Whether locally loaded documents are allowed to access other local
## urls.
## Type: Bool
# c.content.local_content_can_access_file_urls = True

## Whether locally loaded documents are allowed to access remote urls.
## Type: Bool
# c.content.local_content_can_access_remote_urls = False

## Whether support for HTML 5 local storage and Web SQL is enabled.
## Type: Bool
# c.content.local_storage = True

## Allow websites to record audio.
## This setting supports URL patterns.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## This setting is only available with the QtWebEngine backend.
# c.content.media.audio_capture = 'ask'

## Allow websites to record audio and video.
## This setting supports URL patterns.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## This setting is only available with the QtWebEngine backend.
# c.content.media.audio_video_capture = 'ask'

## Allow websites to record video.
## This setting supports URL patterns.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## This setting is only available with the QtWebEngine backend.
# c.content.media.video_capture = 'ask'

## Allow websites to lock your mouse pointer.
## This setting supports URL patterns.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## On QtWebEngine, this setting requires Qt 5.8 or newer.
## On QtWebKit, this setting is unavailable.
# c.content.mouse_lock = 'ask'

## Automatically mute tabs. Note that if the :tab-mute command is used,
## the mute status for the affected tab is now controlled manually, and this
## setting doesn’t have any effect.
## This setting supports URL patterns.
## Type: Bool
# c.content.mute = False

## Netrc-file for HTTP authentication. If unset, ~/.netrc is used
## Type: File
# c.content.netrc_file = None

## Allow websites to show notifications.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
# c.content.notifications = 'ask'
c.content.notifications = False

## Enable pdf.js to view PDF files in the browser. Note that the files
## can still be downloaded by clicking the download button in the pdf.js
## viewer.
## Type: Bool
# c.content.pdfjs = False
c.content.pdfjs = True

## Allow websites to request persistent storage quota via
## navigator.webkitPersistentStorage.requestQuota.
## Type: BoolAsk
## Valid values:
## - true
## - false
## - ask
## On QtWebEngine, this setting requires Qt 5.11 or newer.
## On QtWebKit, this setting is unavailable.
# c.content.persistent_storage = 'ask'

## Enables or disables plugins in Web pages.
## Type: Bool
# c.content.plugins = False
c.content.plugins = True

## Whether the background color and images are also drawn when the page
## is printed.
## Type: Bool
# c.content.print_element_backgrounds = True

## Open new windows in private browsing mode which does not record
## visited pages.
## Type: Bool
# c.content.private_browsing = False

## The proxy to use. In addition to the listed values, you can use a
## `socks://...` or `http://...` URL.
## Type: Proxy
## Valid values:
##   - system: Use the system wide proxy.
##   - none: Don't use any proxy
# c.content.proxy = 'system'

## Send DNS requests over the configured proxy.
## Type: Bool
# c.content.proxy_dns_requests = True

## Allow websites to register protocol handlers via
## navigator.registerProtocolHandler.
## Type: BoolAsk
## Valid values:
## - true
## - false
## - ask
## On QtWebEngine, this setting requires Qt 5.11 or newer.
## On QtWebKit, this setting is unavailable.
# c.content.register_protocol_handler = 'ask'

## Enable quirks (such as faked user agent headers) needed to get specific
## sites to work properly. This setting requires a restart.
## Type: Bool
# c.content.site_specific_quirks = True

## Validate SSL handshakes.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
# c.content.ssl_strict = 'ask'

## How navigation requests to URLs with unknown schemes are handled.
## This setting supports URL patterns.
## Type: String
## Valid values:
##   - disallow: Disallows all navigation requests to URLs with unknown
##               schemes.
##   - allow-from-user-interaction: Allows navigation requests to URLs with
##                                  unknown schemes that are issued from
##                                  user-interaction (like a mouse-click), whereas
##                                  other navigation requests (for example from
##                                  JavaScript) are suppressed.
##   - allow-all: Allows all navigation requests to URLs with unknown schemes.
## On QtWebEngine, this setting requires Qt 5.11 or newer.
## On QtWebKit, this setting is unavailable.
# c.content.unknown_url_scheme_policy = "allow-from-user-interaction"

## A list of user stylesheet filenames to use.
## Type: List of File, or File
# c.content.user_stylesheets = []

## Enables or disables WebGL.
## Type: Bool
# c.content.webgl = True

## Which interfaces to expose via WebRTC. On Qt 5.10, this option doesn’t
## work because of a Qt bug. This setting requires a restart.
## Type: String
## Valid values:
##   - all-interfaces: WebRTC has the right to enumerate all interfaces and
##       bind them to discover public interfaces.
##   - default-public-and-private-interfaces: WebRTC should only use the
##       default route used by http. This also exposes the associated default private address. Default route is the route chosen by the OS on a multi-homed endpoint.
##   - default-public-interface-only: WebRTC should only use the default
##       route used by http. This doesn’t expose any local addresses.
##   - disable-non-proxied-udp: WebRTC should only use TCP to contact peers
##       or servers unless the proxy server supports UDP. This doesn’t expose any local addresses either.
## Default: all-interfaces
## On QtWebEngine, this setting requires Qt 5.9.2 or newer.
## On QtWebKit, this setting is unavailable.
# c.content.webrtc_ip_handling_policy = 'all-interfaces'

## Set fullscreen notification overlay timeout in milliseconds. If set to 0,
## no overlay will be displayed.
## Type: Int
# c.content.fullscreen.overlay_timeout = 3000

## Limit fullscreen to the browser window (does not expand to fill the
## screen).
## Type: Bool
# c.content.fullscreen.window = False

## Monitor load requests for cross-site scripting attempts. Suspicious
## scripts will be blocked and reported in the inspector’s JavaScript
## console. Note that bypasses for the XSS auditor are widely known and
## it can be abused for cross-site info leaks in some scenarios,
## see: https://www.chromium.org/developers/design-documents/xss-auditor
## This setting supports URL patterns.
## Type: Bool
# c.content.xss_auditing = False

## The directory to save downloads to. If unset, a sensible os-specific
## default is used.
## Type: Directory
# c.downloads.location.directory = None

## Prompt the user for the download location. If set to false,
## `downloads.location.directory` will be used.
## Type: Bool
# c.downloads.location.prompt = True

## Remember the last used download directory.
## Type: Bool
# c.downloads.location.remember = True

## What to display in the download filename input.
## Type: String
## Valid values:
##   - path: Show only the download path.
##   - filename: Show only download filename.
##   - both: Show download path and filename.
# c.downloads.location.suggestion = 'path'

## The default program used to open downloads. If null, the default
## internal handler is used. Any `{}` in the string will be expanded to
## the filename, else the filename will be appended.
## Type: String
# c.downloads.open_dispatcher = None

## Where to show the downloaded files.
## Type: VerticalPosition
## Valid values:
##   - top
##   - bottom
# c.downloads.position = 'top'

## Number of milliseconds to wait before removing finished downloads. If
## set to -1, downloads are never removed.
## Type: Int
# c.downloads.remove_finished = -1

## The editor (and arguments) to use for the `open-editor` command. `{}`
## gets replaced by the filename of the file to be edited.
## Type: ShellCommand
# c.editor.command = ['gvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']
c.editor.command = ['subl', '-a', '{}']

## Encoding to use for the editor.
## Type: Encoding
# c.editor.encoding = 'utf-8'

## Handler for selecting file(s) in forms. If external, then the commands
## specified by fileselect.single_file.command and
## fileselect.multiple_files.command are used to select one or multiple files
## respectively.
## Type: String
## Valid values:
##   - default: Use the default file selector.
##   - external: Use an external command.
# c.fileselect.handler = "default"

## Command (and arguments) to use for selecting multiple files in forms. The
## command should write the selected file paths to the specified file,
## separated by newlines. The following placeholders are defined: * {}:
## Filename of the file to be written to.
## Type: ShellCommand
# c.fileselect.multiple_files.command = ['xterm', '-e', 'ranger', '--choosefiles={}']

## Command (and arguments) to use for selecting a single file in forms. The
## command should write the selected file path to the specified file. The
## following placeholders are defined: * {}: Filename of the file to be
## written to.
## Type: ShellCommand
# c.fileselect.single_file.command = ['xterm', '-e', 'ranger', '--choosefile={}']

## The maximum time in minutes between two history items for them to be
## considered being from the same browsing session. Items with less time
## between them are grouped when being displayed in `:history`. Use -1 to
## disable separation.
## Type: Int
# c.history_gap_interval = 30

## Allow Escape to quit the crash reporter.
## Type: Bool
# c.input.escape_quits_reporter = True

## Find text on a page case-insensitively.
## Type: String
## Valid values:
##   - always: Search case-insensitively
##   - never: Search case-sensitively
##   - smart: Search case-sensitively if there are capital chars
# c.search.ignore_case = 'smart'

## Forward unbound keys to the webview in normal mode.
## Type: String
## Valid values:
##   - all: Forward all unbound keys.
##   - auto: Forward unbound non-alphanumeric keys.
##   - none: Don't forward any keys.
# c.input.forward_unbound_keys = 'auto'

## Enter insert mode if an editable element is clicked.
## Type: Bool
# c.input.insert_mode.auto_enter = True

## Leave insert mode if a non-editable element is clicked.
## Type: Bool
# c.input.insert_mode.auto_leave = True

## Automatically enter insert mode if an editable element is focused
## after loading the page.
## Type: Bool
# c.input.insert_mode.auto_load = False

## Leave insert mode when starting a new page load. Patterns may be
## unreliable on this setting, and they may match the url you are navigating
## to, or the URL you are navigating from.
## This setting supports URL patterns.
## Type: Bool
# c.input.insert_mode.leave_on_load = True

## Switch to insert mode when clicking flash and other plugins.
## Type: Bool
# c.input.insert_mode.plugins = False

## Include hyperlinks in the keyboard focus chain when tabbing.
## Type: Bool
# c.input.links_included_in_focus_chain = True

## Timeout (in milliseconds) for partially typed key bindings. If the
## current input forms only partial matches, the keystring will be
## cleared after this time.
## Type: Int
# c.input.partial_timeout = 0

## Enable back and forward buttons on the mouse.
## Type: Bool
# c.input.mouse.back_forward_buttons = True

## Enable Opera-like mouse rocker gestures. This disables the context
## menu.
## Type: Bool
# c.input.mouse.rocker_gestures = False

## Enable Spatial Navigation. Spatial navigation consists in the ability
## to navigate between focusable elements in a Web page, such as
## hyperlinks and form controls, by using Left, Right, Up and Down arrow
## keys. For example, if a user presses the Right key, heuristics
## determine whether there is an element he might be trying to reach
## towards the right and which element he probably wants.
## Type: Bool
# c.input.spatial_navigation = False

## Keychains that shouldn't be shown in the keyhint dialog. Globs are
## supported, so `;*` will blacklist all keychains starting with `;`. Use
## `*` to disable keyhints.
## Type: List of String
# c.keyhint.blacklist = []

## Time from pressing a key to seeing the keyhint dialog (ms).
## Type: Int
# c.keyhint.delay = 500

## Level for console (stdout/stderr) logs. Ignored if the --loglevel or
## --debug CLI flags are used.
## Type: LogLevel
## Valid values:
##   - vdebug
##   - debug
##   - info
##   - warning
##   - error
##   - critical
## Default: info
# c.logging.level.console = "info"

## Level for in-memory logs.
## Type: LogLevel
## Valid values:
##   - vdebug
##   - debug
##   - info
##   - warning
##   - error
##   - critical
## Default: debug
# c.logging.level.ram = "debug"

# Time (in ms) to show messages in the statusbar for. Set to 0 to never
# clear messages.
# Type: Int
# c.messages.timeout = 3000
c.messages.timeout = 5000

## How to open links in an existing instance if a new one is launched.
## This happens when e.g. opening a link from a terminal. See
## `new_instance_open_target_window` to customize in which window the
## link is opened in.
## Type: String
## Valid values:
##   - tab: Open a new tab in the existing window and activate the window.
##   - tab-bg: Open a new background tab in the existing window and activate the window.
##   - tab-silent: Open a new tab in the existing window without activating the window.
##   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
##   - window: Open in a new window.
# c.new_instance_open_target = 'tab'

## Which window to choose when opening links as new tabs. When
## `new_instance_open_target` is not set to `window`, this is ignored.
## Type: String
## Valid values:
##   - first-opened: Open new tabs in the first (oldest) opened window.
##   - last-opened: Open new tabs in the last (newest) opened window.
##   - last-focused: Open new tabs in the most recently focused window.
##   - last-visible: Open new tabs in the most recently visible window.
# c.new_instance_open_target_window = 'last-focused'

## Show a filebrowser in upload/download prompts.
## Type: Bool
# c.prompt.filebrowser = True

## Additional arguments to pass to Qt, without leading `--`. With
## QtWebEngine, some Chromium arguments (see
## https://peter.sh/experiments/chromium-command-line-switches/ for a
## list) will work. This setting requires a restart.
## Type: List of String
# c.qt.args = []

## Additional environment variables to set. Setting an environment variable to
## null/None will unset it.
## This setting requires a restart.
## Type: Dict
# c.qt.environ = {}

## Force a Qt platform to use. This sets the `QT_QPA_PLATFORM`
## environment variable and is useful to force using the XCB plugin when
## running QtWebEngine on Wayland.
## Type: String
# c.qt.force_platform = None

## Force a Qt platformtheme to use. This sets the `QT_QPA_PLATFORMTHEME`
## environment variable which controls dialogs like the filepicker.
## By default, Qt determines the platform theme based on the desktop
## environment. This setting requires a restart.
## Type: String
# c.qt.force_platformtheme = None

## Force software rendering for QtWebEngine. This is needed for
## QtWebEngine to work with Nouveau drivers. This setting requires a
## restart.
## Type: String
## Valid values:
##   - software-opengl: Tell LibGL to use a software implementation of GL (LIBGL_ALWAYS_SOFTWARE / QT_XCB_FORCE_SOFTWARE_OPENGL)
##   - qt-quick: Tell Qt Quick to use a software renderer instead of OpenGL. (QT_QUICK_BACKEND=software)
##   - chromium: Tell Chromium to disable GPU support and use Skia software rendering instead. (--disable-gpu)
##   - none: Don’t force software rendering.
# c.qt.force_software_rendering = 'none'

## Turn on Qt HighDPI scaling. This is equivalent to setting
## QT_AUTO_SCREEN_SCALE_FACTOR=1 in the environment. It's off by default
## as it can cause issues with some bitmap fonts. As an alternative to
## this, it's possible to set font sizes and the `zoom.default` setting.
## Type: Bool
# c.qt.highdpi = False

## Use Chromium’s low-end device mode. This improves the RAM usage of renderer processes, at the expense of performance. This setting requires a restart.
## Type: String
## Valid values:
##   - always: Always use low-end device mode.
##   - auto: Decide automatically (uses low-end mode with < 1 GB available RAM).
##   - never: Never use low-end device mode.
## Default: auto
## This setting is only available with the QtWebEngine backend.
# c.qt.low_end_device_mode = 'auto'

## Which Chromium process model to use. Alternative process models use less
## resources, but decrease security and robustness. See the following pages
## for more details:
## https://www.chromium.org/developers/design-documents/process-models
## https://doc.qt.io/qt-5/qtwebengine-features.html#process-models
## This setting requires a restart.
## Type: String
## Valid values:
##   - process-per-site-instance: Pages from separate sites are put into
##       separate processes and separate visits to the same site are also
##       isolated.
##   - process-per-site: Pages from separate sites are put into separate
##       processes. Unlike Process per Site Instance, all visits to the same
##       site will share an OS process. The benefit of this model is reduced
##       memory consumption, because more web pages will share processes. The drawbacks include reduced security, robustness, and responsiveness.
##   - single-process: Run all tabs in a single process. This should be used
##       for debugging purposes only, and it disables :open --private.
## Default: process-per-site-instance
## This setting is only available with the QtWebEngine backend.
# c.qt.process_model = 'process-per-site-instance'

## Delete the QtWebEngine Service Worker directory on every start. This
## workaround can help with certain crashes caused by an unknown QtWebEngine
## bug related to Service Workers. Those crashes happen seemingly immediately
## on Windows; after one hour of operation on other systems. Note however that
## enabling this option can lead to data loss on some pages (as Service Worker
## data isn’t persisted) and will negatively impact start-up time.
## Type: Bool
# c.qt.workarounds.remove_service_workers = False

## Enable smooth scrolling for web pages. Note smooth scrolling does not
## work with the `:scroll-px` command.
## Type: Bool
# c.scrolling.smooth = False

## When to find text on a page case-insensitively.
## Type: String
## Valid values:
##   - always: Search case-insensitively.
##   - never: Search case-sensitively.
##   - smart: Search case-sensitively if there are capital characters.
# c.search.ignore_case = 'smart'

## Find text on a page incrementally, renewing the search for each typed
## character.
## Type: Bool
# c.search.incremental = True

## Wrap around at the top and bottom of the page when advancing through text
## matches using :search-next and :search-prev.
## Type: Bool
## On QtWebEngine, this setting requires Qt 5.14 or newer.
# c.search.wrap = True

## The name of the session to save by default. If this is set to null,
## the session which was last loaded is saved.
## Type: SessionName
# c.session.default_name = None

## Load a restored tab as soon as it takes focus.
## Type: Bool
# c.session.lazy_restore = False
c.session.lazy_restore = True

## Spell checking languages. You can check for available languages and
## install dictionaries using scripts/install_dict.py. Run the script
## with -h/--help for instructions.
## Type: List of String
## Valid values:
##   - af-ZA: Afrikaans (South Africa)
##   - bg-BG: Bulgarian (Bulgaria)
##   - ca-ES: Catalan (Spain)
##   - cs-CZ: Czech (Czech Republic)
##   - da-DK: Danish (Denmark)
##   - de-DE: German (Germany)
##   - el-GR: Greek (Greece)
##   - en-CA: English (Canada)
##   - en-GB: English (United Kingdom)
##   - en-US: English (United States)
##   - es-ES: Spanish (Spain)
##   - et-EE: Estonian (Estonia)
##   - fa-IR: Farsi (Iran)
##   - fo-FO: Faroese (Faroe Islands)
##   - fr-FR: French (France)
##   - he-IL: Hebrew (Israel)
##   - hi-IN: Hindi (India)
##   - hr-HR: Croatian (Croatia)
##   - hu-HU: Hungarian (Hungary)
##   - id-ID: Indonesian (Indonesia)
##   - it-IT: Italian (Italy)
##   - ko: Korean
##   - lt-LT: Lithuanian (Lithuania)
##   - lv-LV: Latvian (Latvia)
##   - nb-NO: Norwegian (Norway)
##   - nl-NL: Dutch (Netherlands)
##   - pl-PL: Polish (Poland)
##   - pt-BR: Portuguese (Brazil)
##   - pt-PT: Portuguese (Portugal)
##   - ro-RO: Romanian (Romania)
##   - ru-RU: Russian (Russia)
##   - sh: Serbo-Croatian
##   - sk-SK: Slovak (Slovakia)
##   - sl-SI: Slovenian (Slovenia)
##   - sq: Albanian
##   - sr: Serbian
##   - sv-SE: Swedish (Sweden)
##   - ta-IN: Tamil (India)
##   - tg-TG: Tajik (Tajikistan)
##   - tr-TR: Turkish (Turkey)
##   - uk-UA: Ukrainian (Ukraine)
##   - vi-VN: Vietnamese (Viet Nam)
# c.spellcheck.languages = []

## Open new tabs (middleclick/ctrl+click) in the background.
## Type: Bool
# c.tabs.background = True

## On which mouse button to close tabs.
## Type: String
## Valid values:
##   - right: Close tabs on right-click.
##   - middle: Close tabs on middle-click.
##   - none: Don't close tabs using the mouse.
# c.tabs.close_mouse_button = 'middle'

## How to behave when the close mouse button is pressed on the tab bar.
## Type: String
## Valid values:
##   - new-tab: Open a new tab.
##   - close-current: Close the current tab.
##   - close-last: Close the last tab.
##   - ignore: Don't do anything.
# c.tabs.close_mouse_button_on_bar = 'new-tab'

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

## Switch between tabs using the mouse wheel.
## Type: Bool
# c.tabs.mousewheel_switching = True

## Position of new tabs opened from another tab. See
## `tabs.new_position.stacking` for controlling stacking behavior.
## Type: NewTabPosition
## Valid values:
##   - prev: Before the current tab.
##   - next: After the current tab.
##   - first: At the beginning.
##   - last: At the end.
# c.tabs.new_position.related = 'next'

## Stack related tabs on top of each other when opened consecutively.
## Only applies for `next` and `prev` values of
## `tabs.new_position.related` and `tabs.new_position.unrelated`.
## Type: Bool
# c.tabs.new_position.stacking = True

## How new tabs which aren't opened from another tab are positioned.
## Type: NewTabPosition
## Valid values:
##   - prev: Before the current tab.
##   - next: After the current tab.
##   - first: At the beginning.
##   - last: At the end.
# c.tabs.new_position.unrelated = 'last'

## When switching tabs, what input mode is applied.
## Type: String
## Valid values:
##   - persist: Retain the current mode.
##   - restore: Restore previously saved mode.
##   - normal: Always revert to normal mode.
# c.tabs.mode_on_change = 'normal'

## Force pinned tabs to stay at fixed URL.
## Type: Bool
# c.tabs.pinned.frozen = True

## Shrink pinned tabs down to their contents.
## Type: Bool
# c.tabs.pinned.shrink = True

## Which tab to select when the focused tab is removed.
## Type: SelectOnRemove
## Valid values:
##   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
##   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
##   - last-used: Select the previously selected tab.
# c.tabs.select_on_remove = 'next'

## Open a new window for every tab.
## Type: Bool
# c.tabs.tabs_are_windows = False

## Whether to wrap when changing tabs.
## Type: Bool
# c.tabs.wrap = True

## Whether to start a search when something else than a URL is entered.
## Type: String
## Valid values:
##   - naive: Use simple/naive check.
##   - dns: Use DNS requests (might be slow!).
##   - never: Never search automatically.
# c.url.auto_search = 'naive'

## The page to open if :open -t/-b/-w is used without URL. Use
## `about:blank` for a blank page.
## Type: FuzzyUrl
# c.url.default_page = 'https://start.duckduckgo.com/'
c.url.default_page = STARTPAGE

## The URL segments where `:navigate increment/decrement` will search for
## a number.
## Type: FlagList
## Valid values:
##   - host
##   - path
##   - query
##   - anchor
# c.url.incdec_segments = ['path', 'query']

## Open base URL of the searchengine if a searchengine shortcut is invoked
## without parameters.
## Type: Bool
# c.url.open_base_url = False
c.url.open_base_url = True

## The page(s) to open at the start.
## Type: List of FuzzyUrl, or FuzzyUrl
# c.url.start_pages = ['https://start.duckduckgo.com']
c.url.start_pages = [STARTPAGE]

## The URL parameters to strip with `:yank url`.
## Type: List of String
# c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']

## The default zoom level.
## Type: Perc
# c.zoom.default = '100%'

## The available zoom levels.
## Type: List of Perc
# c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']

## How much to divide the mouse wheel movements to translate them into
## zoom increments.
## Type: Int
# c.zoom.mouse_divider = 512

## Whether the zoom factor on a frame applies only to the text or to all
## content.
## Type: Bool
# c.zoom.text_only = False
