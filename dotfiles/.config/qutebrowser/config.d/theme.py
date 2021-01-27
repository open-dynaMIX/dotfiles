# {{@@ header() @@}}
# flake8: noqa: E266


PURPLE = '#470f77'

c = c  # noqa
config = config  # noqa

## Width (in pixels or as percentage of the window) of the tab bar if
## it's vertical.
## Type: PercOrInt
# c.tabs.width = '15%'

## Width (in pixels) of the progress indicator (0 to disable).
## Type: Int
# c.tabs.indicator.width = 3

## Padding (in pixels) for tab indicators.
## Type: Padding
# c.tabs.indicator.padding = {'top': 2, 'bottom': 2, 'left': 0, 'right': 4}

## Maximum width (in pixels) of tabs (-1 for no maximum). This setting
## only applies when tabs are horizontal. This setting does not apply to
## pinned tabs, unless `tabs.pinned.shrink` is False. This setting may
## not apply properly if max_width is smaller than the minimum size of
## tab contents, or smaller than tabs.min_width.
## Type: Int
# c.tabs.max_width = -1

## Minimum width (in pixels) of tabs
## (-1 for the default minimum size behavior).
## This setting only applies when tabs are horizontal.
## This setting does not apply to pinned tabs,
##unless tabs.pinned.shrink is False.
## Type: Int
# c.tabs.min_width = -1

## The height of the completion, in px or as percentage of the window.
## Type: PercOrInt
# c.completion.height = '50%'

## Padding of scrollbar handle in the completion window (in px).
## Type: Int
# c.completion.scrollbar.padding = 2

## Width of the scrollbar in the completion window (in px).
## Type: Int
# c.completion.scrollbar.width = 12

## Shrink the completion to be smaller than the configured size if there
## are no scrollbars.
## Type: Bool
# c.completion.shrink = False

## The rounding radius for the edges of prompts.
## Type: Int
# c.prompt.radius = 8
c.prompt.radius = 0

## When to show a scrollbar.
## Type: String
## Valid values:
##   - always: Always show the scrollbar.
##   - never: Never show the scrollbar.
##   - when-searching: Show the scrollbar when searching for text in the
##                     webpage. With the QtWebKit backend, this is equal to
##                     never.
##   - overlay: Show an overlay scrollbar. With Qt < 5.11 or on macOS, this is
##                     unavailable and equal to when-searching; with the
##                     QtWebKit backend, this is equal to never.
##                     Enabling/disabling overlay scrollbars requires a restart.
# c.scrolling.bar = 'overlay'

## When to show the statusbar.
## Type: String
## Valid values:
##   - always: Always show the statusbar.
##   - always: Always show the statusbar.
##   - never: Always hide the statusbar.
##   - in-mode: Show the statusbar when in modes other than normal mode.
# c.statusbar.show = "always"

## Padding for the statusbar.
## Type: Padding
# c.statusbar.padding = {'top': 1, 'bottom': 1, 'left': 0, 'right': 0}

## The position of the status bar.
## Type: VerticalPosition
## Valid values:
##   - top
##   - bottom
# c.statusbar.position = 'bottom'

## Scaling for favicons in the tab bar. The tab size is unchanged, so big
## favicons also require extra `tabs.padding`.
## Type: Float
# c.tabs.favicons.scale = 1.0

## When to show favicons in the tab bar.
## Type: String
# c.tabs.favicons.show = 'always'

## Maximum stack size to remember for tab switches (-1 for no maximum).
## Type: Int
# c.tabs.focus_stack_size = 10

## Padding around text for tabs
## Type: Padding
# c.tabs.padding = {'top': 0, 'bottom': 0, 'left': 5, 'right': 5}

## The position of the tab bar.
## Type: Position
## Valid values:
##   - top
##   - bottom
##   - left
##   - right
# c.tabs.position = 'top'

## Alignment of the text inside of tabs.
## Type: TextAlignment
## Valid values:
##   - left
##   - right
##   - center
# c.tabs.title.alignment = 'left'

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

## The format to use for the tab title for pinned tabs. The same
## placeholders like for `tabs.title.format` are defined.
## Type: FormatString
# c.tabs.title.format_pinned = '{index}'

