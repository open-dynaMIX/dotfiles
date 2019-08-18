#!/usr/bin/env bash
# {{@@ env['dotdrop_warning'] @@}}
#

SSH_AUTH_SOCK="/run/user/$(id -u)/keyring/ssh"
export SSH_AUTH_SOCK

error () {
    echo "Backup host not available." 1>&2
    exit 1
}


IP="{{@@ env['backup_host'] @@}}"
MAC="{{@@ env['backup_host_mac'] @@}}"

ping -c 1 "$IP" > /dev/null 2>&1 || error
fetched_mac="$(arp -n | grep "$IP" | awk '{print $3}')"
if [[ "$fetched_mac" == "" ]] || [[ "$fetched_mac" != "$MAC" ]]; then
    error
fi

"${HOME}"/scripts/timemachine/rsync-time-backup/rsync_tmbackup.sh "${HOME}"/ {{@@ env['backup_user'] @@}}@"$IP":/home/{{@@ env['backup_user'] @@}}/backups/{{@@ env['model'] @@}}/ "${HOME}"/scripts/timemachine/exclude
