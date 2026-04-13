---
layout: home
title: "4 Ubuntu 설치 완료 후 기본 설정"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 4 Ubuntu 설치 완료 후 기본 설정

## 4. Ubuntu 설치 완료 후 기본 설정

설치가 끝나고 바탕화면(또는 터미널)에 접속했다면 가장 먼저 시스템을 최신 상태로 업데이트해야 합니다. 터미널을 열고 다음 명령어들을 순서대로 입력하세요.

### 4.1 시스템 업데이트 및 업그레이드
```bash
# 원격 저장소에서 패키지 목록의 버전들을 최신으로 갱신
sudo apt update

# 실제로 컴퓨터에 깔린 패키지들을 최신 버전으로 업그레이드
sudo apt upgrade -y

# 업그레이드 후 남은 불필요한 찌꺼기 패키지 자동 제거
sudo apt autoremove -y
```

### 4.2 필수 유틸리티 및 개발 환경 설치
리눅스 서버 운영과 프로그래밍에 뼈대가 되는 최소 도구들을 설치해 둡니다.
```bash
# 텍스트 에디터, 네트워크 도구 모니터링 도구 
sudo apt install vim git curl wget htop -y

# 기본 컴파일러 시스템과 파이썬/노드 
sudo apt install build-essential python3-pip nodejs npm -y
```

### 4.3 방화벽(UFW) 기본 보안 세팅
서버로 운영할 계획이 있다면 불필요한 접속을 차단해야 합니다.
```bash
# 방화벽 활성화 (주의: 원격 환경일 경우 ssh가 막히지 않게 조치)
sudo ufw enable

# 웹(http) 및 원격접속(ssh) 포트만 허용
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
```


---

[⬅️ 이전](../)
