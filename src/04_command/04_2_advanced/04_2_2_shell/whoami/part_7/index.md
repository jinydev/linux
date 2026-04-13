---
layout: home
title: "문제 해결"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 문제 해결

## 문제 해결

### 명령어가 인식되지 않는 경우

일부 시스템에서는 `whoami` 명령어가 설치되지 않았을 수 있습니다.

```console
# 명령어 존재 확인
hojin@DESKTOP-11LMH3B:~$ which whoami
/usr/bin/whoami

# 대안 명령어 사용
hojin@DESKTOP-11LMH3B:~$ echo $USER
hojin

# 또는
hojin@DESKTOP-11LMH3B:~$ logname
hojin
```

### 권한 문제

`whoami` 명령어는 실행 권한이 필요하지 않지만, 일부 환경에서는 제한될 수 있습니다.

```console
# 실행 권한 확인
hojin@DESKTOP-11LMH3B:~$ ls -l $(which whoami)
-rwxr-xr-x 1 root root 14280 Apr 29 16:52 /usr/bin/whoami
```


---

[⬅️ 이전](../)
