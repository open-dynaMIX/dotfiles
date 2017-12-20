#!/bin/bash

gconftool-2 --dump /apps/guake > ~/.config/guake/apps-guake.xml
gconftool-2 --dump /schemas/apps/guake > ~/.config/guake/schemas-apps-guake.xml

echo "Done."
