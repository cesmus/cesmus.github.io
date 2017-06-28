---
title: systemd: journalctl
slug: journalctl
date: 2017-06-26 10:38
updated: 2017-06-27 20:38
category: linux
tags: linux, systemd, journalctl
---

One of the greatest features of `systemd` is its system logging, the journal.

## The Journal

The journal, according to the developers, is a logging scheme that provides structured, indexed and reliable logging on systemd systems, while providing a certain degree of compatibility with classic syslog implementations.

In more detail, the journal is a component of systemd, that captures Syslog messages, Kernel log messages, initial RAM disk and early boot messages as well as messages written to STDOUT/STDERR of all services, indexes them and stores them in binary files called _journals_.

The journal is implemented with the `journald` daemon and `journalctl` is the tool to query the journal.

## journalctl

`journalctl` is used to query the contents of the `systemd` journal.

All users are granted access to their private per-user journals. However, by default, only root and users who are members of a few special groups are granted access to the system journal and the journals of other users. Members of the groups `systemd-journal`, `adm`, and `wheel` can read all journal files.

The output is paged through `less` by default, and long lines are "truncated" to screen width. The hidden part can be viewed by using the left-arrow and right-arrow keys.

Usage
```bash
journalctl [OPTIONS...] [MATCHES...]
```

Below some common operations using `journalctl` (Not all these commands are available to non-root users but since I belong to the `wheel` group they work just fine):

- Display all collected logs in local time:
```bash hl_lines="1"
$ journalctl
-- Logs begin at Fri 2016-05-06 23:00:44 -05, end at Tue 2017-06-27 12:14:11 -05. --
May 06 23:00:44 fedora systemd-journal[200]: Runtime journal is using 8.0M (max allowed 292.3M, trying to leave 438.5M free of 2.8G available → current limit 292.3M).nt limit 292.3M).
May 06 23:00:44 fedora systemd-journal[200]: Runtime journal is using 8.0M (max allowed 292.3M, trying to leave 438.5M free of 2.8G available → current limit 292.3M).nt limit 292.3M).
May 06 23:00:44 fedora kernel: microcode: CPU0 microcode updated early to revision 0x1b, date = 2014-05-29
May 06 23:00:44 fedora kernel: Initializing cgroup subsys cpuset
May 06 23:00:44 fedora kernel: Initializing cgroup subsys cpu
May 06 23:00:44 fedora kernel: Initializing cgroup subsys cpuacct
May 06 23:00:44 fedora kernel: Linux version 4.2.3-300.fc23.x86_64 (mockbuild@bkernel02.phx2.fedoraproject.org) (gcc version 5.1.1 20150618 (Red Hat 5.1.1-4) (GCC) ) #1 SMP Mon Oct 5 15:42:54 UTC 2015
May 06 23:00:44 fedora kernel: Command line: BOOT_IMAGE=/vmlinuz-4.2.3-300.fc23.x86_64 root=/dev/sda4 ro rhgb quiet LANG=en_US.UTF-8
...
```

- Display all collected logs in UTC time and truncate output (--utc, --no-full):
```bash hl_lines="1"
$ journalctl --utc --no-full
-- Logs begin at Fri 2016-05-06 04:00:44 GMT, end at Tue 2017-06-27 17:39:12 GMT. --
May 07 04:00:44 fedora systemd-journal[200]: Runtime journal is using 8.0M (max allowed 292.3M, trying to leave 438.5M free of 2.8G availa...t 292.3M).
May 07 04:00:44 fedora systemd-journal[200]: Runtime journal is using 8.0M (max allowed 292.3M, trying to leave 438.5M free of 2.8G availa...t 292.3M).
May 07 04:00:44 fedora kernel: microcode: CPU0 microcode updated early to revision 0x1b, date = 2014-05-29
May 07 04:00:44 fedora kernel: Initializing cgroup subsys cpuset
May 07 04:00:44 fedora kernel: Initializing cgroup subsys cpu
May 07 04:00:44 fedora kernel: Initializing cgroup subsys cpuacct
May 07 04:00:44 fedora kernel: Linux version 4.2.3-300.fc23.x86_64 (mockbuild@bkernel02.phx2.fedoraproject.org) (gcc version 5.1.1 201506... UTC 2015
May 07 04:00:44 fedora kernel: Command line: BOOT_IMAGE=/vmlinuz-4.2.3-300.fc23.x86_64 root=/dev/sda4 ro rhgb quiet LANG=en_US.UTF-8
...
```

