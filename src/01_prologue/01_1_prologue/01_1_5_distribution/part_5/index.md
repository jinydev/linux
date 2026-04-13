---
layout: home
title: "배포판 설치 및 관리"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 배포판 설치 및 관리

## 배포판 설치 및 관리

### 1. 배포판 설치

#### 설치 방법

**라이브 USB:**
1. **ISO 다운로드**: 원하는 배포판의 ISO 파일 다운로드
2. **USB 제작**: USB 스틱에 라이브 이미지 작성
3. **부팅**: USB로 시스템 부팅
4. **설치**: 설치 프로그램 실행

**가상 머신:**
1. **가상화 소프트웨어**: VirtualBox, VMware 등 설치
2. **가상 머신 생성**: 새로운 가상 머신 생성
3. **ISO 마운트**: 배포판 ISO 파일 마운트
4. **설치**: 가상 머신 내에서 설치

#### 설치 시 고려사항

**하드웨어 호환성:**
- **드라이버 지원**: 하드웨어 드라이버 지원 여부 확인
- **최소 요구사항**: 배포판의 최소 시스템 요구사항 확인
- **권장 사양**: 권장 시스템 사양 확인

**데이터 백업:**
- **중요 데이터**: 설치 전 중요 데이터 백업
- **설치 방식**: 듀얼 부팅 또는 전체 설치 선택
- **파티션**: 디스크 파티션 계획 수립

### 2. 배포판 관리

#### 패키지 관리

**패키지 설치:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install package-name

# CentOS/RHEL
sudo yum install package-name
# 또는
sudo dnf install package-name

# Fedora
sudo dnf install package-name
```

**패키지 업데이트:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt upgrade

# CentOS/RHEL
sudo yum update
# 또는
sudo dnf update

# Fedora
sudo dnf update
```

#### 시스템 관리

**시스템 모니터링:**
- **리소스 모니터링**: CPU, 메모리, 디스크 사용량 확인
- **프로세스 관리**: 실행 중인 프로세스 관리
- **서비스 관리**: 시스템 서비스 시작/중지/재시작

**보안 관리:**
- **정기 업데이트**: 시스템 및 패키지 정기 업데이트
- **방화벽 설정**: 방화벽 규칙 설정 및 관리
- **사용자 관리**: 사용자 계정 및 권한 관리


---

[⬅️ 이전](../)
