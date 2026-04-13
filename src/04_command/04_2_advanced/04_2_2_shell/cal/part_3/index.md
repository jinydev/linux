---
layout: home
title: "한글 달력 설정"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 한글 달력 설정

## 한글 달력 설정

### 로케일 확인

기본 설정값은 영문 달력입니다. 로케일을 변경하여 한글 달력을 출력할 수 있습니다.

`locale` 명령을 통해 현재 설정을 확인합니다.

```console
hojin@DESKTOP-11LMH3B:~$ locale
LANG=C.UTF-8
LANGUAGE=
LC_CTYPE="C.UTF-8"
LC_NUMERIC="C.UTF-8"
LC_TIME="C.UTF-8"
LC_COLLATE="C.UTF-8"
LC_MONETARY="C.UTF-8"
LC_MESSAGES="C.UTF-8"
LC_PAPER="C.UTF-8"
LC_NAME="C.UTF-8"
LC_ADDRESS="C.UTF-8"
LC_TELEPHONE="C.UTF-8"
LC_MEASUREMENT="C.UTF-8"
LC_IDENTIFICATION="C.UTF-8"
LC_ALL=
```

현재 `LANG=C.UTF-8`로 설정되어 있습니다.

### 한글 로케일 설정

한글 달력을 보려면 로케일을 한국어로 변경해야 합니다.

```console
# 임시로 한글 로케일 설정
hojin@DESKTOP-11LMH3B:~$ export LANG=ko_KR.UTF-8
hojin@DESKTOP-11LMH3B:~$ cal
      5월 2020
일 월 화 수 목 금 토
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
```

### 영구 설정

한글 달력을 기본값으로 설정하려면 `~/.bashrc` 파일에 다음 내용을 추가합니다.

```bash
# ~/.bashrc 파일에 추가
export LANG=ko_KR.UTF-8
export LC_TIME=ko_KR.UTF-8
```

설정 후 터미널을 재시작하거나 다음 명령어를 실행합니다.

```console
hojin@DESKTOP-11LMH3B:~$ source ~/.bashrc
```


---

[⬅️ 이전](../)
