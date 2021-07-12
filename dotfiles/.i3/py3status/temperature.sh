#!/usr/bin/bash
# {{@@ header() @@}}

function get_temp {
    for (( i=0; i<5; ++i)); do
        resp=$(curl -q "$1" -H "$2" 2>/dev/null) && break
    done
    echo "$resp"
}

function get_temp_hergi {
    resp=$(get_temp "https://www.wiewarm.ch/api/bad/Schwimmbad_Hergiswil_?cacheScrew=592518")
    echo "$resp" | jq -r '.becken | ."Vierwaldstättersee".temp'
}

function get_temp_reuss {
    resp=$(get_temp "https://www.hydrodaten.admin.ch/lhg/az/dwh/csv/BAFU_2152_Wassertemperatur.csv" "Range: bytes=-32")
    echo "$resp" | cut -d "," -f 2
}

function notification {
    hergiswil="$(get_temp_hergi)"
    reuss="$(get_temp_reuss)"
    echo "Hergiswil: ${hergiswil}°C"
    echo "Reuss: ${reuss}°C"
    notify-send -t 5000 -i plugin-water "$(echo -e "Hergiswil: ${hergiswil}°C\nReuss: ${reuss}°C")"
}

if [ "${1-normal}" == "--py3status" ]; then
    get_temp_reuss
else
    notification
fi
