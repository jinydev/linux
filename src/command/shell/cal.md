---
layout: home
title: "cal - 리눅스 달력 명령어 - 개발자를 위한 리눅스"
description: "cal 명령어의 사용법과 옵션을 알아보세요. 달력 출력, 한글 달력 설정, 다양한 형식의 달력 표시 방법을 포함한 포괄적인 가이드입니다."
keywords: "cal, 달력, linux, 명령어, locale, 한글달력, 날짜, 리눅스"
author: "HojinLee"
og_title: "cal - 리눅스 달력 명령어 - 개발자를 위한 리눅스"
og_description: "cal 명령어의 사용법과 옵션을 알아보세요. 달력 출력, 한글 달력 설정, 다양한 형식의 달력 표시 방법을 포함한 포괄적인 가이드입니다."
og_type: "article"
twitter_card: "summary"
---

# cal 명령어

`cal` 명령어는 리눅스 시스템에서 달력을 출력하는 유틸리티입니다. 이 명령어는 현재 월의 달력이나 지정된 년도, 월의 달력을 터미널에 표시할 수 있습니다.

## 기본 사용법

### 현재 월의 달력 출력

가장 기본적인 사용법으로, 현재 월의 달력을 출력합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cal
      May 2020
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
```

### 특정 년도 달력 출력

`-y` 옵션을 사용하여 전체 년도 달력을 출력할 수 있습니다.

```console
hojin@DESKTOP-11LMH3B:~$ cal -y 2020
                               2020
      January               February               March
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
          1  2  3  4                     1   1  2  3  4  5  6  7
 5  6  7  8  9 10 11   2  3  4  5  6  7  8   8  9 10 11 12 13 14
12 13 14 15 16 17 18   9 10 11 12 13 14 15  15 16 17 18 19 20 21
19 20 21 22 23 24 25  16 17 18 19 20 21 22  22 23 24 25 26 27 28
26 27 28 29 30 31     23 24 25 26 27 28 29  29 30 31
```

### 특정 월 달력 출력

년도와 월을 지정하여 특정 월의 달력을 출력할 수 있습니다.

```console
hojin@DESKTOP-11LMH3B:~$ cal 12 2020
   December 2020
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
```

## 주요 옵션

### `-y` 옵션
현재 년도의 전체 달력을 출력합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cal -y
```

### `-m` 옵션
월요일을 주의 첫 번째 날로 표시합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cal -m
      May 2020
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```

### `-j` 옵션
율리우스력(Julian day numbers)으로 날짜를 표시합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cal -j 5 2020
        May 2020
 Su  Mo  Tu  We  Th  Fr  Sa
                    122 123
124 125 126 127 128 129 130
131 132 133 134 135 136 137
138 139 140 141 142 143 144
145 146 147 148 149 150 151
152
```

### `-3` 옵션
현재 월과 이전, 다음 월을 함께 표시합니다.

```console
hojin@DESKTOP-11LMH3B:~$ cal -3
      April 2020              May 2020              June 2020
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
          1  2  3  4                  1  2      1  2  3  4  5  6
 5  6  7  8  9 10 11   3  4  5  6  7  8  9   7  8  9 10 11 12 13
12 13 14 15 16 17 18  10 11 12 13 14 15 16  14 15 16 17 18 19 20
19 20 21 22 23 24 25  17 18 19 20 21 22 23  21 22 23 24 25 26 27
26 27 28 29 30        24 25 26 27 28 29 30  28 29 30
```

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

## 고급 사용법

### 특정 년도 범위 출력

여러 년도의 달력을 연속으로 출력할 수 있습니다.

```console
hojin@DESKTOP-11LMH3B:~$ for year in {2020..2022}; do echo "=== $year ==="; cal -y $year | head -9; done
```

### 달력 정보를 파일로 저장

달력 출력을 파일로 저장하여 나중에 참조할 수 있습니다.

```console
hojin@DESKTOP-11LMH3B:~$ cal -y > calendar_2020.txt
hojin@DESKTOP-11LMH3B:~$ cal 12 2020 > december_2020.txt
```

### 다른 명령어와 조합

`cal` 명령어를 다른 명령어와 조합하여 활용할 수 있습니다.

```console
# 현재 월의 마지막 날 확인
hojin@DESKTOP-11LMH3B:~$ cal | tail -1 | awk '{print $NF}'
31

# 현재 월의 주 수 확인
hojin@DESKTOP-11LMH3B:~$ cal | wc -l
8
```

## 문제 해결

### 로케일 오류

한글 로케일이 설치되지 않은 경우 다음 명령어로 설치할 수 있습니다.

```console
# Ubuntu/Debian
sudo apt-get install locales
sudo locale-gen ko_KR.UTF-8

# CentOS/RHEL
sudo yum install glibc-locale-source
sudo localedef -c -f UTF-8 -i ko_KR ko_KR.UTF-8
```

### 달력이 제대로 표시되지 않는 경우

터미널의 폰트 설정이나 인코딩 문제일 수 있습니다. 다음을 확인해보세요.

```console
# 터미널 인코딩 확인
hojin@DESKTOP-11LMH3B:~$ echo $LANG
ko_KR.UTF-8

# UTF-8 지원 확인
hojin@DESKTOP-11LMH3B:~$ locale -a | grep ko
ko_KR.utf8
```

## 활용 예제

### 스크립트에서 활용

`cal` 명령어를 스크립트에서 활용하는 예제입니다.

```bash
#!/bin/bash
# 현재 월의 날짜 수 확인
days_in_month=$(cal | tail -1 | awk '{print $NF}')
echo "이번 달은 $days_in_month일입니다."

# 주말 날짜 추출
weekends=$(cal | awk 'NR>2 {for(i=1;i<=NF;i++) if($i ~ /^[0-9]+$/ && (i==1 || i==7)) print $i}')
echo "주말 날짜: $weekends"
```

`cal` 명령어는 간단하지만 매우 유용한 리눅스 명령어입니다. 다양한 옵션과 조합을 통해 효율적으로 날짜 정보를 확인하고 관리할 수 있습니다.
