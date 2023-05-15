---
layout: home
---

# 커맨드라인 33. 흐름제어: for 루프

for 루프는 반복 중에 작업 순서를 처리하는 수단을 제공한다는 점에서 while과 until
루프와 차이가 있다. 이는 프로그래밍할 때 매우 유용하다는 것을 알게 될 것이다. 
그래서 for 루프는 bash 스크립팅에서 매우 인기 있는 구조다.

## 1. for : 전통적인 쉘 형식

```bash
for variable [in words]; do
			commands
done
```

⇒ variable은 루프 수행 중에 증가되는 변수명이고, words 는 선택적인 variable에 순차적으로 할당되는 항목의 목록이다. commands는 각 반복마다 실행되는 명령들이다. 

### 기본 형식

```bash
[me@linuxbox ~]$ for i in A B C D; do echo $i; done
A
B
C
D
```

- for 명령어에 네 개의 단어 목록(A, B, C, D) 가 주어지고 루프는 네 번 실행된다.
- 각 루프가 실 행될 때마다 단어가 변수 i에 할당된다.
- 루프 내에서 echo 명령어로 할당내용을 보기 위해 i값을 표시한다.
- done 키워드는 루프를 닫는다.

### 중괄호 확장 형식

```bash
[me@linuxbox ~]$ for i in {A .. D}; do echo $i; done
A
B
C
D
```

### 경로명 확장 형식

```bash
[me@linuxbox ~]$ for i in distros*.txt;, do echo $i; done
distros-by-date.txt
distros-dates.txt
distros-key-names.txt
distros-key-vernums.txt
distros-names.txt
distros .txt
distros-vernums.txt
distros-versions.txt
```

### 명령어 치환

```bash
				#!/bin/bash
				# longest-word : find longest string in a file
				while [[ -n $1 ]]; do
								if [ [ -r $1 ]] ; then
								max_word=
								max_len=0
								for i in $(strings $1); do
												len=$(echo $i I wc -c)
												if (( len > max_len ) ) ; then
																max_len=$len
																max_word=$i
												fi
								done
								echo "$1: '$max_word' ($max_len characters)"
				fi
				shift
done
```

- 파일 내의 가장 긴 문자열을 검색 
→ 커맨드라인에 하나 이상의 파일명이 주어질 때, 이 프로그램은 각 파일마다 읽을 수 있는 텍스트 ‘단어들’ 의 목록을 생성하기 위해 strings 프로그램(GNU binutils 패키지에 포함된)을 사용한다.
- for 루프는 각 단어를 차례대로 처리하면서 현 단어가 지금까지 발견된 가장 긴 것인지 확인
- 만약 for 명령의 words 부분이 생략되면, for는 위치 매개변수를 기본으로 처리함

### while에서 for문으로 치환

```bash
			#!/bin/bash
			# longest-word2 : find longest string in a file
				for i; do
								if [ [ -r $1 ]] ; then
								max_word=
								max_len=0
								for j in $(strings $1); do
												len=$(echo $j | wc -c)
												if (( len > max_len ) ) ; then
																max_len=$len
																max_word=$i
												fi
								done
								echo "$1: '$max_word' ($max_len characters)"
				fi
done
```

- for 명령어에서 단어 목록이 생략되었기 때문에 그 대신 위치 매개변수를 사용한다.

## 2. for : C언어 형식

bash의 최신 버전에는 C언어에서 사용하는 형식과 닮은 for 명령 문법의 두 번째 형식이 추가되었다. 

```bash
for (( expressionl ; expression2; expression3 ) ) ; do
			commands
done
```

- expression1, expression2, expression]는 모두 식이고, commands 는 루프의 각 반복마다 실행되는 명령들이다.

### 위와 동일한 동작 구조

```bash
(( expressionl ))
while (( expression2 )); do
					commands
					( ( expression3 ) )
done
```

- expression1은 루프를 위한 초기 상태이고, expression2는 루프가 끝나는 시점을 결정하는데 사용된다. 그리고 expression3은 루프의 각 반복 끝 부분에서 실행된다.

### 예제

```bash
#!/bin/bash
# simple_counter : demo of C style for command
for ( ( i=0; i <S; i=i+l ) ) ; do
					echo $i
done
```

**실행결과**

