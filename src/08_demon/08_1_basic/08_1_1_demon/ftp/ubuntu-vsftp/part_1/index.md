---
layout: home
title: "vsftpd 설정"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# vsftpd 설정

## vsftpd 설정
vsftpd.conf 파일을 열어 FTP 서버의 설정을 변경해줘야 합니다.

```
sudo nano /etc/vsftpd.conf
```

다음과 같은 설정을 추가해줍니다.

```
listen=YES
listen_ipv6=NO
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES
chroot_local_user=YES
secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd
pasv_enable=YES
pasv_min_port=40000
pasv_max_port=40100
```

* listen: FTP 서버가 동작하는 IP와 포트를 설정합니다.
* anonymous_enable: 익명 FTP 접속을 허용할지 여부를 설정합니다.
* local_enable: 로컬 FTP 접속을 허용할지 여부를 설정합니다.
* write_enable: FTP 서버에서 파일 쓰기를 허용할지 여부를 설정합니다.
* local_umask: FTP 클라이언트에서 업로드한 파일의 권한을 설정합니다.
* dirmessage_enable: 디렉토리의 메시지를 출력할지 여부를 설정합니다.
* use_localtime: 서버 시간대를 사용할지 여부를 설정합니다.
* xferlog_enable: 전송 로그를 기록할지 여부를 설정합니다.
* connect_from_port_20: 데이터 포트를 20번 포트 대신에 다른 포트를 사용하도록 설정합니다.
* chroot_local_user: 사용자의 홈 디렉토리로 제한합니다.
* secure_chroot_dir: chroot 디렉토리를 설정합니다.
* pam_service_name: PAM 인증 모듈 이름을 설정합니다.
* pasv_enable: Passive 모드를 사용할지 여부를 설정합니다.
* pasv_min_port: Passive 모드에서 사용할 최소 포트를 설정합니다.
* pasv_max_port: Passive 모드에서 사용할 최대 포트를 설정합니다.

저장 후, FTP 서버를 재시작합니다.

```
sudo service vsftpd restart
```


---

[⬅️ 이전](../)
