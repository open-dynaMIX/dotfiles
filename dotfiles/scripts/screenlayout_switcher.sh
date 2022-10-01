#!/usr/bin/bash
# {{@@ header() @@}}

cd ${HOME}/.screenlayout/ || exit 1

d=$(for entry in ./*
do
  echo "$entry"
done | rofi -dmenu -p "Screen layouts")

$d
