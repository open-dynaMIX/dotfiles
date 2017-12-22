#!/bin/bash

gconftool-2 --dump /apps/guake > ~/dotfiles/dotfiles/config/guake/apps-guake.xml
gconftool-2 --dump /schemas/apps/guake > ~/dotfiles/dotfiles/config/guake/schemas-apps-guake.xml
cp ~/dotfiles/dotfiles/config/guake/apps-guake.xml ~/.config/guake/apps-guake.xml
cp ~/dotfiles/dotfiles/config/guake/schemas-apps-guake.xml ~/.config/guake/schemas-apps-guake.xml

echo "Done."
