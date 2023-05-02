# 이것이 리눅스다

## FTP 서버 설치와 운영

- FTP(File TransferProtocol)는 파일을 전송하는데 사용하는 전용 서비스
- 웹 환경이 완전히 일반화되고 FTP의 고유 기능인 파일전송을 웹에서도 편리하게 할 수 있게 되면서 인기가 많이 떨어졌다.
- 하지만 성능이 매우 뛰어나므로 파일 전송이 목적인 사이트에서는 이 서비스가 계속해서 제공될 것이다.
- Centos에서 기본적으로 제공하는 **vsftpd, proctpd, pure-ftpd**를 설치하고 운영해보자.

## 1. vsftpd 설치와 운영

- vsftpd는 CentOS에서 기본적으로 제공
- 리눅스와 유닉스 환경에서 보안성과 성능이 우수한 FTP 서버로 인정

## FTP로 접속

우분에 `vsftpd` 패키지를 설치합니다.

- `sudo apt install vsftpd –y`****

## anonymous

익명 사용자의 접속 및 파일 업로드를 허용하도록 설정하기.

- `sudo /etc/vsftpd.conf`

- vi 에디터로 `/etc/vsftpd.conf` 파일 열기, anonymous 계정의 권한 변경
    
    `anonymous_enable=YES #25
    write_enable=YES # 31
    anon_upload_enable=YES # 40
    anon_mkdir_write_enable=YES # 44`
    

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled.png)

- `**:set number**`
    
    **→ 라인 넘버 나오게**
    

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%201.png)

- `anonymous_enable=YES #25`

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%202.png)

- `write_enable=YES # 31`

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%203.png)

- `anon_upload_enable=YES # 40`

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%204.png)

`anon_mkdir_write_enable=YES # 44`

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%205.png)

- `utf8_filesystem=YES`****

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%206.png)

### 패시브 모드

기본적으로 `vsftpd`는 데이터 전송에 `패시브` 모드를 사용합니다. 클라이언트가 수동 모드를 사용하도록 구성되지 않은 경우 서버와의 데이터 연결을 설정할 수 없어 파일 목록이 표시되지 않을 수 있습니다. 수동 모드를 사용하도록 클라이언트를 구성하거나 vsftpd 구성 파일(/etc/vsftpd.conf)에 다음 줄을 추가하여 vsftpd에서 활성 모드를 활성화할 수 있습니다.

- `pasv_enable=NO`
    
    **마지막 줄에 추가 하고 저장**
    

### 익명 폴더

anonymous로 접속되는 기본 디렉터리는 `/srv/ftp` 이 디렉터리 안에 `pub 디렉터리`를 만들고 모든 사용자의 `읽기`, `쓰기` 권한 허용합니다.

- `cd /srv/ftp`
- `mkdir pub`
- `chmod 777 pub`

### 재시작

변경된 설정을 적용하기 위하여 vsftpd 데몬을 재시작 합니다.

- `sudo systemctl restart vsftpd`
- `sudo systemctl enable vsftpd`

## 방화벽 허용

외부에서 FTP 서버에 접근하도록 방화벽 포트를 허용합니다.

- `sudo ufw allow ftp`
- `sudo ufw reload`

> 문제가 계속 발생시 : 원활한 외부 접속을 허용하기 위해 systemctl stop ufw 명령으로 잠시 방화벽을 끔
> 

---

## 클라이언트 접속 프로그램 필요

- **FileZilla 설치**

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%207.png)

- **설정 → 언어 → 한국어로 설정**

- **로그인**
    - 호스트: 192.168.56.100 (IP 입력)
    - 사용자명: anonymous
    - 비밀번호: 아무거나 입력하여 연결

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%208.png)

---

## 2. proftpd 설치와 운영

- 주로 대형 사이트에서 오랫동안 인기가 많았던 FTP 서버

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%209.png)

### proftpd의 설정 파일 변경

- 설정 파일은 /etc/proftpd.conf
- vi 에디터로 열고 anonymous 사용자가 접속할 수 있도록 변경하기

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%2010.png)

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%2011.png)

- proftpd 재시작, 방화벽 해제 진행
- 이후 FileZilla로 접속

---

## 3. Pure-ftpd의 설치

- yum -y install pure-ftpd
    
    → pure-ftpd 패키지 설치
    

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%2012.png)

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%2013.png)

- systemctl restart pure-ftpd
- systemctl enable pure-ftpd
    
    → 차례로 입력해 서비스 시작
    

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%A5%E1%86%BA%E1%84%8B%E1%85%B5%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%83%E1%85%A1%2026a379d99a764229ba26aef1201d1e1f/Untitled%2014.png)

- 홈 디렉터리에 업로드용 디렉터리와 다운로드용 디렉터리를 생성하고 허가권과 소유권을 변경

- 방화벽 해제
- FileZilla로 접속

---

## 차이점

- vsftpd, proftpd, pure-ftpd는 모두 Linux 시스템에서 사용 가능한 FTP 서버 소프트웨어

1. vsftpd(Very Secure FTP daemon):
    - 안전성과 보안성이 높은 FTP 서버
    - 가벼운 소프트웨어이며, 속도가 빠름
    - 다양한 인증 방식과 SSL/TLS 암호화 지원
    
2. proftpd:
    - 유연성과 확장성이 뛰어난 FTP 서버
    - 다양한 모듈과 기능을 제공하며, 커스터마이즈 가능
    - 고급 사용자를 위한 확장된 기능 제공
    
3. pure-ftpd:
    - 가벼우며 빠른 FTP 서버
    - 다양한 인증 방식과 SSL/TLS 암호화 지원
    - 쉬운 설정 및 관리 가능
    
- 예를 들어, 보안성이 중요한 경우에는 vsftpd가 적합하며,
- 유연성이나 커스터마이즈 가능성이 필요한 경우에는 proftpd가 적합
- pure-ftpd는 가볍고 쉬운 설정 및 관리를 원하는 경우에 적합