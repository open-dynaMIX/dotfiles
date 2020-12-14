#
# ~/.zshrc.d/85-path.zsh
# {{@@ header() @@}}
#

# PATH

PATH="$HOME/.bin:${PATH}:$(ruby -e "puts Gem.user_dir")/bin:$HOME/go/bin"
