#!/usr/bin/bash
# This file is managed by dotdrop, only edit it in your dotdrop files!


SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"


INPUT="${DIR}/radio.csv"
OLDIFS=$IFS
IFS=';'
[ ! -f "$INPUT" ] && { echo "$INPUT file not found"; exit 99; }
declare -A table=()
table_index=()
while read -r title url; do
    table["$title"]="$url"
    table_index+=("$title")
done < "$INPUT"
IFS=$OLDIFS

select station in "${table_index[@]}"; do
    break
done

if [[ "${table[$station]}" == *.pls ]] || [[ "${table[$station]}" == *.m3u ]]; then
    mplayer -cache 1024 -vo none -playlist "${table[$station]}"
else
    mplayer -cache 1024 -vo none "${table[$station]}"
fi