## Show tooltips on tabs. Note this setting only affects windows opened
## after it has been set.
## Type: Bool
# c.tabs.tooltips = True

## Number of close tab actions to remember, per window (-1 for no maximum).
## Type: Int
# c.tabs.undo_stack_size = 100

## When to show the tab bar.
## Type: String
## Valid values:
##   - always: Always show the tab bar.
##   - never: Always hide the tab bar.
##   - multiple: Hide the tab bar if only one tab is open.
##   - switching: Show the tab bar when switching tabs.
# c.tabs.show = 'always'

## Time to show the tab bar before hiding it when tabs.show is set to
## 'switching'.
## Type: Int
# c.tabs.show_switching_delay = 800

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

## Hide the window decoration
## This setting requires a restart on Wayland.
## Type: Bool
# c.window.hide_decoration = False

## The format to use for the window title. The following placeholders are
## defined:  * `{perc}`: The percentage as a string like `[10%]`. *
## `{perc_raw}`: The raw percentage, e.g. `10` * `{title}`: The title of
## the current web page * `{title_sep}`: The string ` - ` if a title is
## set, empty otherwise. * `{id}`: The internal window ID of this window.
## * `{scroll_pos}`: The page scroll position. * `{host}`: The host of
## the current web page. * `{backend}`: Either ''webkit'' or
## ''webengine'' * `{private}` : Indicates when private mode is enabled.
## Type: FormatString
# c.window.title_format = '{perc}{current_title}{title_sep}qutebrowser'


## Set the main window background to transparent.
## This allows having a transparent tab- or statusbar (might require a
## compositor such as picom). However, it breaks some functionality such as
## dmenu embedding via its -w option. On some systems, it was additionally
## reported that main window transparency negatively affects performance.
## Note this setting only affects windows opened after setting it.
## Type: Bool
# c.window.transparent = False

##############################################################################
# COLORS
##############################################################################

## Background color of the completion widget category headers.
## Type: QssColor
# c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #888888, stop:1 #505050)'
c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {0}, stop:1 {0})'.format(PURPLE)

## Bottom border color of the completion widget category headers.
## Type: QssColor
# c.colors.completion.category.border.bottom = 'black'

## Top border color of the completion widget category headers.
## Type: QssColor
# c.colors.completion.category.border.top = 'black'

## Foreground color of completion widget category headers.
## Type: QtColor
# c.colors.completion.category.fg = 'white'

## Background color of the completion widget for even rows.
## Type: QssColor
# c.colors.completion.even.bg = '#333333'

## Text color of the completion widget.
## May be a single color to use for all columns or a list of three colors,
## one for each column.
## Type: List of QtColor, or QtColor
# c.colors.completion.fg = ['white', 'white', 'white']

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

## Foreground color of the matched text in the selected completion item.
## Type: QtColor
# c.colors.completion.item.selected.match.fg = '#ff4444'

## Foreground color of the matched text in the completion.
## Type: QssColor
# c.colors.completion.match.fg = '#ff4444'

## Background color of the completion widget for odd rows.
## Type: QssColor
# c.colors.completion.odd.bg = '#444444'

## Color of the scrollbar in completion view
## Type: QssColor
# c.colors.completion.scrollbar.bg = '#333333'

## Color of the scrollbar handle in completion view.
## Type: QssColor
# c.colors.completion.scrollbar.fg = 'white'

## Background color of disabled items in the context menu.
## If set to null, the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.disabled.bg = None

## Foreground color of disabled items in the context menu.
## If set to null, the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.disabled.fg = None

## Background color of the context menu.
## If set to null, the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.menu.bg = None

## Foreground color of the context menu.
## If set to null, the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.menu.fg = None

## Background color of the context menu’s selected item.
## If set to null, the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.selected.bg = None
c.colors.contextmenu.selected.bg = PURPLE

## Foreground color of the context menu’s selected item.
## If set to null, the Qt default is used.
## Type: QssColor
# c.colors.contextmenu.selected.fg = None

## Background color for the download bar.
## Type: QssColor
# c.colors.downloads.bar.bg = 'black'

