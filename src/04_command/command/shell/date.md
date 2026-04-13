---
layout: home
title: "date - 리눅스 날짜 시간 명령어 - 개발자를 위한 리눅스"
description: "date 명령어의 사용법과 옵션을 알아보세요. 현재 날짜 시간 출력, 날짜 형식 지정, 시간대 설정, 스크립트에서 활용 방법을 포함한 포괄적인 가이드입니다."
keywords: "date, 날짜, 시간, linux, 명령어, 타임스탬프, 시간대, UTC, KST, 리눅스"
author: "HojinLee"
og_title: "date - 리눅스 날짜 시간 명령어 - 개발자를 위한 리눅스"
og_description: "date 명령어의 사용법과 옵션을 알아보세요. 현재 날짜 시간 출력, 날짜 형식 지정, 시간대 설정, 스크립트에서 활용 방법을 포함한 포괄적인 가이드입니다."
og_type: "article"
twitter_card: "summary"
---

# date 명령어

`date` 명령어는 리눅스 시스템에서 현재 날짜와 시간을 출력하거나 설정하는 유틸리티입니다. 이 명령어는 시스템의 현재 시간을 확인하고, 다양한 형식으로 날짜와 시간 정보를 표시할 수 있습니다.

## 기본 사용법

### 현재 날짜와 시간 출력

가장 기본적인 사용법으로, 현재 시스템의 날짜와 시간을 출력합니다.

```console
hojin@DESKTOP-11LMH3B:~$ date
Thu May 21 15:41:31 KST 2020
```

## 날짜 형식 지정

`date` 명령어는 다양한 형식으로 날짜와 시간을 출력할 수 있습니다.

### 기본 형식 옵션

```console
# 년-월-일 형식
hojin@DESKTOP-11LMH3B:~$ date +%Y-%m-%d
2020-05-21

# 년/월/일 형식
hojin@DESKTOP-11LMH3B:~$ date +%Y/%m/%d
2020/05/21

# 요일, 월, 일, 년도
hojin@DESKTOP-11LMH3B:~$ date +%A, %B %d, %Y
Thursday, May 21, 2020

# 24시간 형식
hojin@DESKTOP-11LMH3B:~$ date +%Y-%m-%d %H:%M:%S
2020-05-21 15:41:31

# 12시간 형식
hojin@DESKTOP-11LMH3B:~$ date +%Y-%m-%d %I:%M:%S %p
2020-05-21 03:41:31 PM
```

### 자주 사용되는 형식 지정자

| 지정자 | 설명 | 예시 |
|--------|------|------|
| `%Y` | 4자리 년도 | 2020 |
| `%y` | 2자리 년도 | 20 |
| `%m` | 월 (01-12) | 05 |
| `%d` | 일 (01-31) | 21 |
| `%H` | 시간 (00-23) | 15 |
| `%I` | 시간 (01-12) | 03 |
| `%M` | 분 (00-59) | 41 |
| `%S` | 초 (00-59) | 31 |
| `%A` | 요일 (전체) | Thursday |
| `%a` | 요일 (축약) | Thu |
| `%B` | 월 (전체) | May |
| `%b` | 월 (축약) | May |
| `%p` | AM/PM | PM |
| `%Z` | 시간대 | KST |
| `%z` | 시간대 오프셋 | +0900 |
| `%s` | Unix 타임스탬프 | 1590049291 |

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

## 실용적인 예제

### 파일명에 날짜 사용

백업 파일이나 로그 파일의 이름에 날짜를 포함할 수 있습니다.

```console
# 현재 날짜로 파일명 생성
hojin@DESKTOP-11LMH3B:~$ backup_name="backup_$(date +%Y%m%d_%H%M%S).tar.gz"
hojin@DESKTOP-11LMH3B:~$ echo $backup_name
backup_20200521_154131.tar.gz

# 파일 생성
hojin@DESKTOP-11LMH3B:~$ touch "log_$(date +%Y-%m-%d).txt"
```

### 스크립트에서 활용

`date` 명령어는 스크립트에서 매우 유용하게 활용됩니다.

```bash
#!/bin/bash
# 현재 날짜를 변수에 저장
current_date=$(date +%Y-%m-%d)
current_time=$(date +%H:%M:%S)

echo "현재 날짜: $current_date"
echo "현재 시간: $current_time"

# 로그 파일 생성
log_file="log_${current_date}.log"
echo "[$(date +%Y-%m-%d %H:%M:%S)] 스크립트 시작" >> $log_file
```

### 시스템 시간 설정

시스템 시간을 설정할 수도 있습니다 (root 권한 필요).

```console
# 시스템 시간 설정 (root 권한 필요)
sudo date -s "2020-05-21 15:41:31"

# 또는
sudo date 052115412020.31
```

## 문제 해결

### 시간대 문제

시간대가 올바르게 설정되지 않은 경우 해결 방법입니다.

```console
# 현재 시간대 확인
hojin@DESKTOP-11LMH3B:~$ timedatectl status
               Local time: Thu 2020-05-21 15:41:31 KST
           Universal time: Thu 2020-05-21 06:41:31 UTC
                 RTC time: Thu 2020-05-21 06:41:31
                Time zone: Asia/Seoul (KST, +0900)

# 시간대 목록 확인
hojin@DESKTOP-11LMH3B:~$ timedatectl list-timezones | grep Seoul
Asia/Seoul

# 시간대 설정
sudo timedatectl set-timezone Asia/Seoul
```

### 날짜 형식 오류

날짜 형식이 올바르지 않은 경우의 해결 방법입니다.

```console
# 올바른 날짜 형식 예시
hojin@DESKTOP-11LMH3B:~$ date -d "2020-05-21"
hojin@DESKTOP-11LMH3B:~$ date -d "May 21 2020"
hojin@DESKTOP-11LMH3B:~$ date -d "21 May 2020"

# 잘못된 형식 (오류 발생 가능)
hojin@DESKTOP-11LMH3B:~$ date -d "2020/05/21"  # 대시(-) 사용 권장
```

## 고급 기능

### 날짜 계산

`date` 명령어를 사용하여 날짜 계산을 수행할 수 있습니다.

```bash
#!/bin/bash
# 7일 후 날짜 계산
future_date=$(date -d "7 days" +%Y-%m-%d)
echo "7일 후: $future_date"

# 30일 전 날짜 계산
past_date=$(date -d "30 days ago" +%Y-%m-%d)
echo "30일 전: $past_date"

# 특정 날짜로부터 계산
start_date="2020-05-01"
end_date=$(date -d "$start_date + 1 month" +%Y-%m-%d)
echo "시작일: $start_date"
echo "종료일: $end_date"
```

### 로그 타임스탬프

로그 파일에 타임스탬프를 추가하는 방법입니다.

```bash
# 로그에 타임스탬프 추가
echo "[$(date '+%Y-%m-%d %H:%M:%S')] 작업 시작" >> /var/log/app.log

# 또는 ISO 8601 형식
echo "[$(date -Iseconds)] 작업 시작" >> /var/log/app.log
```

`date` 명령어는 리눅스 시스템 관리와 스크립트 작성에서 필수적인 도구입니다. 다양한 형식 지정자와 옵션을 활용하여 효율적으로 날짜와 시간 정보를 처리할 수 있습니다.