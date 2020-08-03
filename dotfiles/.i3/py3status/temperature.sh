#!/usr/bin/bash
# {{@@ env['dotdrop_warning'] @@}}

hergiswil=$(curl -q "https://www.wiewarm.ch/api/bad/Schwimmbad_Hergiswil_?cacheScrew=592518" 2>/dev/null | jq -r '.becken | ."Vierwaldstättersee".temp')
reuss=$(curl -q https://www.hydrodaten.admin.ch/graphs/2152/temperature_2152.csv 2>/dev/null | tail -n 1 | cut -d "," -f 2)

echo "Hergiswil: ${hergiswil}°C"
echo "Reuss: ${reuss}°C"

notify-send -t 5000 -i plugin-water "$(echo -e "Hergiswil: ${hergiswil}°C\nReuss: ${reuss}°C")"
