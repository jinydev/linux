---
layout: home
---

# 아파치 웹서버
아파치 웹서버는 가장 대중적인 오픈 소스 웹서버로, HTML 문서 및 웹 페이지를 제공하는 소프트웨어입니다.  







## 환경설정

아파치 웹서버 운영을 위한 환경 설정 방법에 대해서 알아 봅니다.

* [가상호스트](vhost)



# 아파치 웹서버

## 아파치란?
아파치 HTTP 서버는 아파치 소프트웨어 재단에서 관리하는 오픈 소스, 크로스 플랫폼 HTTP 웹 서버 소프트웨어다. BSD, 리눅스 등 유닉스 계열 뿐 아니라 마이크로소프트 윈도우나 노벨 넷웨어 같은 기종에서도 무료로 운용할 수 있다



## 아파치 설치
패키지를 통하여 아파치 웹서버를 손쉽게 설치 할 수 있습니다.
> 윈도우에 아파치 설치하기

### 우분투 apt 설치
우분투에서 apt 패키지 관리자를 통하여 아파치 v2.x를 설치합니다. 콘솔에서 다음과 같이 명령을 입력합니다.  

```bash
$sudo apt install apache2
```

명령을 실행하면 apt는 서버에서 최신의 아파치 버젼을 확인하여, 다운로드 설치를 진행합니다.

실행결과
```bash
hojin@hojin3:~$ sudo apt install apache2
[sudo] password for hojin:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  apache2-bin apache2-data apache2-utils bzip2 libapr1 libaprutil1 libaprutil1-dbd-sqlite3
  libaprutil1-ldap liblua5.3-0 mailcap mime-support ssl-cert
Suggested packages:
  apache2-doc apache2-suexec-pristine | apache2-suexec-custom www-browser bzip2-doc
The following NEW packages will be installed:
  apache2 apache2-bin apache2-data apache2-utils bzip2 libapr1 libaprutil1 libaprutil1-dbd-sqlite3
  libaprutil1-ldap liblua5.3-0 mailcap mime-support ssl-cert
0 upgraded, 13 newly installed, 0 to remove and 73 not upgraded.
Need to get 2138 kB of archives.
After this operation, 8505 kB of additional disk space will be used.
Do you want to continue? [Y/n]
```

### 설치 후 버전 확인
아파치가 정삭적으로 설치가 되었다면 다음과 같이 명령을 입력하여 버젼을 확인합니다.

```bash
hojin@hojin3:~$ apache2 -v
Server version: Apache/2.4.52 (Ubuntu)
Server built:   2023-03-08T17:32:01
```



### Apache 서비스 기동/멈춤
이제 설치한 아파치를 실행해 보도록 합니다.

#### 아파치 서버 실행

```bash
hojin@hojin3:~$ sudo service apache2 start
 * Starting Apache httpd web server apache2
```



#### 아파치 서버 정지

```bash
hojin@hojin3:~$ sudo service apache2 stop
 * Stopping Apache httpd web server apache2  
```


#### 아파치 서버 재시작

```bash
hojin@hojin3:~$ sudo service apache2 restart
 * Restarting Apache httpd web server apache2                 [ OK ]
```


## Apache 서비스 관리
시스템에 등록하여 서비스가 `가동`/`멈춤`/`상태` 를 확인 합니다.

```
$ systemctl restart apache2
$ systemctl enable apache2
$ systemctl status apache2
```

> wsl에서는 systemctl을 기본적으로 사용할 수 없어,  추가 설정을 해야 사용이 가능하다. 윈도우/리눅스 멀티부팅이 아니라 기본적으로 window를 main server로 사용하고 ubuntu의 service도 같이 사용하려면 윈도우 시작시 리눅스 서비스도 같이 실행해야 하기 때문에 systemctl 명령어 활성화가 필요하다 


## 웹 서버 동작 확인하기

브라우저 실행, 주소 창에 http://localhost/ 또는 http://127.0.0.1/ 입력합니다.

![image-20230324151841484](./img/image-20230324151841484.png)



서버 동작 확인, listen port 80을 확인 하여 정상 동작 확인

```bash
hojin@hojin3:~$ netstat -ntlp
(No info could be read for "-p": geteuid()=1000 but you should be root.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp6       0      0 :::80                   :::*                    LISTEN      -
```

![image-20230324152005975](./img/image-20230324152005975.png)



Apache server의 home directory 변경

```bash
$vi /etc/apache2/sites-available/000-default.conf
```





```ini
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>
```



Document Root 를 바꾸려고 하면 Permission 에러가 난다.

`/etc/apache2/apache2.conf`에서 `<Directory>`에 관한 설정을 변경

denied -> granted 로 변경

![image-20230324152340860](./img/image-20230324152340860.png)



## 방화벽 해제

외부에서 웹 서버에 접근할 수 있도록 ufw allow 80 명령으로 포트 허용.

​     ifconfig ens32 명령으로 가상머신의 IP 주소 확인



![image-20230324152427284](./img/image-20230324152427284.png)












