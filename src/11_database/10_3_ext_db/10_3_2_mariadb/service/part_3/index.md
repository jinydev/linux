---
layout: home
title: "상태확인"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 상태확인

## 상태확인
---
마리아DB 데몬의 실행 상태를 확인합니다.

```
hojin@hojin:~$ sudo systemstl status mariadb
sudo: systemstl: command not found
hojin@hojin:~$ sudo systemctl status mariadb
● mariadb.service - MariaDB 10.5.8 database server
     Loaded: loaded (/lib/systemd/system/mariadb.service; enabled; vendor preset: enabled)
    Drop-In: /etc/systemd/system/mariadb.service.d
             └─migrated-from-my.cnf-settings.conf
     Active: active (running) since Fri 2021-01-01 15:32:16 KST; 16min ago
       Docs: man:mariadbd(8)
             https://mariadb.com/kb/en/library/systemd/
   Main PID: 4815 (mariadbd)
     Status: "Taking your SQL requests now..."
      Tasks: 10 (limit: 1074)
     Memory: 68.0M
     CGroup: /system.slice/mariadb.service
             └─4815 /usr/sbin/mariadbd
```

<br>


---

[⬅️ 이전](../)
