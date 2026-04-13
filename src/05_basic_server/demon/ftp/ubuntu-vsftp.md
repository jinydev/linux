---
layout: home
---

# vsftpd

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

## 방화벽 설정
FTP 서버에 방화벽을 설정해줘야 합니다. Ubuntu의 기본 방화벽인 ufw를 사용하여 설정합니다.

```
sudo ufw allow 20/tcp
sudo ufw allow 21/tcp
sudo ufw allow 40000:50000/tcp
sudo ufw enable
```

* ufw allow 20/tcp: FTP 서버의 데이터 포트를 열어줍니다.
* ufw allow 21/tcp: FTP 서버의 제어 포트를 열어줍니다.
* ufw allow 40000:50000/tcp: FTP 서버의 Passive 모드에서 사용하는 포트를 열어줍니다.
* ufw enable: 방화벽을 활성화합니다.

## 포트 포워딩
호스트에서 FTP 서버에 접속하기 위해서는 VirtualBox에서 포트 포워딩

VirtualBox에서 호스트와 게스트 간의 네트워크 연결 방식 중 하나인 NAT(Network Address Translation)를 사용하는 경우, 호스트에서 게스트에 접속하기 위해서는 게스트에서 열어둔 포트를 호스트에서 접근 가능한 포트로 포워딩해줘야 합니다.

* VirtualBox의 설정에서 네트워크 탭으로 이동합니다.
* NAT 네트워크의 설정을 클릭합니다.
* 포트 포워딩을 추가하기 위해서는 아래의 정보를 입력합니다.

    * 이름: 임의로 지정 가능합니다. 예를 들어, "FTP"라고 입력합니다.
    * 프로토콜: TCP
    * 호스트 IP: 비워둡니다.
    * 호스트 포트: 호스트에서 접근할 포트 번호를 입력합니다. 예를 들어, 21번 포트를 사용한다면 21이라고 입력합니다.
    * 게스트 IP: 비워둡니다.
    * 게스트 포트: 게스트에서 열어둔 포트 번호를 입력합니다. 예를 들어, vsftpd에서 설정한 Passive 모드에서 사용하는 포트 범위인 40000-40100번 포트 중 아무 번호나 입력합니다.


호스트에서 FTP 클라이언트를 실행하여, 호스트 IP와 호스트에서 포워딩한 포트 번호를 입력하면 게스트의 FTP 서버에 접속할 수 있습니다. 예를 들어, 호스트 IP가 192.168.0.10이고 호스트에서 포워딩한 포트 번호가 21번이라면, FTP 클라이언트에서 192.168.0.10:21로 접속하면 됩니다.
