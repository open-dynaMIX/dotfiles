#
# ~/.zshrc.d/85-path.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

# PATH

PATH="$HOME/.bin:${PATH}:$(ruby -e "puts Gem.user_dir")/bin:$HOME/go/bin"
