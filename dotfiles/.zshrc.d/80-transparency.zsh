#
# ~/.zshrc.d/80-transparency.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

{%@@ if env['has_x'] == "true" @@%}
[ -n "$XTERM_VERSION" ] && transset-df 0.8 -a >/dev/null || true
[ "$TERM" = "xterm-termite" ] && transset-df 0.8 -a >/dev/null || true
{%@@ endif @@%}
