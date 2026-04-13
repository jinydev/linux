---
layout: home
title: "유틸리티 Utility"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 유틸리티 Utility

## 유틸리티 (Utility)

### 1. 유틸리티의 개념과 역할

유틸리티는 사용자가 시스템을 편리하게 사용하기 위한 용용 프로그램입니다. 쉘과 유틸리티는 사용자 입장에서는 구분이 필요 없으며, 시스템을 더욱 효율적으로 사용할 수 있도록 도움을 줍니다.

#### 유틸리티의 주요 기능

**시스템 관리:**
- **시스템 모니터링**: CPU, 메모리, 디스크 사용량 확인
- **네트워크 관리**: 네트워크 연결 및 설정 관리
- **사용자 관리**: 사용자 계정 및 권한 관리
- **서비스 관리**: 시스템 서비스 시작/중지/재시작

**파일 관리:**
- **파일 조작**: 파일 복사, 이동, 삭제
- **압축/해제**: 파일 압축 및 압축 해제
- **검색**: 파일 및 디렉토리 검색
- **편집**: 텍스트 파일 편집

### 2. 주요 유틸리티

#### 시스템 모니터링 유틸리티

**CPU 및 메모리 모니터링:**
```bash
# CPU 사용량 확인
top
htop
mpstat

# 메모리 사용량 확인
free -h
vmstat

# 디스크 사용량 확인
df -h
du -sh directory
```

**네트워크 모니터링:**
```bash
# 네트워크 연결 확인
netstat -tuln
ss -tuln

# 네트워크 인터페이스 확인
ip addr
ifconfig

# 네트워크 연결 테스트
ping hostname
traceroute hostname
```

#### 파일 관리 유틸리티

**파일 조작:**
```bash
# 파일 복사
cp source destination

# 파일 이동
mv old_name new_name

# 파일 삭제
rm filename

# 파일 내용 보기
cat filename
less filename
head -n 10 filename
tail -n 10 filename
```

**파일 검색:**
```bash
# 파일 검색
find /path -name "filename"

# 내용 검색
grep "pattern" filename

# 파일 타입 확인
file filename

# 파일 권한 확인
ls -la filename
```

#### 텍스트 처리 유틸리티

**텍스트 편집:**
```bash
# 간단한 텍스트 편집
nano filename
vim filename

# 텍스트 처리
sed 's/old/new/g' filename
awk '{print $1}' filename

# 텍스트 정렬
sort filename
uniq filename
```

**파일 비교:**
```bash
# 파일 비교
diff file1 file2

# 파일 병합
patch file.patch

# 파일 무결성 확인
md5sum filename
sha256sum filename
```

### 3. 유틸리티의 특징

#### 모듈화된 설계

**유틸리티의 특징:**
- **단일 기능**: 각 유틸리티는 하나의 특정 기능을 수행
- **파이프라인**: 여러 유틸리티를 연결하여 복잡한 작업 수행
- **재사용성**: 다른 스크립트나 프로그램에서 재사용 가능
- **확장성**: 새로운 유틸리티 추가 가능

#### Unix 철학

**Unix 철학의 적용:**
- **작은 것이 아름답다**: 작고 단순한 프로그램
- **한 가지 일을 잘 한다**: 각 프로그램은 하나의 기능에 집중
- **파이프라인으로 연결**: 프로그램들을 연결하여 복잡한 작업 수행
- **텍스트 기반**: 텍스트 파일을 통한 데이터 교환


---

[⬅️ 이전](../)
