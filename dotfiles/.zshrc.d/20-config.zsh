#
# ~/.zshrc.d/20-config.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

# The following lines were added by compinstall

# zstyle ':completion:*' completer _complete _ignored _approximate
# zstyle :compinstall filename "$HOME/.zshrc"

zstyle ':completion:*' completer _complete _match _approximate
zstyle ':completion:*:match:*' original only
zstyle -e ':completion:*:approximate:*' \
        max-errors 'reply=($((($#PREFIX+$#SUFFIX)/3))numeric)'
zstyle ':completion:*:*:*:*:processes' command "ps -u $(whoami) -o pid,user,comm -w -w"
zstyle ':completion:*' rehash true # this could slow down completion
zstyle :compinstall filename "$HOME/.zshrc"

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=10000000
SAVEHIST=10000000
HISTFILESIZE=1000000
setopt histignorespace
setopt appendhistory
setopt HIST_FIND_NO_DUPS
setopt notify
unsetopt beep
bindkey -v
# End of lines configured by zsh-newuser-install

disable -r time  # disable shell reserved word

setopt extendedglob
