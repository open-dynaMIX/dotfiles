#
# ~/.zshrc.d/60-prompt.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

# Pure prompt
autoload -U promptinit; promptinit
# PURE_CMD_MAX_EXEC_TIME=5
PURE_GIT_UP_ARROW="↑"
PURE_GIT_DOWN_ARROW="↓"
if [[ $EUID -eq 0 ]]; then
    PURE_PROMPT_SYMBOL="#"
# else
#     PURE_PROMPT_SYMBOL="$"
fi
prompt pure
