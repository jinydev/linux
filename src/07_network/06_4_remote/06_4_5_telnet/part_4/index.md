---
layout: home
title: "설정"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 설정

## 설정
두개의 패키지가 모두 설치되어 있다면 설정을 합니다.

* `xinetd` 설정 파일에 `telnet`이 동작하도록 설정

vi /etc/xinetd.conf 에 다음 내용을 추가 합니다.
```
# Simple configuration file for xinetd
#
# Some defaults, and include /etc/xinetd.d/

defaults
{

# Please note that you need a log_type line to be able to use log_on_success
# and log_on_failure. The default is the following :
# log_type = SYSLOG daemon info

}

service telnet
{
    disable = ni
    flags = REUSE
    socket_type = stream
    wait = no
    user = root
    server = /usr/sbin/in.telnetd
    log_on_failure += USERID
}

includedir /etc/xinetd.d
```

* xinetd 다시 실행
서비스 명령을 통하여 xinetd를 시작 합니다. 

```
hojin@hojin3:~$ sudo service xinetd start

```


---

[⬅️ 이전](../)
