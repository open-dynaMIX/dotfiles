#
# ~/.zshrc.d/80-transparency.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

{%@@ if env['has_x'] == "true" @@%}
[ -n "$XTERM_VERSION" ] && transset-df 0.9 -a >/dev/null || true
{%@@ endif @@%}
