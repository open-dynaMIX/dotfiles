#!/usr/bin/bash
# {{@@ env['dotdrop_warning'] @@}}


# Original script source:
# https://gist.github.com/tomjnixon/1348383/68a1783a111f5eed7b1f8a4a70adb157c9118e1b

# Script to switch all programs to a specific sync. Why this isn't easy, i
# don't know.

# This script takes a single optional argument, the sink name, index, or alias (defined
# below).

# To make this work, you will need to:
#   - Set up the sink_names array below.
#     PulseAudio sink names are usually rather obtuse, and the indices can
#     change, so you can declare short names for sinks in the array below.
#
#     The format is '[alias]=device_name'. The sink names can be found with:
#       $ pacmd list-sinks | grep '^\s*name'
#     , and are the monstrosities between the angle brackets.


if [ -z "$1" ]; then
    (>&2 echo "No argument provided!")
    exit 1
fi


declare -A sink_names=(
    [speakers]="{{@@ audio_device_pulse_internal @@}}"
    [hdmi]="{{@@ audio_device_pulse_hdmi @@}}"
)

sink=${sink_names[$1]:-$1}
profile="$1"


(
    echo set-default-sink "$sink"

    pacmd list-sink-inputs |
        grep -E '^\s*index:' |
        grep -oE '[0-9]+' |
        while read -r input
    do
        echo move-sink-input "$input" "$sink"
    done
) | pacmd > /dev/null

echo "$profile"
