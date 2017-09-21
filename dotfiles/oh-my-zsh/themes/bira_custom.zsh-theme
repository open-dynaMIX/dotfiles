# ZSH Theme - Preview: http://gyazo.com/8becc8a7ed5ab54a0262a470555c3eed.png
local return_code="%(?..%{$fg[red]%}%? ↵%{$reset_color%})"

if [[ -z "$SSH_CLIENT" ]]; then
        prompt_host=""
else
        prompt_host=%{$fg_bold[white]%}@%{$reset_color$fg[yellow]%}$(hostname)
fi

if [ $(whoami) != "root" ]; then
    local user_host='%{$terminfo[bold]$fg[green]%}%n%{$reset_color%}'
else
    local user_host='%{$terminfo[bold]$fg[red]%}%n%{$reset_color%}'
fi
local current_dir='%{$terminfo[bold]$fg[blue]%} %~%{$reset_color%}'
local rvm_ruby=''
if which rvm-prompt &> /dev/null; then
  rvm_ruby='%{$fg[red]%}‹$(rvm-prompt i v g)›%{$reset_color%}'
else
  if which rbenv &> /dev/null; then
    rvm_ruby='%{$fg[red]%}‹$(rbenv version | sed -e "s/ (set.*$//")›%{$reset_color%}'
  fi
fi
local git_branch='$(git_prompt_info)%{$reset_color%}'
# local pyenv=''
# if [[ -n $VIRTUAL_ENV ]]; then
#     pyenv='('`basename $VIRTUAL_ENV`') '
# fi
# export VIRTUAL_ENV_DISABLE_PROMPT=1

PROMPT="╭─${user_host}${prompt_host}${current_dir} ${rvm_ruby} ${git_branch}
╰─%B$%b "
RPS1="${return_code}"

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[yellow]%}‹"
ZSH_THEME_GIT_PROMPT_SUFFIX="› %{$reset_color%}"
