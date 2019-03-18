# Dotfiles
I manage my dotfiles using [dotdrop](https://github.com/deadc0de6/dotdrop).

# Packages
A not exhaustive list of things I use for my GUI systems:
 - [Ario](http://ario-player.sourceforge.net/)
 - [AwOken](https://alecive.deviantart.com/art/AwOken-163570862)
 - [cower](https://github.com/falconindy/cower)
 - [dotdrop](https://github.com/deadc0de6/dotdrop)
 - [Droid Sans Mono](http://www.droidfonts.com/)
 - [dunst](https://github.com/dunst-project/dunst)
 - [Fira Code](https://github.com/tonsky/FiraCode)
 - [Font-Awesome](https://github.com/FortAwesome/Font-Awesome)
 - [Guake](https://github.com/Guake/guake)
 - [gvim](http://www.vim.org/)
 - [i3ipc-python](https://github.com/acrisci/i3ipc-python)
 - [i3](https://github.com/i3/i3)
 - [i3lock](https://github.com/i3/i3lock)
 - [i3status](https://github.com/i3/i3status)
 - [libnotify](https://developer.gnome.org/libnotify/)
 - [lxappearance](https://wiki.lxde.org/de/LXAppearance)
 - [MFixx](https://github.com/file-icons/MFixx) (edited version: moved all glyphs to private area in order to avoid conflicts with font-awesome. Plus some additional glyphs)
 - [mpc](https://github.com/MusicPlayerDaemon/mpc)
 - [nemo](https://github.com/linuxmint/nemo)
 - [nemo-fileroller](https://github.com/linuxmint/nemo-extensions/tree/master/nemo-fileroller)
 - [nemo-python](https://github.com/linuxmint/nemo-extensions/tree/master/nemo-python)
 - [nemo-seahorse](https://github.com/linuxmint/nemo-extensions/tree/master/nemo-seahorse)
 - [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
 - [pdfjs](https://github.com/mozilla/pdf.js)
 - [powerline](https://github.com/powerline/powerline)
 - [py3status](https://github.com/ultrabug/py3status)
 - [qt5-styleplugins](http://code.qt.io/cgit/qt/qtstyleplugins.git)
 - [qutebrowser](https://github.com/qutebrowser/qutebrowser)
 - [qutebrowser-compare-config](https://github.com/open-dynaMIX/qutebrowser-compare-config)
 - [raiseorlaunch](https://github.com/open-dynaMIX/raiseorlaunch)
 - [rofi](https://github.com/DaveDavenport/rofi)
 - [rofi-dmenu](https://aur.archlinux.org/packages/rofi-dmenu/)
 - [screen](https://www.gnu.org/software/screen/)
 - [Scribes](http://scribes.sourceforge.net/)
 - [simple-mpv-webui](https://github.com/open-dynaMIX/simple-mpv-webui)
 - [streamwall](https://github.com/open-dynaMIX/streamwall)
 - [termite](https://github.com/thestinger/termite)
 - [time](https://directory.fsf.org/wiki/Time)
 - [transset-df](http://forchheimer.se/transset-df/)
 - [unclutter-patched](https://aur.archlinux.org/packages/unclutter-patched/)
 - [viewnior](https://siyanpanayotov.com/project/viewnior/)
 - [vundle](https://github.com/VundleVim/Vundle.vim)
 - [xcompmgr](https://cgit.freedesktop.org/xorg/app/xcompmgr/)
 - [xdotool](https://github.com/jordansissel/xdotool)
 - [xterm](https://invisible-island.net/xterm/xterm.html)
 - [youtube-dl](https://github.com/rg3/youtube-dl)
 - [zathura](https://github.com/pwmt/zathura)
 - [zathura-pdf-poppler](https://github.com/pwmt/zathura-pdf-poppler)
 - [zsh](https://www.zsh.org/)
 - [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
 - [zsh-completions](https://github.com/zsh-users/zsh-completions)
 - [zsh-history-substring-search](https://github.com/zsh-users/zsh-history-substring-search)
 - [zsh-pure-prompt](https://github.com/sindresorhus/pure)
 - [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)

# Install

``` shell
yay -S ario awoken-icons dotdrop dunst otf-font-awesome guake gvim i3ipc-python-git i3-wm i3lock i3status libnotify lxappearance nemo nemo-fileroller nemo-python nemo-seahorse-nonautilus mpc oh-my-zsh-git otf-fira-code pdfjs powerline powerline-fonts py3status qt5ct qt5-styleplugins qutebrowser-git raiseorlaunch rofi rofi-dmenu screen scribes termite time transset-df ttf-droid unclutter-patched viewnior xcompmgr xdotool xterm youtube-dl zathura zathura-pdf-poppler zsh zsh-autosuggestions zsh-completions zsh-history-substring-search zsh-pure-prompt zsh-syntax-highlighting
```

# py3status

![i3bar with py3status screenshot](screenshots/i3bar_py3status.png "i3bar with py3status screenshot")

# Configuring theme
To have a uniform look for gtk, qt4 and qt5, the theme needs to be configured in

 - lxappearance
 - qtconfig-qt4
 - qt5ct

Add `export QT_QPA_PLATFORMTHEME=qt5ct` and `export QT_AUTO_SCREEN_SCALE_FACTOR=0` to `.xinitrc`.

# Set some default applications
``` bash
xdg-settings set default-web-browser qutebrowser.desktop
xdg-mime default nemo.desktop inode/directory
xdg-mime default org.pwmt.zathura-pdf-poppler.desktop application/pdf
```