- Follow live view of logs (-f/--follow):
```bash
journalctl -f
```

- Display logs of current boot (-b/--boot=):
```bash
journalctl -b
```

- Display kernel logs from previous boot (-k/--dmesg, -b/--boot= [ID][±offset]):
```bash
journalctl -k -b -1
```

- List system boots:
```bash hl_lines="1"
$ journalctl --list-boots
-10 38ba890bfa33438dafaf6ef973632f24 Sat 2017-02-18 14:06:23 -05—Mon 2017-02-20 08:59:48 -05
 -9 bee7acaabf8c4bae84f4e722f7a1cdee Mon 2017-02-20 09:55:05 -05—Tue 2017-02-21 17:02:47 -05
 -8 79e75e53d5064de39cc8daa5d9b498b0 Tue 2017-02-21 17:03:04 -05—Mon 2017-03-13 20:15:35 -05
 -7 7f4b18dd2d1c41818403ebd4127ebdab Mon 2017-03-13 20:15:35 -05—Sun 2017-03-19 14:04:07 -05
 -6 4fa6854475654115b6a42a6152a28ed0 Sun 2017-03-19 14:04:16 -05—Sun 2017-03-19 14:09:04 -05
 -5 347eab3e0a8b466daf1fd0c2dd8f530c Sun 2017-03-19 14:08:58 -05—Mon 2017-04-03 08:25:33 -05
 -4 c5fdea929ed64ae0b780a7c69e3dce23 Mon 2017-04-03 08:25:47 -05—Sun 2017-04-09 19:56:33 -05
 -3 3583690c404b41318a6a2b9a06c17b74 Sun 2017-04-09 20:10:48 -05—Mon 2017-05-08 01:24:10 -05
 -2 72266bc3243d41999e63926fb679b7cb Mon 2017-05-08 07:50:10 -05—Fri 2017-05-26 07:45:22 -05
 -1 830be6c653a54e50ac93f45b338cf213 Fri 2017-05-26 07:44:54 -05—Thu 2017-06-01 23:43:42 -05
  0 29fe47d8fdf6485ab76d2eb73416787a Thu 2017-06-01 23:43:55 -05—Tue 2017-06-27 15:33:56 -05
```

- Display logs filtered by priority _error_ or higher (-p/--priority=):
```bash
journalctl -p err
```

- Display all logs from the day before (-S/--since=):
```bash
journalctl --since=yesterday
```

- Reverse order, latest entries are shown first (-S/--since=, -r/--reverse):
```bash
journalctl -S today -r
```

- Display entries from the last twenty minutes (-S/--since=):
```bash
journalctl --since "20 min ago"
```

- Display entries between dates (-S/--since=, -U/--until=):
```bash
journalctl -S "2014-11-16 23:59:59" -U "2014-11-23 23:59:59"
```

- Display entries between hours (-u/--init=, -S/--since=, -U/--until=):
```bash
journalctl -u sshd --since=00:00 -U 9:30
```

- Display logs generated by D-Bus executable
```bash
journalctl /usr/bin/dbus-daemon
```

- Display logs generated by a disk
```bash
journalctl /dev/sda
```

- Display a live log from httpd service (-f/--follow, -u/--unit=):
```bash
journalctl -f -u httpd
```