```bash
[me@linuxbox ~]$ simple_counter
0
1
2
3
4
```

- expression1에서는 변수 i를 0으로 초기화하고, expression2는 i가 5보다 작은 경우에만 루프를 허용한다. 그리고 expression3는 루프가 반복될 때마다 i의 값을 1씩 더한다.

## 3. 마무리

기존 스크립트 for명령으로 변환 

### 기존 report_home_space 함수

```bash
report_home_space () {
				if [[ $(id -u) -eq 0 ]]; then
								cat « - _EOF_
												<H2>Home Space Utilization (All Users) </H2>
												<PRE >$( du -sh / home /*)</PRE>
												_EOF_
				else
								cat « - _EOF_
												<H2 >Home Space Utilization ($USER) </H2 >
												< PRE >$(du -sh $HOME) </ PRE >
												_EOF_
				fi
				return
}
```

### for 명령어로 재작성

```bash
report_home_space () {

			local format="%8s%10s%10s\ n"
			local i dir_list total_files total_dirs total_size user_name
			if [[ $(id -u) -eq 0 )]; then
			dir_list=/ home /*
			user_name="All Users "
			else
			dir_list=$HOME
			user_name=$USER fi
			echo "<H2>Home Space Utilization ($user nam </ H2>"
			for i in $dir_list; do
						total_files=$(find $i -type f I we -1)
						total_dirs=$(find $i -type d I we -1)
						total_size=$(du -sh $i I cut -f 1)
						echo "<H3 >$i</ H3 >"
						echo "<PRE>"
						printf "$format" "Dirs" "Files" "Size"
						printf "$format" "----" "-----" "----"
						printf "$format" $total_dirs $total_files $total_size
						echo "</ PRE >"
			done
			return 
}
```

- 각 사용자 홈 디렉토리에 대한 자세한 정보와 파일 및 하위 디렉토리 전부를 포함하게끔 이 스크립트를 다시 작성한 것이다.
- if 문에서 완전한 동작을 수행하는 대신에 for 루프에서 추후 사용될 변수들을 설정하고, 또한 여러 지역 변수들을 함수에 추가하고 printf를 사용하여 출력의 일부를 포맷했다.

# 우분투 리눅스 7. 서버 시스템

## 1. 서버 시스템이란

### 서버 시스템이란

서버란 클라이언트의 반대편에 서 있는 컴퓨터를 가리킨다. 즉 서비스를 제공하는 컴퓨터를 서버라고 말하고 서비스를 제공받는 서비스를 클라이언트라고 한다. 

서버는 하드웨어측면과 소프트웨어 측면으로 나눌 수가 있는데 대부분의 서버라고 하면 서버 기능을 하는 소프트웨어를 실행하고 잇는 컴퓨터가 된다. 서버 기능을 수행하는 소프트웨어는 많은 종류가 있다. 

| 서버 종류 | 역할 |
| --- | --- |
| 웹 서버 | 웹 페이지를제공하기 위한다양한지원 |
| 파일 서버 | 파일을 분류, 저장하고 검색 및 다운로드 지원 |
| 메일 서버 | 이메일 전송, 수신 및 저장을 지원 |
| DNS 서버 | 도메인 이름을 IP와 연결 지원 |
| 네트워크 서버 | 각 네트워크 관련 프로토콜 지원 |
| 데이터베이스 서버 | 오라클, MySQL 등의 데이터베이스 지원 |
| SSH 서버 | 암호처리 된 원격접속 지원 |
| Telnet 서버 | 원격접속 지원 |
| FTP 서버 | 파일 전송기능을 지원 |
| NFS 서버 | 파일 연동을 위한 서버 |
| 기타  | 프린터서버, 게임서버 등의 다양한 서버 존재 |

### 1) 웹서버 설치하기

LAMP (Linux, Apache, MySQL, PHP) 란 리눅스 시스템 에서 웹 페이지를 만들어 서비스 할 수 있는 홈페이지 지원 프로그램 패키지이다.

**LAMP 설치하기** 

```bash
# apt-get isntall phpmyadmin mysql-clinent mysql-server php5-common apache2 php5-mysql
```

⇒ Ubuntu의 apt-get 명령어로 파일을 다운받고 설치함

**“~(틸트)”로 사용자별 홈페이지에 접속하기**

