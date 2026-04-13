---
layout: home
title: "고급 사용법"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 고급 사용법

## 고급 사용법

### Unix 타임스탬프

Unix 타임스탬프(1970년 1월 1일부터의 초 단위)를 출력합니다.

```console
hojin@DESKTOP-11LMH3B:~$ date +%s
1590049291
```

### 타임스탬프에서 날짜 변환

Unix 타임스탬프를 읽기 쉬운 날짜 형식으로 변환할 수 있습니다.

```console
hojin@DESKTOP-11LMH3B:~$ date -d @1590049291
Thu May 21 15:41:31 KST 2020
```

### 특정 날짜 출력

특정 날짜를 지정하여 해당 날짜의 정보를 출력할 수 있습니다.

```console
# 내일 날짜
hojin@DESKTOP-11LMH3B:~$ date -d "tomorrow"
Fri May 22 15:41:31 KST 2020

# 어제 날짜
hojin@DESKTOP-11LMH3B:~$ date -d "yesterday"
Wed May 20 15:41:31 KST 2020

# 특정 날짜
hojin@DESKTOP-11LMH3B:~$ date -d "2020-05-21"
Thu May 21 00:00:00 KST 2020

# 상대적 날짜
hojin@DESKTOP-11LMH3B:~$ date -d "1 week ago"
Thu May 14 15:41:31 KST 2020

hojin@DESKTOP-11LMH3B:~$ date -d "2 months ago"
Thu Mar 21 15:41:31 KST 2020
```

### 시간대 설정

다른 시간대의 시간을 확인할 수 있습니다.

```console
# UTC 시간
hojin@DESKTOP-11LMH3B:~$ date -u
Thu May 21 06:41:31 UTC 2020

# 특정 시간대
hojin@DESKTOP-11LMH3B:~$ TZ='America/New_York' date
Thu May 21 02:41:31 EDT 2020

hojin@DESKTOP-11LMH3B:~$ TZ='Europe/London' date
Thu May 21 07:41:31 BST 2020
```


---

[⬅️ 이전](../)
