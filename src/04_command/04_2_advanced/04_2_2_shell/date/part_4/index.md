---
layout: home
title: "실용적인 예제"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 실용적인 예제

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


---

[⬅️ 이전](../)
