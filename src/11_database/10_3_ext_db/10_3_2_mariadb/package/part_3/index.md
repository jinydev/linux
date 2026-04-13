---
layout: home
title: "패키지 설치"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 패키지 설치

## 패키지 설치
---
최신 버젼의 Mariadb를 설치할 수 있도록 목록을 갱신하였습니다. 
다음과 같이 명령을 입력하여 mariadb를 설치합니다.

```
$ sudo apt install mariadb-server -y
```

설치가 완료 되었면 자동으로 MariaDB가 실행됩니다. 다음과 같이 프로세스를 확인해 봅니다.

```
hojin@hojin:~$ ps -ef | grep mysql
mysql       4815       1  0 15:32 ?        00:00:00 /usr/sbin/mariadbd
hojin       5812    2266  0 15:34 pts/0    00:00:00 grep --color=auto mysql
```

<br>


---

[⬅️ 이전](../)
