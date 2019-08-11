#!/usr/bin/env zsh
#
# {{@@ env['dotdrop_warning'] @@}}
#
[[ -z $PER_DIRECTORY_HISTORY_DEFAULT_GLOBAL ]] && PER_DIRECTORY_HISTORY_DEFAULT_GLOBAL=false


if [[ $PER_DIRECTORY_HISTORY_DEFAULT_GLOBAL == true ]]; then
  # start in global mode
  _per_directory_history_is_global=false
  _per-directory-history-set-global-history
fi