## Background color for downloads with errors.
## Type: QtColor
# c.colors.downloads.error.bg = 'red'

## Foreground color for downloads with errors.
## Type: QtColor
# c.colors.downloads.error.fg = 'white'

## Color gradient start for download backgrounds.
## Type: QtColor
# c.colors.downloads.start.bg = '#0000aa'

## Color gradient start for download text.
## Type: QtColor
# c.colors.downloads.start.fg = 'white'

## Color gradient stop for download backgrounds.
## Type: QtColor
# c.colors.downloads.stop.bg = '#00aa00'

## Color gradient end for download text.
## Type: QtColor
# c.colors.downloads.stop.fg = 'white'

## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.downloads.system.bg = 'rgb'

## Color gradient interpolation system for download text.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.downloads.system.fg = 'rgb'

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

## Background color of the keyhint widget.
## Type: QssColor
# c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'

## Text color for the keyhint widget.
## Type: QssColor
# c.colors.keyhint.fg = '#FFFFFF'

## Rounding radius (in pixels) for the edges of the keyhint dialog.
## Type: Int
# c.keyhint.radius = 6
c.keyhint.radius = 0

## Highlight color for keys to complete the current keychain.
## Type: QssColor
# c.colors.keyhint.suffix.fg = '#FFFF00'

## Background color of an error message.
## Type: QssColor
# c.colors.messages.error.bg = 'red'

## Border color of an error message.
## Type: QssColor
# c.colors.messages.error.border = '#bb0000'

## Foreground color of an error message.
## Type: QssColor
# c.colors.messages.error.fg = 'white'

## Background color of an info message.
## Type: QssColor
# c.colors.messages.info.bg = 'black'

## Border color of an info message.
## Type: QssColor
# c.colors.messages.info.border = '#333333'

## Foreground color an info message.
## Type: QssColor
# c.colors.messages.info.fg = 'white'

## Background color of a warning message.
## Type: QssColor
# c.colors.messages.warning.bg = 'darkorange'
c.colors.messages.warning.bg = PURPLE

## Border color of a warning message.
## Type: QssColor
# c.colors.messages.warning.border = '#d47300'
c.colors.messages.warning.border = PURPLE

## Foreground color a warning message.
## Type: QssColor
# c.colors.messages.warning.fg = 'white'

## Background color for prompts.
## Type: QssColor
# c.colors.prompts.bg = '#444444'

## Border used around UI elements in prompts.
## Type: String
# c.colors.prompts.border = '1px solid gray'

## Foreground color for prompts.
## Type: QssColor
# c.colors.prompts.fg = 'white'

## Background color for the selected item in filename prompts.
## Type: QssColor
# c.colors.prompts.selected.bg = 'grey'

## Background color of the statusbar in caret mode.
## Type: QssColor
# c.colors.statusbar.caret.bg = 'purple'
c.colors.statusbar.caret.bg = PURPLE

## Foreground color of the statusbar in caret mode.
## Type: QssColor
# c.colors.statusbar.caret.fg = 'white'

## Background color of the statusbar in caret mode with a selection.
## Type: QssColor
# c.colors.statusbar.caret.selection.bg = '#a12dff'

## Foreground color of the statusbar in caret mode with a selection.
## Type: QssColor
# c.colors.statusbar.caret.selection.fg = 'white'

## Background color of the statusbar in command mode.
## Type: QssColor
# c.colors.statusbar.command.bg = 'black'

## Foreground color of the statusbar in command mode.
## Type: QssColor
# c.colors.statusbar.command.fg = 'white'

## Background color of the statusbar in private browsing + command mode.
## Type: QssColor
# c.colors.statusbar.command.private.bg = 'darkslategray'
c.colors.statusbar.command.private.bg = 'red'

## Foreground color of the statusbar in private browsing + command mode.
## Type: QssColor
# c.colors.statusbar.command.private.fg = 'white'

## Background color of the statusbar in insert mode.
## Type: QssColor
# c.colors.statusbar.insert.bg = 'darkgreen'

## Foreground color of the statusbar in insert mode.
## Type: QssColor
# c.colors.statusbar.insert.fg = 'white'