- Output logs with metadata:
```bash hl_lines="1"
$ journalctl -o verbose
-- Logs begin at Fri 2016-05-06 23:00:44 -05, end at Tue 2017-06-27 15:01:01 -05. --
Fri 2016-05-06 23:00:44.145769 -05 [s=980d50e2f0c8457683aded28f925ac07;i=1;b=bdac7df248b14ba0aab46c6e3e3c84f1;m=19c55f;t=532389e9c2c69;x=ee8ab73f8410
    PRIORITY=6
    _TRANSPORT=driver
    MESSAGE=Runtime journal is using 8.0M (max allowed 292.3M, trying to leave 438.5M free of 2.8G available → current limit 292.3M).
    MESSAGE_ID=ec387f577b844b8fa948f33cad9a75e6
    _PID=200
    _UID=0
    _GID=0
    _COMM=systemd-journal
    _EXE=/usr/lib/systemd/systemd-journald
    _CMDLINE=/usr/lib/systemd/systemd-journald
    _CAP_EFFECTIVE=25402800cf
    _SYSTEMD_CGROUP=/system.slice/systemd-journald.service
    _SYSTEMD_UNIT=systemd-journald.service
    _SYSTEMD_SLICE=system.slice
    _BOOT_ID=bdac7df248b14ba0aab46c6e3e3c84f1
    _MACHINE_ID=2682a64ca8a14ec5512b5c07536950ae
    ...
```

- Output as a binary stream suitable for backups and network transfers:
```bash hl_lines="1"
$ journalctl -o export
__CURSOR=s=980d50e2f0c8457683aded28f925ac07;i=1;b=bdac7df248b14ba0aab46c6e3e3c84f1;m=19c55f;t=532389e9c2c69;x=ee8ab73f8410598b
__REALTIME_TIMESTAMP=1462593644145769
__MONOTONIC_TIMESTAMP=1688927
_BOOT_ID=bdac7df248b14ba0aab46c6e3e3c84f1
PRIORITY=6
_TRANSPORT=driver
MESSAGE=Runtime journal is using 8.0M (max allowed 292.3M, trying to leave 438.5M free of 2.8G available → current limit 292.3M).
MESSAGE_ID=ec387f577b844b8fa948f33cad9a75e6
_PID=200
_UID=0
_GID=0
_COMM=systemd-journal
_EXE=/usr/lib/systemd/systemd-journald
_CMDLINE=/usr/lib/systemd/systemd-journald
_CAP_EFFECTIVE=25402800cf
_SYSTEMD_CGROUP=/system.slice/systemd-journald.service
_SYSTEMD_UNIT=systemd-journald.service
_SYSTEMD_SLICE=system.slice
_MACHINE_ID=2682a64ca8a14ec5512b5c07536950ae
...
```

- Output as JSON data suitable for web:
```bash
journalctl -o json
```

- Display entries that matches the expression:
```bash
journalctl _SYSTEMD_UNIT=firewalld.service
```

- Find out possible values for field:
```bash hl_lines="1"
$ journalctl _SELINUX_CONTEXT=<TAB><TAB>
kernel
system_u:system_r:alsa_t:s0
system_u:system_r:auditctl_t:s0
system_u:system_r:auditd_t:s0
system_u:system_r:crond_t:s0-s0:c0.c1023
system_u:system_r:dhcpc_t:s0
system_u:system_r:firewalld_t:s0
system_u:system_r:policykit_t:s0
system_u:system_r:rpm_t:s0
...
```

- Display logs from selinux label PolicyKit:
```bash
journalctl _SELINUX_CONTEXT=system_u:system_r:policykit_t:s0
```

- Current disk usage of the journal:
```bash hl_lines="1"
$ journalctl --disk-usage
Archived and active journals take up 2.8G on disk.
```

- Verify internal consistency of journal files:
```bash
journalctl --verify
```

For further information about journalctl, read [Red Hat Documentation: Using the Journal](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/s1-Using_the_Journal.html), [0pointer.de post: journalctl](http://0pointer.de/blog/projects/journalctl.html), [man page: journalctl](https://www.freedesktop.org/software/systemd/man/journalctl.html)
