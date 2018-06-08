#
# ~/.zshrc
# {{@@ env['dotdrop_warning'] @@}}
#

# load all config files
if [ -d $HOME/.zshrc.d ]; then
    for file in $HOME/.zshrc.d/*.zsh(N); do
        . $file
    done
fi
