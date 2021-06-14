#
# ~/.zshrc.d/80-transparency.zsh
# {{@@ header() @@}}
#

{%@@ if has_x @@%}
[ -n "$XTERM_VERSION" ] && transset-df 0.8 -a >/dev/null || true
{%@@ endif @@%}
