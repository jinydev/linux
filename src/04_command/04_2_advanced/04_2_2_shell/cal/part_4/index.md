---
layout: home
title: "고급 사용법"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 고급 사용법

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


---

[⬅️ 이전](../)
