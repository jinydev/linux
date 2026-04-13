---
layout: home
title: "고급 사용법"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 고급 사용법

## 고급 사용법

### 스크립트에서 활용

`whoami` 명령어는 스크립트에서 매우 유용하게 활용됩니다.

```bash
#!/bin/bash
# 현재 사용자 확인
current_user=$(whoami)

echo "현재 사용자: $current_user"

# 사용자별 조건 분기
if [ "$current_user" = "root" ]; then
    echo "관리자 권한으로 실행 중입니다."
elif [ "$current_user" = "hojin" ]; then
    echo "일반 사용자로 실행 중입니다."
else
    echo "알 수 없는 사용자: $current_user"
fi
```

### 보안 검증

스크립트에서 특정 사용자만 실행할 수 있도록 제한하는 데 사용할 수 있습니다.

```bash
#!/bin/bash
# root 사용자만 실행 가능하도록 제한
if [ "$(whoami)" != "root" ]; then
    echo "이 스크립트는 root 권한이 필요합니다."
    echo "현재 사용자: $(whoami)"
    exit 1
fi

echo "관리자 권한으로 스크립트가 실행되었습니다."
```

### 로그 파일에 사용자 정보 추가

로그 파일에 현재 사용자 정보를 포함하여 기록할 수 있습니다.

```bash
#!/bin/bash
# 로그 파일에 사용자 정보와 함께 기록
log_file="/var/log/app.log"
user_info=$(whoami)
timestamp=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$timestamp] 사용자: $user_info - 작업 시작" >> $log_file
```


---

[⬅️ 이전](../)