아파치 서버에는 각 사용자들이 외부에 공개하고자 하는 html 파일을 저장하기 위한 용도로 각 사용자계정 홈 디렉터리 표시인 “~(틸트)”를 이용해서 접속할 수 있다. 이런 역할을 하는 디렉터리는 아파치 설정파일에 “UserDir” 항목으로 적어주면 된다.

다음 명령들을 차례로 수행한다.

```bash
# cd /etc/apache2/mods-enabled 
# In -s /etc/apache2/mods-available/userdir.load . 
# In -s /etc/apache2/mods-available/userdir.conf .
```

etc/apache2/mods- enabled/userd[ir.co](http://ir.co/)nf" 파일을 확인한다. 특별한 편집을 추가하지 않았다면 두 번째 줄에 "UserDir’' 항목이 존재한다. （기본 값 : publicJitmi)

```bash
# vi /etc/apache2/mods-enabled/userdir.conf
```

**아파치 서비스를 다시 시작하기**

```bash
# /etc/init.d/apache2 restart
```

**웹서비스 확인하기** 

```bash
$ mkdir public_html
$ cd ~/public_html
$ cd /var/www/index.html .
```

⇒ 웹서비스를 볼 수 있도록 페이지 제작까지 완성 ⇒ IP 확인하기

### 2) FTP 서버 설치하기

FTP서버 (File Transfer Protoco)는 파일 전송 프로토콜을 지원하는 서버이다

**FTP 서버 설치하기**

```bash
#apt-get install vsftpd
```

FTP 서버 설치가 성공되었고 서비스가 시작된다. 

웹 서비스 테스트와 동일한 방법으로 동일 도메인 네트워크의 다른 컴퓨터인 윈도우즈에서 ALFTP 를 설치하여 테스트하여 본다. 

### **3) NFS 서버 구축 및 운영**

NFS는 네트워크상의 다른 사용자 디렉터리의 일을 공유할 수 있도록 시스템을 구성 한다. NFS를 사용하는 것으로, 사용자와 프로그램은 원격지 컴퓨터의 파일을 자신의 컴퓨터에 있는파일을 사용하는것처럼 쉽게 접근할수 있다. 

**NFS가 제공하는가장 주목할 만한 특징**

1. 공통적으로 사용되는 데이터가 단일 시스템에 저장되고 네트워크상의 다른 컴퓨터에 접근할수 있기  때문에 저장 공간을 절약할 수 있다.
2. 사용자가 모든 네트워크 에 응하는 각각의 홈 디렉터리를 가질 필요가 없다
3. 홈 디렉터리를 NFS 서버 상에 만들 수 있고 네트워크롤 통하여 접근할 수 있다.
4. 플로피디스크, CDROM 드라이브, 그리고 USB 이브와 같은 저장 장치들도 네트워크 상의 다른 컴퓨터에서 사용될 수 있다. 이는 네트워크 전체의 착탈식 미디어 드라이브의 숫자를 줄일 수도있다

### **NFS(Network File System) 설치하기**

```bash
#sudo apt-get install nfs-kernel-server nfs-common portmap
```

**portmap 설정**

```bash
#sudo vi /etc/default/portmap
```

직접 편집을 하여야 하지만, 다음 명령은 portmap 을 일괄 설정한다

```bash
#sudo dpkg-reconfigure portmap
```

**portmap 서비스 재시작**

```bash
#sudo /etc/init.d/portmap restart
```

### **NFS 설정**

**NFS 서버 시작**

```bash
# sudo /etc/init.d/nfs-kernel-server start
```

**다른 컴퓨터에서 공유된 NFS 디렉터리 마운트**

```bash
# sudo mount example.hostname.com:/ubuntu /local/ubuntu
```

위 명령문에서 제시된 마운트 위치 디렉터리 "/locaVubuntu" 는 반드시 있어야 한다.
"/locaVubuntu'' 디렉터리 내에 는 다론 파일 또는 서브디렉토리가 없도독 한다.

## 4) 인터넷 익스플**로러 사용하기**

**인터넷 익스플로러 설치** 

```bash
# wget -q http://wine.budgetdedicated.com/apt/387EE263.gpg -O- | apt-key add -
# wget http://www.tatanka.com.br/ies4linux/downloads/ies4linux-latest.tar.gz
```

**''budgetdedicated" 를 "apt-key” 에 추가하고 "ies/linux-lates.tar.gaz 를 다운로드 받는다**

```bash
# apt-get update
# apt-get install wine cabextract
```

```bash
# tar zxvf ies4linux-latest.tar.gz
```

**압축된 아카이브 파일을 현재 디렉터리에 압축까지 같이 해제한다**

```bash
# cd ies4linu-2.99.0.1
# ./ies4linux
```

**폰트문제 해결을 위해 와인의 폰트와 연동**

```bash
In -s -/.wine/drive_c/windows/Fonts -/.ies4linux/ie6/drive_c/windows/Fonts
```

**ies4linux를 다시 실행하여 설치를 진행**

```bash
# cd ./ies4linux-2.99.0.1 
# ./ies31inux
```

**터미널 창에서 홈 디렉터리로 이동하고 익스플로러 실행**

```bash
# ~/bin/ie6
```

root 계정에서 실행하는 경우는 반드시 “xhost +” 명령을 실행한 후에 익스플로러를 실행하여아 함 

## 2. Oracle(오라클)

### 1) 오라클 설치준비하기

root로 로그인하기

버전 확인 

```bash
# uname -r
```

현재 설치되어 있는 모든 패키지를 수정 확인하고 버전을 업그레이드

```bash
# apt-get update
# apt-get upgrade
```

→ vmware에서 단독 운영체제로 Ubuntu를 설치했다면 grup을 추가적으로 설치

오라클에 필요한 추가 패키지 일괄 설치

```bash
 # apt-get install elfutils libaio1 libaio-dev libstdc++6-4.3dev sysstat lesstif2 lesstif2-dev build-essential rpm original-awk ksh alien

```

패키지 설치 확인

```bash
apt-cache showpkg binutils | more
```

필요한 패키지 목록

```bash
elfutils 
libaio1 
libaio-dev 
libstdc++6-4.3-dev 
sysstat 
lesstif2 
lesstif2-dev 
build-essential 
rpm 
original-awk 
ksh 
alien
```

오라클에서 사용자 그룹 및 사용자 추가

```bash
# addgroup dba
```

```bash
# addgroup oinstall
```

```bash
# addgroup nobody
```

```bash
# useradd -m oracle -g oinstall -G dba -s/bin/bash
```

```bash
# useradd -g nobody nobody
```

오라클 설치를 위한 디렉터리를 만들고 접근모드 변경

```bash
# mkdir /oracle 
# mkdir /oracle/11 g 
# chown -R oracle:oinstall /oracle 
# chmod -R 775 /oracle
```

오라클 파라미터 설정

```bash
# vi /etc/sysctl.conf
```

```bash
fs.file-max = 65535 
kernel.shmall = 20971 52 
kernel.shmmax = 2147483648 
kernel.shmmni = 4096 
kernel.sem = 250 32000 100 128 
net.ipv4.ip_localJ)ort_range = 1024 65000 
net.core.rmem_default = 1048576 
net.core.rmem_max = 1048576 
net.core.wmem_default = 262144 
net.core.wmem_max = 262144
```

시스템 다시 시작 후 오라클로 로그인

그놈 (GNOME) 윈도우는 오라클로 로그인음 하고 Putty는 root 로 로그인음 하여 작업을 한다.
오라클 파라미터 설정 적용은 다음 명명으로 수행한다.

```bash
# sysctl -a 2> error.log | grep shmmax
```

/ect/sysctl.conf 적용

```bash
# sysctl -p
```

사용자계정 쉘 권한 설정을 /etc/security/limits.conf 파일의 마지막 줄 다음에 추가

```bash
# vi /etc/security/limits.conf
```

```bash
oracle soft nproc 2047 
oracle hard nproc 16383 
oracle soft nofile 1023 
oracle hard nofile 65535
```

''/etc/pam.d/login" 파일의 마지막 줄 다음에 추가

```bash
# vi /etc/pam.d/login
```

```bash
session required /lib/security/pam_limits.so 
session required pam imits.so
```

디렉터리 심볼릭 링크가 다른 위치에 존재하기 때문예 "dpkg —S 패키지명을 이용하여 위지를 알아본다.

```bash
# ln -s /usr/bin/original-awk /bin/awk
# ln -s /usr/lib/rpm /bin/rpm
# ln -s /lib/libgcc_s.so.1 /lib/libgcc_s.so
# ln -s /usr/bin/basename /bin/basename
```

오류가 나오더라도 정상적인 수행이 가능하게끔 rpm 권한 주기

```bash
# chmod ago+w /usr/lib/rpm/*
# chmod ago+w /usr/lib/rpm/.
```

### 2) 환경변수 설정

```bash
# vi /etc/profile
```

```bash
export ORACLE_OWNER=oracle 
export ORACLE_BASE=/oracle 
export ORACLE_HOME=/oracle/11 g 
export ORACLE_S1D=orcl 
export PATH=$PATH:$0RACLE_HOME/bin
```

다운로드한 오라클 압축파일을 /home/oracle로 옮긴 다음 압축을 해제한다.

```bash
# mv 다운로드/linux_11gR1_database_1013.zip /home/oracle
$ unzip linux_11gR1_database_1013.zip
```

./database 의 모든 파일과 하위 디렉터리 및 파일의 소유자를 oracle-oinstall로 지정한다

```bash
# chown -R oracle:oinstall ./database
```

만약 우분투 서버를 설치하엿다면 다음과 같이 데스크톱 환경을 설치 

```bash
# apt-get install ubuntu-desktop
```

### 3) 설치 진행

오라클 설치는 “X-window” 에서 시작하여야 한다

Ubuntu의 GNOME 환경에서 oracle 계정으로 로그인하여 터미널 창을 실행하고 설치작업을 진행

./database/runinstaller 실행

```bash
$ export LANG=C
$ ./database/runInstaller
```

한글이 표시되지 않으므로 "export LANG=C" 명령음 입력하여 영문전용으로 언어 환경을 바꿈

### 4) 데이터베이스 서버 자동 시작

"／etc/oratab" 파일을 열어 다음과 같이 수정한다. 

```bash
$ vi /etc/oratab
```

“/etc/init.d/oracle” 을 생성하여 다음과 같이 입력한다

```bash
$ vi /etc/init.d/oracle
```

```bash
# ! /bin/bash 
ORA_HOME="/oracle/11 g" 
ORA_OWNER="oracle" 
if [ ! -f $0RA_HOME/bin/dbstart-o ! -d $0RA_HOME ] 
then 
		echo "Oracle Startup: failed" 
		exit 1 
fi 
case "$1 " in 
		start) 
				echo -n "Oracle Start: " 
				su - $0RA_OWNER -c "$0RA_HOME/bin/lsnrctl start" 
				SU - $0RA_OWNER -c $0RA_HOME/bin/dbstart 
				touch /var/lock/subsys/oracle 
				echo "OK"
				;;
		stop) 
				echo -n "ORACLE Shutdown: " 
				su - $0RA_OWNER -c "$0RA_HOME/bin/lsnrctl stop" 
				su - $0RA_OWNER -c $0RA_HOME/bin/dbshut 
				rm /var/lock/subsys/oracle 
				echo "OK" 
				;;
		restart) 
					$0 stop 
					$0 start
			;;
		*) 
					echo "Usage: $0 startistoplrestart" 
					exit 1
esac 
exitO 

```

스크립트 파일의 모드를 755로 조정

```bash
# chmod 755 /etc/intit.d/oracle
```

환경변수 

```bash
# vi $ORACLE_HOME/bin/dbstart
# vi $ORACLE_HOME/bin/dbshut
```

ORACLE_HOME_LISTENER=$1 으로 되어있는 내용을 ORACLE_HOME_LISTENER=$ORACLE_HOME으로 수정

환경검사 명령어인 ckconfig설치

```bash
# apt-get install chkconfig
```

설치가 자동으로 완료된다

```bash
# chkconfig -add oracle
```

오라클 환경검사 레벨을 3으로 설정

```bash
# chkconfig -level 3 oracle on
```

오라클 계정으로 돌아와서 데이터베이스 시작

```bash
$ /etc/init.d/oracle start
```

### 5) 오라클 사용하기

```bash
# /orcale/11g/bin/dbstart ORACLE_HOME
```

오라클 데이터베이스를 시작하고 리스너 컨트롤 시작, sqlplus 실행

```bash
$ lnsrctl start
$ sqlplus /nolog
```