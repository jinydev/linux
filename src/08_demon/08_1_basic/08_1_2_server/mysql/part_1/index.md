---
layout: home
title: "프로세스 확인"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 프로세스 확인

## 프로세스 확인
---
시작여부의 프로세스를 확인해 봅니다.

```console
hojin@DESKTOP-11LMH3B:~$ ps -ef | grep mysql
hojin     5863     8  0 16:15 tty1     00:00:00 grep --color=auto mysql
```

서버를 시작합니다.
``` console
hojin@DESKTOP-11LMH3B:~$ sudo service mysql status
[sudo] password for hojin:
 * MariaDB is stopped.
``` 

```console
hojin@DESKTOP-11LMH3B:~$ sudo service mysql status
 * /usr/bin/mysqladmin  Ver 9.1 Distrib 10.3.22-MariaDB, for debian-linux-gnu on x86_64
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Server version          10.3.22-MariaDB-1ubuntu1
Protocol version        10
Connection              Localhost via UNIX socket
UNIX socket             /var/run/mysqld/mysqld.sock
Uptime:                 15 sec

Threads: 7  Questions: 2  Slow queries: 0  Opens: 17  Flush tables: 1  Open tables: 11  Queries per second avg: 0.133
```

중지하기
```console
hojin@DESKTOP-11LMH3B:~$ sudo service mysql stop
 * Stopping MariaDB database server mysqld                                                                       [ OK ]
```


---

[⬅️ 이전](../)
