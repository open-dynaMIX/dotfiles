#!/usr/bin/bash
# {{@@ env['dotdrop_warning'] @@}}

cd ${HOME}/.screenlayout/ || exit 1

d=$(for entry in ./*
do
  echo "$entry"
done | rofi -dmenu)

$d
