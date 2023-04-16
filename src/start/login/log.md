---
layout: home
---

# 로그인 기록
리눅스는 접속을 하는 모든 사용자의 로그인을 기록합니다.

## 로그인 기록
리눅스에서 로그인 기록(login record)은 시스템에 로그인한 사용자들의 정보와 로그인 시도에 대한 정보를 기록하는 것을 말합니다.

로그인 기록은 `시스템 보안`을 강화하는 데 중요한 역할을 합니다. 이 로그는 보안 관리자가 시스템에 접근한 사용자 및 시간을 추적할 수 있으며, 필요한 경우 불법적인 접근을 추적하고 예방할 수 있습니다.

로그인 기록은 시스템 로그 파일에 기록됩니다. 로그 파일은 `/var/log` 디렉토리에 위치하며, 로그인 기록은 `/var/log/auth.log` 또는 `/var/log/secure` 파일에 저장됩니다.

로그인 기록에는 다음과 같은 정보들이 포함됩니다.

* 사용자 이름과 IP 주소
* 로그인 시도 시간
* 로그인 성공 여부
* 실패한 로그인 시도 횟수
* 실패한 로그인 시도 시간

로그인 기록을 정기적으로 `모니터`링하고 검토하여, `보안 관련 이슈`를 `감지`하고 처리할 수 있습니다.

## 접속기록
리눅스는 모든 로그인 기록을 `/var/log/wtmp`에 기록합니다.

```bash
hojin@hojin-550XDA:~$ ls /var/log/wtmp
/var/log/wtmp
```
`last`의 명령은 `/var/log/wtmp`파일의 내용을 쉽게 할인 할 수 있는 명령을 제공합니다.

### last
`last` 명령어로 최근 접속 기록 및 최근 재부팅 기록을 볼 수 있다.

```
hojin@hojin-550XDA:~$ last
hojin    pts/0        172.30.1.76      Wed Mar 29 13:07   still logged in
hojin    pts/0        172.30.1.67      Fri Mar 24 15:09 - 03:21  (12:11)
hojin    pts/0        172.30.1.91      Wed Mar 22 14:28 - 14:42  (00:14)
hojin    pts/0        172.30.1.91      Wed Mar 22 14:26 - 14:27  (00:01)
hojin    pts/1        172.30.1.25      Mon Mar 13 14:12 - 20:25  (06:13)
hojin    tty2         tty2             Tue Mar  7 17:52   still logged in
reboot   system boot  5.19.0-35-generi Tue Mar  7 17:52   still running

wtmp begins Sat Mar  4 17:53:01 2023
```

### 일부 특정 사용자 확인
`last`명령 뒤에 계정을 붙여 입력합니다.
```
hojin@hojin-550XDA:~$ last hojin
hojin    pts/0        172.30.1.76      Wed Mar 29 13:07   still logged in
hojin    pts/0        172.30.1.67      Fri Mar 24 15:09 - 03:21  (12:11)
hojin    pts/1        172.30.1.25      Mon Mar 13 14:12 - 20:25  (06:13)
hojin    tty2         tty2             Tue Mar  7 17:52   still logged in

wtmp begins Sat Mar  4 17:53:01 2023
hojin@hojin-550XDA:~$
```

### 특정시간 이전 접속 확인  
`-t` 옵션으로 일시를 붙이면 그 이전의 접속기록만 표시된다. 인수는 `YYYYMMDDHHMMSS(연월일시분초)` 형식으로 적어야 한다.

```
hojin@hojin-550XDA:~$ last -t 20230329040000
hojin    pts/0        172.30.1.67      Fri Mar 24 15:09 - 03:21  (12:11)
hojin    pts/0        172.30.1.91      Wed Mar 22 14:28 - 14:42  (00:14)
hojin    pts/0        172.30.1.91      Wed Mar 22 14:26 - 14:27  (00:01)

wtmp begins Sat Mar  4 17:53:01 2023
hojin@hojin-550XDA:~$
```

### 지난달 기록 보기
`/var/log/wtmp`는 `logrotate`에 의해 로그 기록값이 순환됩니다.
`logrotate`는 `/etc/logrotate.conf` 설정에 따라 매달 1일의 특정 갯수가 넘는 경우 순환되어 기록되게 설계되어 있습니다. 이런경우 `.1`, `.2`와 같은 확장자를 확인하여 보존된 파일을 확인해야 합니다.

```
last -f /var/log/wtmp.1
```
