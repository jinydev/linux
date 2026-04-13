---
layout: home
title: "CLI 사용 팁과 모범 사례"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# CLI 사용 팁과 모범 사례

## CLI 사용 팁과 모범 사례

### 1. 효율적인 명령어 사용

**명령어 히스토리 활용:**
```bash
# 히스토리 검색
history | grep search_term
Ctrl + R                # 역방향 검색
!number                 # 히스토리 번호로 명령어 실행
```

**별칭 설정:**
```bash
# 자주 사용하는 명령어를 별칭으로 설정
alias ll='ls -la'
alias ..='cd ..'
alias grep='grep --color=auto'
```

### 2. 스크립팅 기초

**간단한 스크립트 예제:**
```bash
#!/bin/bash
# 기본 스크립트 템플릿

echo "Hello, World!"
echo "Current directory: $(pwd)"
echo "Current user: $(whoami)"
```

### 3. 권한 관리

**파일 권한 이해:**
```bash
# 권한 확인
ls -la filename

# 권한 변경
chmod 755 filename     # 숫자로 권한 설정
chmod +x filename      # 실행 권한 추가
chmod -w filename      # 쓰기 권한 제거

# 소유자 변경
chown user:group filename
```


---

[⬅️ 이전](../)