## Background color of the statusbar.
## Type: QssColor
# c.colors.statusbar.normal.bg = 'black'

## Foreground color of the statusbar.
## Type: QssColor
# c.colors.statusbar.normal.fg = 'white'

## Background color of the statusbar in passthrough mode.
## Type: QssColor
# c.colors.statusbar.passthrough.bg = 'darkblue'

## Foreground color of the statusbar in passthrough mode.
## Type: QssColor
# c.colors.statusbar.passthrough.fg = 'white'

## Background color of the statusbar in private browsing mode.
## Type: QssColor
# c.colors.statusbar.private.bg = '#666666'
c.colors.statusbar.private.bg = 'red'

## Foreground color of the statusbar in private browsing mode.
## Type: QssColor
# c.colors.statusbar.private.fg = 'white'

## Background color of the progress bar.
## Type: QssColor
# c.colors.statusbar.progress.bg = 'white'

## Foreground color of the URL in the statusbar on error.
## Type: QssColor
# c.colors.statusbar.url.error.fg = 'orange'

## Default foreground color of the URL in the statusbar.
## Type: QssColor
# c.colors.statusbar.url.fg = 'white'

## Foreground color of the URL in the statusbar for hovered links.
## Type: QssColor
# c.colors.statusbar.url.hover.fg = 'aqua'

## Foreground color of the URL in the statusbar on successful load
## (http).
## Type: QssColor
# c.colors.statusbar.url.success.http.fg = 'white'

## Foreground color of the URL in the statusbar on successful load
## (https).
## Type: QssColor
# c.colors.statusbar.url.success.https.fg = 'lime'

## Foreground color of the URL in the statusbar when there's a warning.
## Type: QssColor
# c.colors.statusbar.url.warn.fg = 'yellow'

## Background color of the tab bar.
## Type: QtColor
# c.colors.tabs.bar.bg = '#555555'

## Background color of unselected even tabs.
## Type: QtColor
# c.colors.tabs.even.bg = 'darkgrey'
c.colors.tabs.even.bg = '#464646'

## Foreground color of unselected even tabs.
## Type: QtColor
# c.colors.tabs.even.fg = 'white'

## Color for the tab indicator on errors.
## Type: QtColor
# c.colors.tabs.indicator.error = '#ff0000'

## Color gradient start for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.start = '#0000aa'

## Color gradient end for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.stop = '#00aa00'

## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.tabs.indicator.system = 'rgb'

## Background color of unselected odd tabs.
## Type: QtColor
# c.colors.tabs.odd.bg = 'grey'
c.colors.tabs.odd.bg = '#333333'

## Foreground color of unselected odd tabs.
## Type: QtColor
# c.colors.tabs.odd.fg = 'white'

## Background color of pinned unselected even tabs.
## Type: QtColor
# c.colors.tabs.pinned.even.bg = 'darkseagreen'

## Foreground color of pinned unselected even tabs.
## Type: QtColor
# c.colors.tabs.pinned.even.fg = 'white'

## Background color of pinned unselected odd tabs.
## Type: QtColor
# c.colors.tabs.pinned.odd.bg = 'seagreen'

## Foreground color of pinned unselected odd tabs.
## Type: QtColor
# c.colors.tabs.pinned.odd.fg = 'white'

## Background color of pinned selected even tabs.
## Type: QtColor
# c.colors.tabs.pinned.selected.even.bg = 'black'

## Foreground color of pinned selected even tabs.
## Type: QtColor
# c.colors.tabs.pinned.selected.even.fg = 'white'

## Background color of pinned selected odd tabs.
## Type: QtColor
# c.colors.tabs.pinned.selected.odd.bg = 'black'

## Foreground color of pinned selected odd tabs.
## Type: QtColor
# c.colors.tabs.pinned.selected.odd.fg = 'white'

## Background color of selected even tabs.
## Type: QtColor
# c.colors.tabs.selected.even.bg = 'black'
c.colors.tabs.selected.even.bg = PURPLE

## Foreground color of selected even tabs.
## Type: QtColor
# c.colors.tabs.selected.even.fg = 'white'

