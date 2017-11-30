#
# ~/.zshrc.d/30-exports.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

if [ "$TERM" = "xterm" ]; then
    export TERM=xterm-256color
fi

if [ -f /usr/bin/screen ]; then
    export SYSSCREENRC=/etc/screenrc
fi

if [ -f $HOME/.pythonrc ]; then
    export PYTHONSTARTUP=$HOME/.pythonrc
fi

if [[ -n $SSH_CONNECTION ]]; then
    export EDITOR='nano'
else
    export EDITOR='nano'
fi
