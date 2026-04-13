---
layout: home
title: "고급 활용"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 고급 활용

## 고급 활용

### 환경 변수와 함께 사용

환경 변수와 함께 사용하여 더 상세한 정보를 얻을 수 있습니다.

```bash
#!/bin/bash
# 사용자 정보와 환경 변수 확인
current_user=$(whoami)
user_home=$HOME
user_shell=$SHELL

echo "사용자: $current_user"
echo "홈 디렉터리: $user_home"
echo "기본 쉘: $user_shell"
```

### 시스템 모니터링

시스템 모니터링 스크립트에서 사용자 활동을 추적할 수 있습니다.

```bash
#!/bin/bash
# 사용자 활동 로그
log_file="/var/log/user_activity.log"
current_user=$(whoami)
current_time=$(date '+%Y-%m-%d %H:%M:%S')
current_dir=$(pwd)

echo "$current_time - 사용자: $current_user - 디렉터리: $current_dir" >> $log_file
```

### 다중 사용자 환경

다중 사용자 환경에서 사용자별 작업을 관리할 때 활용할 수 있습니다.

```bash
#!/bin/bash
# 사용자별 작업 디렉터리 생성
current_user=$(whoami)
user_workspace="/workspace/$current_user"

# 사용자별 작업 디렉터리가 없으면 생성
if [ ! -d "$user_workspace" ]; then
    mkdir -p "$user_workspace"
    echo "작업 디렉터리가 생성되었습니다: $user_workspace"
fi

# 작업 디렉터리로 이동
cd "$user_workspace"
echo "현재 작업 디렉터리: $(pwd)"
```

`whoami` 명령어는 간단하지만 매우 유용한 리눅스 명령어입니다. 특히 스크립트 작성과 시스템 관리에서 현재 사용자 정보를 확인하는 데 필수적인 도구로 활용됩니다.

---

[⬅️ 이전: date - 리눅스 날짜 시간 명령어 - 개발자를 위한 리눅스](../date/) &nbsp;|&nbsp; [🏠 분류 목차](../../../../) &nbsp;|&nbsp; [다음: 8.1 문서 에디터 종류 (vi/nano) ➡️](../../../04_3_editor/04_3_1_vim/)


---

[⬅️ 이전](../)
