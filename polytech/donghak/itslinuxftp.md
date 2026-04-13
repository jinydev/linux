---
layout: home
---

# FTP 서버 설치와 운영 (vsftpd 기반)

전통적인 파일 전송 프로토콜인 FTP(File Transfer Protocol)는 웹 환경의 발전으로 인기가 줄어들긴 했지만, 오직 대용량 파일 전송만을 목적으로 하는 서버 인프라에서는 그 엄청난 처리 속도와 가벼움 덕분에 여전히 애용되고 있습니다. 

리눅스의 3대 FTP 데몬인 `vsftpd`, `proftpd`, `pure-ftpd` 중, 가장 보안성이 뛰어나고 실무 표준으로 사용되는 **vsftpd(Very Secure FTP Daemon)**를 중심으로 서버를 구축해 봅니다.

*(과거 보고서 오류 교정: 이전 자료에서 CentOS 생태계를 설명하며 갑자기 우분투의 `apt` 명령어를 혼용하는 심각한 충돌이 있었습니다. 아래 가이드는 실무 레드햇/기반 서버 생태계의 표준 `yum/dnf` 패키지 관리자를 기준으로 완전히 재작성되었습니다.)*

## 1. vsftpd 패키지 설치
리눅스 기본 저장소에서 가장 높은 평가를 받는 vsftpd를 다운로드하여 엽니다.
```bash
# 기본 패키지 관리자를 통한 고속 설치
sudo yum -y install vsftpd
```

## 2. FTP 환경 설정 (`/etc/vsftpd/vsftpd.conf`)
FTP 서버의 허가 정책을 결정합니다. 에디터(`vi`)로 설정 파일을 열어 익명(Anonymous) 사용자의 파일 업로드 및 디렉토리 생성 권한을 개방해 봅니다.

```bash
sudo vi /etc/vsftpd/vsftpd.conf
```
설정 파일 내부의 주요 지시자를 찾아 아래와 같이 `YES`로 변경(혹은 주석 `#` 해제)합니다.
```ini
# 익명 사용자(아이디: anonymous)의 접속을 허용합니다 (기본값)
anonymous_enable=YES 

# 파일 쓰기, 업로드, 디렉토리 생성 권한을 전면 허용합니다. (주석 해제)
write_enable=YES 
anon_upload_enable=YES 
anon_mkdir_write_enable=YES 

# (선택) 한글 파일명이 깨지는 것을 방지
utf8_filesystem=YES
```

## 3. 업로드용 디렉토리(pub) 권한 개방
`anonymous` 계정으로 접속했을 때 들어가는 기본 뿌리 경로는 `/var/ftp` 입니다. (우분투의 경우 `/srv/ftp`) 보안상 뿌리에 직접 쓰기는 막혀있으므로, 안에 전용 폴더를 뚫어주어야 합니다.
```bash
sudo cd /var/ftp
sudo mkdir pub            # pub 폴더 생성
sudo chmod 777 pub        # 누구나 읽고 쓰고 실행하도록 권한 777 부여
```

## 4. 방화벽 해제 및 서비스 재시작
FTP의 기본 통신 포트인 `21`번 포트를 방화벽에서 구멍 내어 외부 접속을 허락합니다.
```bash
# 방화벽(firewalld)에 ftp 서비스 룰을 영구적으로 개방
sudo firewall-cmd --permanent --add-service=ftp
sudo firewall-cmd --reload

# vsftpd 데몬 재시작 및 부팅 시 자동실행 등록
sudo systemctl restart vsftpd
sudo systemctl enable vsftpd
```

## 5. 클라이언트 접속 테스트 (FileZilla)
PC에 무료 FTP 클라이언트인 `FileZilla`를 설치합니다. 상단의 빠른 연결 탭에서 아래와 같이 입력하여 접속을 성공시킵니다.
* **호스트:** 서버의 IP 주소 (예: `192.168.56.100`)
* **사용자명:** `anonymous`
* **비밀번호:** (빈칸 혹은 아무 문자)
* **포트:** `21`

---

## 💡 참고: 리눅스 3대 FTP 서버 비교
1. **vsftpd:** 이름 그대로 보안(Secure)과 가벼움, 속도에 모든 것을 몰빵한 최고의 대중적 데몬.
2. **proftpd:** 복잡하고 거대한 기업용 서버에서 고도로 유연한 커스터마이징 모듈이 필요할 때 사용. (설정 문법이 아파치 웹서버와 아주 비슷합니다)
3. **pure-ftpd:** 구성이 극도로 직관적이고 가벼워 빠른 시간 안에 구축을 끝내고 싶을 때 매력적임.