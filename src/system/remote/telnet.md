---
layout: home
---

# 텔렛

## 텔렛이란?
서 버의 네트워크를 통하여 원격으로 접속하는 방식 규약(프로토콜) 입니다.

`xintd`, `telnet` 패키지를 설치합니다.

## xinetd 설치
`xinetd`는 리눅스 네트워크 서비스 데몬으로 `telnet`을 사용하기 위해서는 필수로 설치해야 되는 요소입니다.

```
$ sudo apt-get install xinetd
```

## telnet 설치
`telnetd`는 텔넷 서비스 데몬으로 `telnet`을 서용하기 위한 필수 요소임

```
$sudo apt-get install telnetd
```

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



## 텔넷 클라이언트

### 윈도우 기본 telnet 클라이 언트를 설치한다.
`제어판`에 가서 `프로그램 및 기능`을 선택합니다. 
오른쪽 메뉴에서 `Windows 기능 켜기/끄기`를 선택합니다.
[텔넷 클라이언트]를 부분을 활성화 합니다.



![image-20230322144209427](./img/image-20230322144209427.png)




* 명령 프롬프트(관리자)를 실행(윈도우키+x)

