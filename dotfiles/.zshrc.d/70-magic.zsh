#
# ~/.zshrc.d/70-magic.zsh
# {{@@ env['dotdrop_warning'] @@}}
#


# Magic
set_abbrevations() {
    typeset -Ag abbreviations
    abbreviations=(
      "Le"    "| less"
      "Eg"    "| egrep"
      "Ta"    "| tail"
      "Tl"    "tail -F"
      "So"    "| sort"
      "Cm"    "git commit -am \"__CURSOR__\""
      "Cml"   "${last_commit%?}__CURSOR__\""
      "Pu"    "${push_command} __CURSOR__"
      "Re"    "grep -rniC 0 \"__CURSOR__\" ./"
    )
}

get_last_commit_cmd() {
    last_commit=$(fc -nlr 1 -1 | egrep -m 1 "^git commit")
    if ! [ -n "$last_commit" ]; then
        last_commit='git commit -am ""'
    fi
}

get_git_push_cmd() {
    if [ -d .git ] || git rev-parse --git-dir > /dev/null 2>&1; then
        if ! git_branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null); then
            git_branch="master"
        fi
        push_command="git push origin $git_branch"
    else
        push_command='Pu '
    fi
}

magic-abbrev-expand() {
    get_last_commit_cmd
    get_git_push_cmd
    set_abbrevations
    local MATCH
    LBUFFER=${LBUFFER%%(#m)[_a-zA-Z0-9]#}
    command=${abbreviations[$MATCH]}
    LBUFFER+=${command:-$MATCH}

    if [[ "${command}" =~ "__CURSOR__" ]]
    then
        RBUFFER=${LBUFFER[(ws:__CURSOR__:)2]}
        LBUFFER=${LBUFFER[(ws:__CURSOR__:)1]}
    else
        zle self-insert
    fi
}

no-magic-abbrev-expand() {
    LBUFFER+=' '
}

zle -N magic-abbrev-expand
zle -N no-magic-abbrev-expand
bindkey " " magic-abbrev-expand
bindkey "^x " no-magic-abbrev-expand
bindkey -M isearch " " self-insert
