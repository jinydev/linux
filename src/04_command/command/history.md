---
layout: home
---

# 명령어 히스토리
커멘드 라인 기반의 리눅스 명령은매번 명령어를 입력하기 때문에 불편 합니다.

리눅스는 이전 입력한 명령들을 쉽게 찾아 재실행 할 수 있도록 명력 기록을 가지고 있습니다.

## 화살표
화살표를 이용하여 이전명령어를 쉽게 찾아 볼 수 있습니다.

## 명령 기록파일
지금까지 사용한 명령어는 해당 사용자의 기본 디렉토리 내에 `.bash_history`에 저장되어 있습니다.

```
hojin@hojin3:~$ ls -all
total 32
drwxr-x--- 2 hojin hojin 4096 Mar 22 14:03 .
drwxr-xr-x 3 root  root  4096 Mar  4 18:50 ..
-rw------- 1 hojin hojin  513 Mar 22 13:56 .bash_history
-rw-r--r-- 1 hojin hojin  220 Mar  4 18:50 .bash_logout
-rw-r--r-- 1 hojin hojin 3771 Mar  4 18:50 .bashrc
-rw------- 1 hojin hojin   20 Mar 21 00:50 .lesshst
-rw-r--r-- 1 hojin hojin    0 Mar 22 13:49 .motd_shown
-rw-r--r-- 1 hojin hojin  807 Mar  4 18:50 .profile
-rw-r--r-- 1 hojin hojin    0 Mar 20 17:09 .sudo_as_admin_successful
-rw------- 1 hojin hojin  932 Mar 22 14:03 .viminfo
```

> 기업용 시스템에서는 해당 파일을 실시간으로 중앙통제장치로 전송하여 보관함으로써 불순한 의도의 접근을 감시하는 용도로도 사용됨.