#
# ~/.zshrc.d/90-aliases.zsh
# {{@@ header() @@}}
#

if [[ $EUID -ne 0 ]]; then
    # alias sudo='sudo ' # needed for using aliases with sudo
    # alias please='sudo '
    alias sudo='nocorrect sudo' # needed for using aliases with sudo
    alias please='nocorrect sudo '
fi
alias ..='cd ..'
alias amiinscreen='echo $STY'
alias b='buku --suggest --deep'
alias cal='cal -m'
alias cp='cp -i'
alias dcbl='docker-compose build --pull'
alias dotdrop='eval $(cat ~/dotfiles/env.defaults ~/dotfiles/.env | grep -v "^#") /usr/bin/dotdrop --cfg=~/dotfiles/config.yaml'
alias fuck='sudo $(fc -ln -1)'
alias gti='git'
alias gst='git status -u'
alias home='cd ~/'
alias ll='ls -la'
alias ls='ls -h --color=auto --group-directories-first'
alias menu='xdg_menu | less'
alias mv='mv -i'
alias mynload='nload -t 1000 -i 500 -o 100 -u K'
alias nano='nano -cw'
alias pa='pacaur'
alias pprint='python -m json.tool'
alias radio='~/scripts/radio/radio.sh'
alias rm='rm -i'
alias timemachine="~/scripts/timemachine/timemachine.sh"
alias tv7='mpv --no-resume-playback --playlist="https://tv7api2.tv.init7.net/api/playlist/default.m3u?rp=true"'
alias seconds='while true; do; date +"%H:%M:%S"; sleep 1; done'
alias syncit='rsync -avxe ssh --delete --delete-excluded --exclude-from=$HOME/scripts/syncit/exclude $HOME/ {{@@ env['backup_user'] @@}}@{{@@ env['backup_host'] @@}}:/home/{{@@ env['backup_user'] @@}}/backups/{{@@ model @@}}/'
alias whereami='pwd'
alias worms='worms -d 40 -l 16 -n 6'
{%@@ if profile == "fuckup" @@%}
alias janosch='~/scripts/wrapper.sh --both gcompris --disable-quit --disable-config --profile janosch-profil'
alias gphoto-capture='echo "gphoto2 --capture-image-and-download --interval 20 --filename image%5n.%C"'
alias ffmpeg-convert='echo "ffmpeg -f image2 -i image%5d.jpg -vf scale=-1:1080 -qscale 1 output.mkv (-qscale can be a value 1-31 (best-worst))"'
{%@@ elif profile == "ant" @@%}
alias caluma='cd ~/code/caluma/'
{%@@ endif @@%}
{%@@ if has_x @@%}
alias x='exec startx; exit'
alias xkill='xkill -button 1'
alias qutebrowser-compare-config.py='~/code/qutebrowser-compare-config.py/qutebrowser-compare-config.py ~/.config/qutebrowser/config.d/'
{%@@ endif @@%}
if which docker > /dev/null 2>&1; then
    alias docker-cleanup='docker rm -v $(docker ps -a -q -f status=exited) && docker rmi $(docker images -f "dangling=true" -q)'
    alias dclean='docker stop $(docker ps -q)'
    alias dpurge='docker volume ls --format '{{.Name}}' | grep -E "[A-Fa-f0-9]{64}" | xargs docker volume rm'
fi
if which tremc > /dev/null 2>&1; then
    alias bt='tremc'
fi

django_secret_key() {
    if [ $# -eq 0 ]; then
        range=63
    else
        range="$1"
    fi
    python -c """\
import random
import string
choice = f\"{string.ascii_letters}{string.digits}{string.punctuation}\"
print(''.join([random.SystemRandom().choice(choice) for i in range("$range")]))
"""
}


pyenv-clean() {
    if [ -z ${PYENV_VIRTUAL_ENV+x} ]; then
        echo "Not in virtualenv. Doing nothing"
        return 0
    fi
    freeze=($(pip freeze))
    for dep in ${freeze[@]}; do
        echo $dep
    done
    echo

    read "rm?Do you want to remove those packages? [y/n]: "
    case $rm in
        [YyJj]|"" ) pip uninstall $freeze -y;;
        [Nn] ) return 0;;
        * ) echo "Please answer yes or no.";;
    esac
}

gotest() {
    result="$(go test -v -cover $@)"
    exit_code=$?
    echo "$result" | sed ''/PASS/s//$(printf "\033[32mPASS\033[0m")/'' | sed ''/FAIL/s//$(printf "\033[31mFAIL\033[0m")/'' | sed ''/RUN/s//$(printf "\033[34mRUN\033[0m")/''
    return "$exit_code"
}

alias got='gotest'

hgrep() {
    history | grep -E "$1"
}
