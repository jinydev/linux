---
layout: home
title: "문제 해결"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 문제 해결

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


---

[⬅️ 이전](../)
