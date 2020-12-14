#
# ~/.zshrc.d/80-transparency.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

{%@@ if has_x @@%}
[ -n "$XTERM_VERSION" ] && transset-df 0.8 -a >/dev/null || true
[ "$TERM" = "xterm-termite" ] && transset-df 0.8 -a >/dev/null || true
{%@@ endif @@%}
