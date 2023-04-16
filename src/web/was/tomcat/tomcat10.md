---
layout: home
typora-copy-images-to: ./img
---

# Tomcat10 설치



## 톰켓 설치
Apache Tomcat 또는 Tomcat은 널리 알려지고 사용되는 Java 애플리케이션 서버입니다. Apache Software Foundation의 개발자 커뮤니티에서 개발 및 유지 관리하는 오픈 소스 웹 서버 및 서블릿 컨테이너입니다. 

Ubuntu 리포지토리에서 Tomcat을 설치하는 대신 바이너리 배포 파일을 사용하여 Tomcat 10을 설치합니다. 먼저 Tomcat 바이너리 배포 파일을 다운로드해야 합니다. [최신 버전을 확인하려면 https://tomcat.apache.org/download-10.cgi](https://tomcat.apache.org/download-10.cgi) 의 다운로드 페이지로 이동하세요.
> Tomcat 10을 사용하려면 시스템에 JRE 8 이상의 버전이 설치되어 있어야 합니다. 


### 다운로드
`wget` 명령을 통하여 최신의 톰켓 10.1 버젼을 다운로드 합니다.

```bash
hojin@hojin3:~$ wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.7/bin/apache-tomcat-10.1.7.tar.gz -O /tmp/tomcat-10.tar.gz

hojin@hojin3:~$ ls /tmp/tomcat-10.tar.gz
/tmp/tomcat-10.tar.gz
```

다운로드 파일을 압축을 해제 합니다.

```bash
hojin@hojin3:~$ sudo -u tomcat tar -xzvf /tmp/tomcat-10.tar.gz  --strip-components=1 -C /opt/tomcat
```

위 명령어로 `/opt/tomcat`에 바이너리 배포 파일이 다운로드 및 추출되고 파일/디렉토리는 사용자 `tomcat`이 소유합니다.


### tomcat 시스템 사용자 생성

보안상의 이유로 사용자 `root`로 Tomcat을 실행하는 것은 권장되지 않으므로 Tomcat을 실행할 새 시스템 사용자를 생성합니다.


```bash
hojin@hojin3:~$ sudo useradd -m -d /opt/tomcat -U -s /bin/false tomcat
```

위의 명령을 실행하면 `/opt/tomcat` 디렉토리가 자동으로 생성됩니다.


```bash
hojin@hojin3:~$ ls /opt/
tomcat
```


### tomcat Service 등록
`service` 명령으로 톰켓을 실행할 수 있도록 스크립트를 생성합니다. 

`/etc/init.d/` 디렉토리에 tomcat 파일을 생성합니다.
```
sudo nano /etc/init.d/tomcat
```

다음과 같이 스크립트 내용을 작성합니다.

```
#!/bin/bash

### BEGIN INIT INFO
# Provides:    tomcat
# Required-Start:  $remote_fs $syslog
# Required-Stop:   $remote_fs $syslog
# Default-Start:   2 3 4 5
# Default-Stop:    0 1 6
# Short-Description: auto start Tomcat server
# Description: start web server
### END INIT INFO

case $1 in
start)
sh /톰캣위치/bin/startup.sh
;;
stop)
sh /톰캣위치/bin/shutdown.sh
;;
restart)
sh /톰캣위치/bin/shutdown.sh
sleep 2
sh /톰캣위치/bin/startup.sh
;;
esac
exit 0
```

파일의 권한을 바꾼다.

```bash
sudo chmod 755 /etc/init.d/tomcat
```
 

서비스를 업데이트 한다.
```bash
sudo update-rc.d tomcat defaults
```
 

서비스를 시작하여 본다.
```
service tomcat start
```
 

잘 동작하는지 상태를 확인하여 본다.
```
service tomcat status
```


### systemctl 등록방법
Tomcat 서비스를 관리하려면 systemd 서비스 파일을 만들어야 합니다.

```bash
sudo nano /etc/systemd/system/tomcat.service
```



다음 내용을 삽입합니다.

```
[Unit]
Description=Apache Tomcat
After=network.target

[Service]
Type=forking

User=tomcat
Group=tomcat

Environment=JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
Environment=CATALINA_PID=/opt/tomcat/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment="CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC"

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

ExecReload=/bin/kill $MAINPID
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```



파일을 저장하고 종료합니다.

다음 명령을 실행하여 systemd 관리자 구성을 다시 로드합니다.



```
systemctl daemon-reload
```

지금 Tomcat을 실행하고 재부팅 시 서비스를 실행하려면 다음 명령을 실행할 수 있습니다.



```
# systemctl enable --now tomcat
```

다음 명령을 실행하여 Tomcat 서비스를 확인하고 확인할 수 있습니다.



```
# systemctl status tomcat
```

It will show you an output like this:

As you can see, Tomcat is now running and listening on its default port 8080. You can open your web browser and navigate to http://YOUR_SERVER_IP_ADDRESS:8080







```bash
sudo apt-cache search tomcat
sudo apt install tomcat9 tomcat9-admin
```

설치된 tomcat 버젼 확인
```
hojin@hojin3:~$ /usr/share/tomcat9/bin/version.sh
Using CATALINA_BASE:   /usr/share/tomcat9
Using CATALINA_HOME:   /usr/share/tomcat9
Using CATALINA_TMPDIR: /usr/share/tomcat9/temp
Using JRE_HOME:        /usr
Using CLASSPATH:       /usr/share/tomcat9/bin/bootstrap.jar:/usr/share/tomcat9/bin/tomcat-juli.jar
Using CATALINA_OPTS:
NOTE: Picked up JDK_JAVA_OPTIONS:  --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.util.concurrent=ALL-UNNAMED --add-opens=java.rmi/sun.rmi.transport=ALL-UNNAMED
Server version: Apache Tomcat/9.0.58 (Ubuntu)
Server built:   Jan 6 1970 15:09:28 UTC
Server number:  9.0.58.0
OS Name:        Linux
OS Version:     5.15.90.1-microsoft-standard-WSL2
Architecture:   amd64
JVM Version:    11.0.18+10-post-Ubuntu-0ubuntu122.04
JVM Vendor:     Ubuntu
```

### 방화벽 및 포트 허용

포트확인
```
ss -ltn
```

```
sudo ufw allow from any to any port 8080 proto tcp
```

### 접속 테스트

`localhost:8080`으로 접속을 하여 톰켓 기본 페이지가 출력이 되는지 확인해 봅니다.

