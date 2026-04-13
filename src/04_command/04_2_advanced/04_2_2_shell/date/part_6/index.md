---
layout: home
title: "고급 기능"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 고급 기능

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

---

[⬅️ 이전: cal - 리눅스 달력 명령어 - 개발자를 위한 리눅스](../cal/) &nbsp;|&nbsp; [🏠 분류 목차](../../../../) &nbsp;|&nbsp; [다음: whoami - 리눅스 사용자 확인 명령어 - 개발자를 위한 리눅스 ➡️](../whoami/)


---

[⬅️ 이전](../)
