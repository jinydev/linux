# [FTP 서버 설치와 운영]

FTP(File Transfer Protocol)는 파일 전송을 위한 프로토콜 중 하나로, 파일을 전송하고 다운로드할 수 있도록 해줍니다. 이번에는 FTP 서버를 설치하고 운영하는 방법에 대해 알아보겠습니다.

1. vsftpd 설치
 $ sudo apt update 
 $ sudo apt install vsftpd 

2. 방화벽 포트(20번,21번) 허용 
vsftpd는 기본적으로 20번, 21번 포트를 사용한다. 방화벽을 사용한다면 해당 포트번호를 허용해준다.
 
$ sudo ufw allow 20/tcp
$ sudo ufw allow 21/tcp
$ sudo ufw enable
3. /etc/vsftpd.conf 설정 파일 수정
 $ sudo gedit /etc/vsftpd.conf 

 ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99FD4E395C34311B17)

 /etc/vsftpd.conf 파일 (설정파일 수정)

# anonymous 유저 허용 여부
anonymous_enable=NO 

# 계정사용자 접속 허용 여부
local_enable=YES 

# 업로드 허용 여부
write_enable=YES 

# 디렉토리나 파일 생성시 umask 값 
# local_umask의 숫자를 변경하여 기본 권한을 변경해 준다.
# 디폴트값 022
local_umask = 022
폴더는 777 - 022 = 775
파일은 666 - 022 = 644

# 사용자 홈디렉토리에 .message 파일에 작성 
dirmessage_enable=YES 
# chroot 적용 자신의 계정에서 상위 디렉토리로 이동 허용 여부
chroot_local_user=YES 
allow_chroot

4. vsftpd서비스 재시작
자신의 상황에 맞게 설정하면 되고 아래의 문서를 참고하여 필요한 설정을 해준다. 
https://security.appspot.com/vsftpd/vsftpd_conf.html

설정이 끝나면 vsftpd 서비스를 재시작 해준다.
 $ sudo service vsftpd restart
파일질라로 접속해본다.

## proftp 설치
1 단계 : ProFTPD 서버 설치
물론 사용하려면 소프트웨어를 설치해야합니다. 먼저 터미널에서 다음 apt-get 명령을 실행하여 모든 시스템 패키지가 최신 상태인지 확인하십시오.

$ sudo apt-get update
$ sudo apt-get upgrade
이제 ProFTPD 서버를 설치하려면 터미널에서 실행하십시오.

$ sudo apt-get install proftpd
설치하는 동안 ProFTPD 서버에 대해 원하는 사용 유형을 선택하라는 메시지가 표시되며 필요에 맞는 최상의 모드를 선택할 수 있습니다.

2 단계 : ProFTPD 서버 구성
사용하기 전에 일부 파일을 편집해야합니다. /etc/proftpd/proftpd.conf 는 Ubuntu/Debian 서버의 기본 구성 파일이며 를 사용하여 편집을 시작합니다. vi 명령을 실행합니다.

$ sudo vi /etc/proftpd/proftpd.conf
![](https://ko.linux-console.net/common-images/install-proftpd-in-ubuntu-and-debian/Configure-Proftpd-in-Ubuntu-620x423.png)

아래와 같이 파일의 내용을 변경합니다.

- ServerName: Make it your default server name.
- UseIPV6: You may switch it to “Off“, if you don’t use it.
- DefaultRoot : Uncomment this line to restrict users with their home folders.
- RequireValidShell: Uncomment this line and make it “On” to enable logging in for users, even for those who doesn’t have a valid shell in /etc/shells to log in.
- AuthOrder: Uncomment the line to enable the using of local passwords.
- Port: This line defines the default port for the FTP server, it is 21 by default. If you want, you can define any custom port here.
- SystemLog: The default log file path, you may change it if you want.


ProFTPD 서버를 다시 시작

$ sudo service proftpd restart