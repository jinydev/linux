---
layout: home
---

# Nginx 톰켓 연동 (AJP)
웹서버인 Nginx와 WAS인 톰켓을 연동합니다.

## nginx-ajp-module
nginx에서 AJP 프로토콜을 사용하기 위해서는 nginx용 AJP 모듈을 사용해야합니다. 
> mod_jk 모듈은 Apache 웹 서버에서 AJP 연동을 위해 사용되는 모듈입니다.

```
sudo apt install libnginx-mod-jk
```

libnginx-mod-jk 패키지는 Ubuntu 공식 패키지 저장소에는 포함되어 있지 않을 수 있습니다. 대신에, ppa:ondrej/nginx 저장소를 추가하고 nginx-full 패키지를 설치한 후에, libapache2-mod-jk 패키지를 설치하여 Nginx와 Apache Tomcat을 AJP 프로토콜로 연결할 수 있습니다.

ppa:ondrej/nginx 저장소 추가

```
sudo add-apt-repository ppa:ondrej/nginx
sudo apt update
```

nginx-full 패키지 설치
```
sudo apt install nginx-full
```

libapache2-mod-jk 패키지 설치
```
sudo apt install libapache2-mod-jk
```

libapache2-mod-jk를 이용하여 Nginx와 Tomcat을 AJP 프로토콜로 연결
/etc/apache2/mods-available/jk.conf 파일에 다음과 같이 설정을 추가합니다.

```
<IfModule mod_jk.c>
    JkWorkersFile /etc/libapache2-mod-jk/workers.properties
    JkLogFile /var/log/apache2/mod_jk.log
    JkLogLevel info
    JkLogStampFormat "[%a %b %d %H:%M:%S %Y]"
</IfModule>
```

그리고 /etc/apache2/mods-available/jk.load 파일을 만들고 다음과 같이 설정을 추가합니다.

```
LoadModule jk_module /usr/lib/apache2/modules/mod_jk.so
```

/etc/libapache2-mod-jk/workers.properties 파일을 생성하고 다음과 같이 설정을 추가합니다.

```
worker.list=tomcat
worker.tomcat.type=ajp13
worker.tomcat.host=localhost
worker.tomcat.port=8009
```


## Nginx 설정
Nginx에서 AJP 모듈 활성화 합니다.
/etc/nginx/nginx.conf 파일을 엽니다.
http 블록 안에 있는 server 블록을 찾습니다.
location 블록 안에 proxy_pass를 다음과 같이 추가합니다.

```
http {
    ...
    upstream tomcat {
        server 127.0.0.1:8009;
    }
    server {
        listen 80;
        server_name example.com;

        location / {
            proxy_pass http://tomcat;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
    ...
}
```

nginx를 재시작합니다.
```bash
sudo service nginx restart
```


## Tomcat에서 AJP 연결 활성화
Tomcat 설치 경로의 conf/server.xml 파일을 엽니다.
```
sudo vi /etc/tomcat9/server.xml
```

<Connector> 엘리먼트를 찾습니다.
protocol 속성을 "AJP/1.3"으로 설정합니다.
port 속성을 8009로 설정합니다.
redirectPort 속성을 8443로 설정합니다.

```xml
<Connector protocol="AJP/1.3" address="0.0.0.0" port="8009" redirectPort="8443" packetsize="65536" secretRequired="false"/>
```

<Connector> 엘리먼트를 저장하고 파일을 닫습니다.

톰켓을 재시작합니다.

```bash
sudo systemctl restart tomcat9 
```


