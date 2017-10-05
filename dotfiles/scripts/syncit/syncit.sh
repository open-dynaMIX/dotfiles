#!/bin/bash
#
## syncit
## Version 0.1
##
## 2013
## 2014
## Fabio Rämi


echo "
 ____ ____ ____ ____ _________ ____ ____
||S |||Y |||N |||C |||   ☠   |||I |||T ||
||__|||__|||__|||__|||_______|||__|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|

"

## variables
scriptlocation=$(readlink -f $0)
scriptdir=$(dirname $scriptlocation)
rsynccmd="rsync -avxe ssh --delete --delete-excluded --include-from=/home/{{@@ env['USER'] @@}}/scripts/syncit/include --exclude-from=/home/{{@@ env['USER'] @@}}/scripts/syncit/exclude"
serverdir="{{@@ env['USER'] @@}}@{{@@ env['backup_host'] @@}}:/var/disk/{{@@ env['USER'] @@}}/backup_{{@@ env['model'] @@}}/"
localdir="/home/{{@@ env['USER'] @@}}/"

rm -f "$scriptdir"/.pyoutput

# close file descriptors and cleanup temp files
function cleanup {
        if [ "$zenity" == true  ]; then
          exec 3>&-
          exec 4>&-
          rm -f $scriptdir/.pyoutput
        fi
        rm -f /tmp/syncitfifo.$$
}

function usage {
        echo -e "usage: $0 [--zenity|--shut|-h]"
}

# handle missing slash at the end of localdir
if ! echo "$localdir" | grep -E -q "/$"; then
  localdir="$localdir/"
fi

for var in "$@"
do
    if [ $var == '-h' ]; then
      usage
      exit 0
    elif [ $var == '--zenity' ]; then
      zenity=true
    elif [ $var == '--shut' ]; then
      shut=true
    fi
done

# redirect stdout & stderr to logfile if there is not terminal
if ! [[ -t 1 ]] || [ "$zenity" == true ]; then
  zenity=true
  exec 1>>$scriptdir/syncit.log 2>&1
else
  zenity=false
fi

# Check if all needed commands are available.
# Taken from http://wiki.bash-hackers.org/scripting/style
if [ "$zenity" == true  ]; then
  my_needed_commands="zenity gksudo rsync"
else
  my_needed_commands="rsync"
fi
missing_counter=0
for needed_command in $my_needed_commands; do
  if ! hash "$needed_command" >/dev/null 2>&1; then
    printf "Command not found: %s\n" "$needed_command" >&2
    ((missing_counter++))
  fi
done
if ((missing_counter > 0)); then
  printf "$(date) - Minimum %d commands are missing, aborting.\n" "$missing_counter" >&2
  exit 1
fi

# fetch the sudo password
if ! [[ -t 1 ]]; then
  while ! sudo -kSp '' [ 1 ] <<<"${sudopassword}" 2>/dev/null; do
    sudopassword="$( gksudo --print-pass --message 'Provide permission for the process to shut down your computer.
Type your password, or press Cancel.' -- : 2>/dev/null )"
    # Check for null entry or cancellation.
    if [[ ${?} != 0 || -z ${sudopassword} ]]
    then
        exit 1
    fi
  done
else
  if [ "$shut" == true ]; then
    echo -n "Provide permission for the process to shut down your computer.
Password:"
    read -s sudopassword; echo
  fi
fi

if [ "$zenity" == true  ]; then
  # prepare the notifications
  exec 4> >(zenity --notification --listen)
  exec 3> >($scriptdir/trayicon.py)
  echo "icon:$scriptdir/icon.png" >&4
  echo "icon $scriptdir/icon.png" >&3

  # create the file for python to write in
  rm -f $scriptdir/.pyoutput
  touch $scriptdir/.pyoutput
fi

# the rsync part
echo "$(date) - Sync is in progress..."
if [ "$zenity" == true  ]; then
  echo "tooltip sync is in progress" >&3
  echo "message:Sync is in progress..." >&4
fi

# Using fifo to get the PID of rsync.
FIFONAME=/tmp/syncitfifo.$$
rm -f $FIFONAME
mkfifo $FIFONAME
# The rsync-command
$rsynccmd $localdir $serverdir > "$FIFONAME" &
RSYNC_PID=$!

# execute rsync
while read -r; do
  LINE="$REPLY"
  if [ -e "$localdir$LINE" ] && [[ -t 1 ]]; then
    if [ "$zenity" == true  ]; then
      echo "tooltip Syncing: $LINE" >&3
    fi
  fi
  echo -e "$LINE"
  # check if user wants to cancel
  if [ -f "$scriptdir/.pyoutput" ]; then
    if cat "$scriptdir/.pyoutput" | egrep -q "quit"; then
      kill $RSYNC_PID
      echo "$(date) - Cancel"
      if [ "$zenity" == true  ]; then
        echo "message:Cancel" >&4
      fi
      sleep 2
      cleanup
      exit 1
    fi
  fi
done <"$FIFONAME"

# fetch and react on the rsync exit status
wait $RSYNC_PID
rsync_stat=$?

case $rsync_stat in
  0)
    echo "$(date) - Syncing was successful."
    if [ "$zenity" == true  ]; then
      echo "message:Syncing was successfull" >&4
    fi
  ;;
  *)
    echo "$(date) - Error while syncing! Exit $rsync_stat"
    if [ "$zenity" == true  ]; then
      echo "message:Error while syncing! Exit $rsync_stat" >&4
    fi
    sleep 1
    cleanup
    exit 1
  ;;
esac

# check if user wants to shutdown the computer
if [ "$zenity" == true  ]; then
  pyshut=($( cat $scriptdir/.pyoutput ))
fi
if [ -n "$pyshut" ]; then
  count=$(echo -e "$pyshut" | wc -l)
  ((count--))
  for item in "$pyshut"; do
    case ${pyshut[$count]} in
      noshut)
        exitnow="yes"
        break
      ;;
      turnoff)
        exitnow="no"
        break
      ;;
      *)
        exitnow="yes"
    esac
    ((count--))
  done
elif [ -n "$shut" ]; then
  :
else
  exitnow="yes"
fi
if [ "$exitnow" = "yes" ]; then
  cleanup
  exit 0
fi

# execute shutdown as root
echo "$(date) - Shutting down in 3 seconds."
if [ "$zenity" == true  ]; then
  echo "tooltip Shutting down in 3 seconds" >&3
  echo "message:Shutting down in 3 seconds" >&4
fi
sleep 3
cleanup
echo 'echo -e "$sudopassword\n" | sudo -S -s -- shutdown -h now'
exit 0
