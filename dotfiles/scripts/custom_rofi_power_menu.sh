#!/usr/bin/bash
# {{@@ header() @@}}

choices="\
⏾ Suspend
⏻ Shut down
➾ Logout\
"

sel=$(echo "$choices" | rofi -dmenu -p "Power menu")


if [[ "${sel}" == "⏾ Suspend" ]]; then
    systemctl suspend
elif [[ "${sel}" == "⏻ Shut down" ]]; then
    systemctl poweroff
elif [[ "${sel}" == "➾ Logout" ]]; then
    loginctl terminate-session "${XDG_SESSION_ID-}"
fi