## Background color of selected odd tabs.
## Type: QtColor
# c.colors.tabs.selected.odd.bg = 'black'
c.colors.tabs.selected.odd.bg = PURPLE

## Foreground color of selected odd tabs.
## Type: QtColor
# c.colors.tabs.selected.odd.fg = 'white'

## Background color for webpages if unset (or empty to use the theme's
## color)
## Type: QtColor
# c.colors.webpage.bg = 'white'

## Which algorithm to use for modifying how colors are rendered with
## darkmode.
## Type: String
## Valid values:
##   - lightness-cielab: Modify colors by converting them to CIELAB color space and inverting the L value.
##   - lightness-hsl: Modify colors by converting them to the HSL color space and inverting the lightness (i.e. the "L" in HSL).
##   - brightness-rgb: Modify colors by subtracting each of r, g, and b from their maximum value.
# c.colors.webpage.darkmode.algorithm = 'lightness-cielab'

## Contrast for dark mode. This only has an effect when
## `colors.webpage.darkmode.algorithm` is set to `lightness-hsl` or
## `brightness-rgb`.
## Type: Float
# c.colors.webpage.darkmode.contrast = 0.0

## Render all web contents using a dark theme. Example configurations
## from Chromium's `chrome://flags`:  - "With simple HSL/CIELAB/RGB-based
## inversion": Set   `colors.webpage.darkmode.algorithm` accordingly.  -
## "With selective image inversion": Set
## `colors.webpage.darkmode.policy.images` to `smart`.  - "With selective
## inversion of non-image elements": Set
## `colors.webpage.darkmode.threshold.text` to 150 and
## `colors.webpage.darkmode.threshold.background` to 205.  - "With
## selective inversion of everything": Combines the two variants   above.
## Type: Bool
# c.colors.webpage.darkmode.enabled = False

## Render all colors as grayscale. This only has an effect when
## `colors.webpage.darkmode.algorithm` is set to `lightness-hsl` or
## `brightness-rgb`.
## Type: Bool
# c.colors.webpage.darkmode.grayscale.all = False

## Desaturation factor for images in dark mode. If set to 0, images are
## left as-is. If set to 1, images are completely grayscale. Values
## between 0 and 1 desaturate the colors accordingly.
## Type: Float
# c.colors.webpage.darkmode.grayscale.images = 0.0

## Which images to apply dark mode to. WARNING: With QtWebengine 5.15.0, this
## setting can cause frequent renderer process crashes due to a bug in Qt.
## Thus, the smart setting is ignored and treated like never in that case.
## Type: String
## Valid values:
##   - always: Apply dark mode filter to all images.
##   - never: Never apply dark mode filter to any images.
##   - smart: Apply dark mode based on image content.
# c.colors.webpage.darkmode.policy.images = 'smart'

## Which pages to apply dark mode to.
## Type: String
## Valid values:
##   - always: Apply dark mode filter to all frames, regardless of content.
##   - smart: Apply dark mode filter to frames based on background color.
# c.colors.webpage.darkmode.policy.page = 'smart'

## Threshold for inverting background elements with dark mode. Background
## elements with brightness above this threshold will be inverted, and
## below it will be left as in the original, non-dark-mode page. Set to
## 256 to never invert the color or to 0 to always invert it. Note: This
## behavior is the opposite of `colors.webpage.darkmode.threshold.text`!
## Type: Int
# c.colors.webpage.darkmode.threshold.background = 0

## Threshold for inverting text with dark mode. Text colors with
## brightness below this threshold will be inverted, and above it will be
## left as in the original, non-dark-mode page. Set to 256 to always
## invert text color or to 0 to never invert text color.
## Type: Int
# c.colors.webpage.darkmode.threshold.text = 256

## Force prefers-color-scheme: dark colors for websites.
## Type: Bool
## On QtWebEngine, this setting requires Qt 5.14 or newer.
## On QtWebKit, this setting is unavailable.
# c.colors.webpage.prefers_color_scheme_dark = False
c.colors.webpage.prefers_color_scheme_dark = True

## CSS border value for hints.
## Type: String
# c.hints.border = '1px solid #E3BE23'
c.hints.border = '1px solid #ffffff'
