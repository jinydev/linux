---
layout: home
title: "CLI 기본 명령어"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# CLI 기본 명령어

## CLI 기본 명령어

### 1. 파일 및 디렉토리 관리

**기본 명령어:**
```bash
# 현재 디렉토리 확인
pwd

# 디렉토리 목록 보기
ls
ls -la          # 숨김 파일 포함 모든 정보
ls -lh          # 파일 크기 사람이 읽기 쉽게

# 디렉토리 이동
cd /path/to/directory
cd ~            # 홈 디렉토리로 이동
cd ..           # 상위 디렉토리로 이동

# 디렉토리 생성
mkdir directory_name
mkdir -p parent/child  # 상위 디렉토리도 함께 생성

# 파일/디렉토리 삭제
rm filename
rm -r directory_name   # 디렉토리 재귀 삭제
rm -f filename         # 강제 삭제
```

### 2. 파일 조작

**파일 관리 명령어:**
```bash
# 파일 복사
cp source destination
cp -r source_dir destination_dir

# 파일 이동/이름 변경
mv old_name new_name
mv file destination/

# 파일 내용 보기
cat filename
less filename          # 페이징으로 보기
head -n 10 filename    # 처음 10행 보기
tail -n 10 filename    # 마지막 10행 보기

# 파일 검색
find /path -name "*.txt"
grep "pattern" filename
```

### 3. 시스템 정보 확인

**시스템 모니터링 명령어:**
```bash
# 시스템 정보
uname -a               # 커널 정보
cat /proc/version      # 커널 버전
cat /etc/os-release    # 배포판 정보

# 프로세스 정보
ps aux                 # 모든 프로세스
top                    # 실시간 프로세스 모니터링
htop                   # 향상된 top (설치 필요)

# 시스템 리소스
free -h                # 메모리 사용량
df -h                  # 디스크 사용량
du -sh directory       # 디렉토리 크기
```


---

[⬅️ 이전](../)
