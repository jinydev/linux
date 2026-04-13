---
layout: home
---

# 우분투 FTP 서버 설치 및 운영 가이드

**FTP (File Transfer Protocol)**는 대용량 파일 전송을 위해 고안된 유서 깊은 프로토콜입니다. 리눅스 환경에서 가장 널리 쓰이는 매우 빠르고 안정적인 FTP 데몬인 `vsftpd`의 설치 및 운용 방법을 알아봅니다.

---

## 1. vsftpd (Very Secure FTP Daemon) 설치 및 방화벽 오픈

우분투 패키지 매니저를 통해 설치합니다.
```bash
sudo apt update 
sudo apt install vsftpd 
```

FTP는 특이하게 두 개의 포트를 사용합니다 (20번: 데이터 전송용, 21번: 명령어 제어용). 방화벽을 뚫어줍니다.
```bash
sudo ufw allow 20/tcp
sudo ufw allow 21/tcp
sudo ufw enable
```

> **[❗알림] Passive 모드 (수동 모드)**
> 현대 클라이언트 환경(유무선 공유기 내부)에서는 방화벽 NAT 통과 문제로 Active 모드가 아닌 Passive 모드가 필수입니다. 운용 시 `vsftpd.conf` 에 `pasv_min_port`, `pasv_max_port` 룰을 지정하고 해당 포트 대역 방화벽도 열어주어야 실무에서 에러가 없습니다.

---

## 2. vsftpd 환경 설정 (`/etc/vsftpd.conf`)

주요 옵션들을 에디터(nano, vim 등)로 열어 수정합니다.
```bash
sudo vi /etc/vsftpd.conf
```

**[핵심 옵션 해설]**
```ini
# anonymous(익명 무단 접속) 유저 허용 여부. 보안상 무조건 NO
anonymous_enable=NO 

# 시스템에 등록된 리눅스 계정 유저의 접속 허용 여부
local_enable=YES 

# 파일 업로드/수정 권한 활성화
write_enable=YES 

# 디렉터리 및 파일 생성 시 빼지는 권한 (umask)
# 기본 디렉터리 777에서 022를 빼면 755 생성, 파일은 666에서 022를 빼면 644가 생성됨
local_umask=022

# 사용자가 접속 시 루트 디렉터리(최상위 /)로 올라가버려서 전체 시스템을 엿보지 못하게
# 자신의 홈 디렉터리에 가둬버리는 감옥(chroot) 정책 활성화
chroot_local_user=YES 
allow_chroot_root_user=YES
```

다 설정했으면 데몬을 시스템에 재시작하여 적용합니다.
```bash
sudo systemctl restart vsftpd
```
이제 윈도우의 FileZilla 같은 클라이언트 프로그램에서 리눅스 IP를 입력하고 접속을 테스트할 수 있습니다.

---

## 3. (참고) ProFTPD 설치
vsftpd 외에도 기능적 유연성이 뛰어난 `proftpd` 데몬이 있습니다.
```bash
sudo apt install proftpd
```
* 환경설정 경로: `/etc/proftpd/proftpd.conf`를 수정하여 `Port 21`, `DefaultRoot ~` (홈 디렉터리 감옥) 등을 제어하고 재시작(`sudo systemctl restart proftpd`)합니다. 다만 보안 및 성능 최적화 면에서 최근엔 `vsftpd`가 더 널리 권장됩니다.