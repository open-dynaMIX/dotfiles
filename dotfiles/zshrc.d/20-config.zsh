#
# ~/.zshrc.d/20-config.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

# The following lines were added by compinstall

zstyle ':completion:*' completer _complete _ignored _approximate
zstyle :compinstall filename "$HOME/.zshrc"

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=10000000
SAVEHIST=10000000
HISTFILESIZE=1000000
#setopt appendhistory
setopt notify
unsetopt beep
bindkey -v
# End of lines configured by zsh-newuser-install

setopt extendedglob
