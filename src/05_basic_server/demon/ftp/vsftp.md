---
layout: home
---

# vsFTP
vsftpd(매우 안전한 FTP 데몬)는 Linux 및 Unix 계열 시스템을 위한 가볍고 안전하며 빠른 FTP 서버 소프트웨어입니다. 보안 기능과 단순성으로 유명하여 FTP 서버 설치에 널리 사용됩니다.  

## vsftpd의 몇 가지 주요 기능

* 보안: vsftpd는 보안을 염두에 두고 설계되었으며 chroot 감옥, IP 기반 액세스 제한, SSL/TLS 암호화 및 일반적인 FTP 취약성으로부터 보호하는 데 도움이 되는 강력한 구성 옵션 세트와 같은 기능을 포함합니다.

* 성능: vsftpd는 고성능에 최적화되어 있으며 많은 수의 동시 연결을 처리할 수 있어 트래픽이 많은 환경에서 사용하기에 적합합니다.

* 손쉬운 구성: vsftpd는 구성하기 쉽고 사용자가 필요에 따라 FTP 서버를 설정하고 사용자 지정하는 데 도움이 되는 포괄적인 문서 세트와 함께 제공됩니다.

* 호환성: vsftpd는 Linux, FreeBSD 및 Solaris를 포함한 대부분의 Unix 계열 운영 체제와 호환됩니다.

전반적으로 vsftpd는 엔터프라이즈 환경, 웹 호스팅 서비스 및 안전한 파일 전송이 필요한 기타 시나리오에서 널리 사용되는 안정적이고 안전한 FTP 서버입니다.

## 설치하기
우분에 `vsftpd` 패키지를 설치합니다.
```bash
sudo apt install vsftpd –y
```

## anonymous 
익명 사용자의 접속 및 파일 업로드를 허용하도록 설정하기.  

```bash
sudo /etc/vsftpd.conf
```
vi 에디터로 `/etc/vsftpd.conf` 파일 열기, anonymous 계정의 권한 변경

```ini
anonymous_enable=YES #25
write_enable=YES # 31
anon_upload_enable=YES # 40
anon_mkdir_write_enable=YES # 44
```

한글폴더 폴기 허용
```ini
utf8_filesystem=YES
```


### 패시브 모드
기본적으로 `vsftpd`는 데이터 전송에 `패시브` 모드를 사용합니다. 클라이언트가 수동 모드를 사용하도록 구성되지 않은 경우 서버와의 데이터 연결을 설정할 수 없어 파일 목록이 표시되지 않을 수 있습니다. 수동 모드를 사용하도록 클라이언트를 구성하거나 vsftpd 구성 파일(/etc/vsftpd.conf)에 다음 줄을 추가하여 vsftpd에서 활성 모드를 활성화할 수 있습니다.

```bash
pasv_enable=NO
```


### 익명 폴더
anonymous로 접속되는 기본 디렉터리는 `/srv/ftp` 
이 디렉터리 안에 `pub 디렉터리`를 만들고 모든 사용자의 `읽기`, `쓰기` 권한 허용합니다.

```bash
cd /srv/ftp
mkdir pub
chmod 777 pub
```

### 재시작
변경된 설정을 적용하기 위하여 vsftpd 데몬을 재시작 합니다.
```bash 
sudo systemctl restart vsftpd
sudo systemctl enable vsftpd
```

vsftpd 데몬이 정상적으로 실행되고 있는지 확인합니다.  

```bash
systemctl status vsftpd 
```

## 방화벽 허용 
외부에서 FTP 서버에 접근하도록 방화벽 포트를 허용합니다.
```bash
sudo ufw allow ftp
sudo ufw reload
```

> 문제가 계속 발생시 : 원활한 외부 접속을 허용하기 위해 systemctl stop ufw 명령으로 잠시 방화벽을 끔

## 접속 주소 확인
`ifconfig` 명령으로 서버의 IP 주소 확인

```bash
poly@poly-VirtualBox:/srv/ftp$ ifconfig
enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::7cac:debc:82dc:b444  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:17:48:bc  txqueuelen 1000  (Ethernet)
        RX packets 56675  bytes 85372089 (85.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4359  bytes 296103 (296.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

enp0s8: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.56.114  netmask 255.255.255.0  broadcast 192.168.56.255
        inet6 fe80::6fee:caa9:42b4:a0e2  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:85:76:27  txqueuelen 1000  (Ethernet)
        RX packets 690  bytes 58667 (58.6 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 557  bytes 75170 (75.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 203  bytes 19696 (19.6 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 203  bytes 19696 (19.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

호스트 전용 어뎁터로 연결된 `192.168.56.114`를 확인할 수 있습니다.



## 클라이언트 접속

![슬라이드39](./img/슬라이드39.PNG)

![슬라이드40](./img/슬라이드40.PNG)

![슬라이드41](./img/슬라이드41.PNG)

![슬라이드42](./img/슬라이드42.PNG)

![슬라이드43](./img/슬라이드43.PNG)

## 계정별 접속
특정 계정을 사용하여 vsftpd에 대한 액세스를 허용하려면 다음 단계를 수행해야 합니다.

* FTP 서버에 액세스하는 데 사용할 새 시스템 사용자 계정을 만듭니다. "adduser" 명령을 사용하여 새 사용자를 만들 수 있습니다. 예를 들면 다음과 같습니다.

```bash
sudo adduser ftpuser
```

* `passwd` 명령을 사용하여 새 사용자 계정의 암호를 설정합니다.

```bash
sudo passwd ftpuser
```

* 인증에 로컬 사용자 계정을 사용하도록 vsftpd를 구성합니다. 이는 vsftpd 구성 파일(/etc/vsftpd.conf)에 다음 줄을 추가하여 수행할 수 있습니다.

```bash
local_enable=YES
```

* 선택적으로 사용자를 자신의 홈 디렉토리로 chroot하도록 vsftpd를 구성할 수도 있습니다. 이렇게 하면 FTP 서버에 대한 액세스가 자신의 홈 디렉토리로만 제한됩니다. 이는 vsftpd 구성 파일에 다음 줄을 추가하여 수행할 수 있습니다.

```bash
chroot_local_user=YES
allow_writeable_chroot=YES
```

* vsftpd 서비스를 다시 시작하여 변경 사항을 적용합니다.
```bash
sudo systemctl restart vsftpd
```

이 단계를 완료한 후 새 사용자 계정과 설정한 암호를 사용하여 vsftpd 서버에 연결할 수 있어야 하며 사용자는 홈 디렉토리로 제한됩니다(chrooting이 활성화된 경우).
