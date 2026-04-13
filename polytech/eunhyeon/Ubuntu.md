---
layout: home
---

# 리눅스 - 우분투(Ubuntu) 자격 증명 및 패키지 관리
## 0418. `su`, `sudo`, `apt` 명령어 
<hr/>

우분투를 포함한 리눅스 환경에서 시스템 설정을 변경하거나 소프트웨어를 설치하려면 **최고 관리자(root)** 권한이 필요합니다. 일반 제약이 있는 사용자 계정(User)이 관리자 권한을 획득하고 패키지를 관리하는 핵심 명령어들을 살펴봅니다.

## 1. 계정 전환: `su` (Substitute User)
`su` 명령어는 현재 접속한 사용자 계정을 다른 사용자 계정(기본적으로 root)으로 완전히 전환할 때 사용합니다. 

```bash
su          # root 사용자로 변경 (root 비밀번호 입력 필요)
exit        # 원래 사용자로 복귀
su user01   # user01 사용자로 변경 (user01 비밀번호 입력 필요)
su - user01 # user01 사용자로 변경하면서 시스템 환경변수(PATH 등)까지 타겟 사용자의 것으로 초기화
whoami      # 현재 쉘을 실행 중인 사용자 이름 확인
```

## 2. 관리자 권한 차용: `sudo` (Superuser DO)
`sudo` 명령어는 계정 자체를 변경하지 않고, **단일 명령어에 한해서만 일시적으로 최고 관리자(root) 권한**을 빌려 실행하는 도구입니다.

* `su`가 root 비밀번호를 공유해야 하는 보안상 약점이 있는 반면, `sudo`는 **현재 사용자의 비밀번호**만 입력하면 되며, 로그가 시스템에 남기 때문에 한층 더 안전하고 권장되는 방식입니다.
* 사용자가 `/etc/sudoers` 파일이나 `sudo` 그룹에 등록되어 있어야만 사용이 가능합니다.

```bash
sudo apt update         # root 권한으로 패키지 인덱스 업데이트 실행
sudo -s                 # 임시로 root 권한의 쉘을 실행 (현재 작업 디렉토리 유지)
sudo -i                 # 완전한 root 환경으로 로그인 (root의 Home 디렉토리로 이동)
```

## 3. 우분투 패키지 관리자: `apt` (Advanced Packaging Tool)
우분투 및 데비안 계열의 핵심 패키지 관리 도구입니다. 옛날에는 `apt-get`과 `apt-cache`로 나뉘어져 파편화된 명령어를 썼으나, 현재는 사용자 친화적인 **`apt`** 명령어로 통합되어 이를 사용하는 것이 현대적인 표준(Best Practice)입니다.

패키지 소스(저장소) 목록은 `/etc/apt/sources.list` 및 `/etc/apt/sources.list.d/` 디렉터리에 정의되어 있습니다.

```bash
# 1. 패키지 인덱스 업데이트 (원격 저장소에서 최신 소프트웨어 목록을 가져옴, 설치는 안함)
sudo apt update

# 2. 시스템의 모든 패키지를 최신 버전으로 업그레이드
sudo apt upgrade

# 3. 특정 패키지 설치
sudo apt install <패키지명>
sudo apt install nginx    # 예시: nginx 설치

# 4. 패키지 삭제
sudo apt remove <패키지명>  # 설정 파일은 남기고 삭제
sudo apt purge <패키지명>   # 설정 파일까지 완전히 찌꺼기 없이 삭제

# 5. 패키지 정보 검색
apt search <검색어>         # 패키지 이름이나 설명이 포함된 패키지 찾기
apt show <패키지명>         # 특정 패키지의 상세 정보, 버전, 의존성 확인
```
