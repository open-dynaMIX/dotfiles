# {{@@ env['dotdrop_warning'] @@}}
# flake8: noqa: E266


c = c  # noqa
config = config  # noqa

## Font used in the completion categories.
## Type: Font
# c.fonts.completion.category = 'bold default_size default_family'

## Font used in the completion widget.
## Type: Font
# c.fonts.completion.entry = 'default_size default_family'

## Font used for the context menu.
## If set to null, the Qt default is used.
## Type: Font
# c.fonts.contextmenu = None

## Font used for the debugging console.
## Type: QtFont
# c.fonts.debug_console = 'default_size default_family'

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

## Font used for the downloadbar.
## Type: Font
# c.fonts.downloads = 'default_size default_family'

## Font used for the hints.
## Type: Font
# c.fonts.hints = 'bold default_size default_family'

## Font used in the keyhint widget.
## Type: Font
# c.fonts.keyhint = 'default_size default_family'

## Font used for error messages.
## Type: Font
# c.fonts.messages.error = 'default_size default_family'

## Font used for info messages.
## Type: Font
# c.fonts.messages.info = 'default_size default_family'

## Font used for warning messages.
## Type: Font
# c.fonts.messages.warning = 'default_size default_family'

## Font used for prompts.
## Type: Font
# c.fonts.prompts = 'default_size sans-serif'

## Font used in the statusbar.
## Type: Font
# c.fonts.statusbar = 'default_size default_family'

## Font used in the tab bar.
## Type: QtFont
# c.fonts.tabs = 'default_size default_family'

## Font family for cursive fonts.
## Type: FontFamily
# c.fonts.web.family.cursive = ''

## Font family for fantasy fonts.
## Type: FontFamily
# c.fonts.web.family.fantasy = ''

## Font family for fixed fonts.
## Type: FontFamily
# c.fonts.web.family.fixed = ''

## Font family for sans-serif fonts.
## Type: FontFamily
# c.fonts.web.family.sans_serif = ''

## Font family for serif fonts.
## Type: FontFamily
# c.fonts.web.family.serif = ''

## Font family for standard fonts.
## Type: FontFamily
# c.fonts.web.family.standard = ''

## The default font size for regular text.
## Type: Int
# c.fonts.web.size.default = 16

## The default font size for fixed-pitch text.
## Type: Int
# c.fonts.web.size.default_fixed = 13

## The hard minimum font size.
## Type: Int
# c.fonts.web.size.minimum = 0

## The minimum logical font size that is applied when zooming out.
## Type: Int
# c.fonts.web.size.minimum_logical = 6
