---
layout: home
title: "항상 실행하기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 항상 실행하기

## 항상 실행하기
---
MariaDB를 새로이 설치할때 또는 systemctl 명령을 통하여 서버를 실행할 수 있습니다. 하지만, 리눅스 서버가 재부팅되는 경우에는 Mariadb가 자동으로 실행되지 않습니다. 매번 서버를 재부팅할때마다 systemctl 명령을 통하여 MariaDB를 시작해 주어야 합니다.

서버가 실행될때 자동으로 MariaDB가 실행되도록 설정을 할 수 있습니다. enable 명령을 사용합니다.

```
hojin@hojin:~$ sudo systemctl enable mariadb
Synchronizing state of mariadb.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable mariadb
```

반대로 자동 실행을 해제할 경우에는 disable 명령을 사용합니다.

```
hojin@hojin:~$ sudo systemctl disable mariadb
Synchronizing state of mariadb.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install disable mariadb
Removed /etc/systemd/system/multi-user.target.wants/mariadb.service.
```

---

[⬅️ 이전: root 설정하기](../root/) &nbsp;|&nbsp; [🏠 분류 목차](../../../../) &nbsp;|&nbsp; [다음: 테스트 및 접속하기 ➡️](../test/)


---

[⬅️ 이전](../)
