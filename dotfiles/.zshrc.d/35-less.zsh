#
# ~/.zshrc.d/35-less.zsh
# {{@@ header() @@}}
#

# enable syntax highlight in less
if [[ -f /usr/bin/src-hilite-lesspipe.sh ]]; then
    export LESSOPEN="| /usr/bin/src-hilite-lesspipe.sh %s"
fi

# default less options
export LESS='-F -i -M -R -S -W -z-4'
