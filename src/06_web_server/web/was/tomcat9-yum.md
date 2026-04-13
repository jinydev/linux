---
layout: home
---

# Rocky에서 Tomcat9 설치하기
Rocky9에서 Tomcat 9를 설치합니다.

## 수동 설치 방법

Tomcat 9 바이너리 파일을 다운로드 받습니다.
```
sudo curl -O https://downloads.apache.org/tomcat/tomcat-9/v9.0.74/bin/apache-tomcat-9.0.74.tar.gz
```

압축을 풉니다.
```
sudo tar xzf apache-tomcat-9.0.74.tar.gz -C /usr/share/
```

디렉토리 이름을 변경합니다.
```
sudo mv /usr/share/apache-tomcat-9.0.74 /usr/share/tomcat9
```

Tomcat 사용자를 추가합니다.
```
sudo useradd -r tomcat
```

소유자를 변경합니다.
```
sudo chown -R tomcat: /usr/share/tomcat9/
```

Tomcat 서비스 파일을 생성합니다.
```
sudo vi /etc/systemd/system/tomcat.service
```
서비스 파일에 다음 내용을 입력하고 저장합니다.

```
[Unit]
Description=Apache Tomcat 9 Servlet Container
After=syslog.target network.target

[Service]
Type=forking

Environment=JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64/jre
Environment=CATALINA_PID=/usr/share/tomcat9/temp/tomcat.pid
Environment=CATALINA_HOME=/usr/share/tomcat9/
Environment=CATALINA_BASE=/usr/share/tomcat9/
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'

ExecStart=/usr/share/tomcat9/bin/startup.sh
ExecStop=/usr/share/tomcat9/bin/shutdown.sh

User=tomcat
Group=tomcat
UMask=0007
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```


## JAVA_HOME 변경
Java 11 OpenJDK를 설치한 경우, 다음 명령어를 사용하여 JAVA_HOME 환경 변수의 경로를 확인할 수 있습니다.

```
echo $JAVA_HOME
```

만약 JAVA_HOME 환경 변수가 설정되어 있지 않다면, 다음 명령어를 사용하여 JAVA_HOME 환경 변수를 설정할 수 있습니다.

```
sudo update-alternatives --config java
```

위 명령어를 실행하면 다른 버전의 자바도 설치되어 있다면 선택할 수 있는 목록이 나타납니다. 여기서 원하는 버전을 선택하면 해당 버전의 JAVA_HOME 경로가 자동으로 설정됩니다. 설정이 완료되면 다시 echo $JAVA_HOME 명령어를 사용하여 경로가 제대로 설정되었는지 확인할 수 있습니다.

```
[poly@localhost ~]$ sudo update-alternatives --config java

There is 1 program that provides 'java'.

  Selection    Command
-----------------------------------------------
*+ 1           java-11-openjdk.x86_64 (/usr/lib/jvm/java-11-openjdk-11.0.19.0.7-1.el9_1.x86_64/bin/java)

Enter to keep the current selection[+], or type selection number: 1
```
위 명령어를 실행하면 설치된 자바 버전 리스트가 나타나며 현재 선택된 자바 버전은 *+ 표시로 표시됩니다. 선택할 자바 버전 번호를 입력하면 해당 버전이 자동으로 java_home에 설정됩니다. 위 예제에서는 java-11-openjdk.x86_64 버전이 현재 선택되어 있습니다.

```
[poly@localhost ~]$ echo $JAVA_HOME

[poly@localhost ~]$
```
echo $JAVA_HOME 명령어를 실행했을 때 아무런 값도 출력되지 않는다면, JAVA_HOME 환경변수가 설정되어 있지 않은 것입니다.

JAVA_HOME 환경변수를 설정해야 합니다. 다음과 같이 명령어를 입력하여 설정할 수 있습니다.

```
sudo vi /etc/profile.d/java.sh
```

vi 에디터가 열리면, 다음과 같이 입력하여 JAVA_HOME 환경변수를 설정합니다.

```
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.19.0.7-1.el9_1.x86_64
export PATH=$JAVA_HOME/bin:$PATH
```
저장하고 vi 에디터를 종료한 후에 다음 명령어로 변경된 환경변수를 적용합니다.

```
source /etc/profile.d/java.sh
```

다시 echo $JAVA_HOME 명령어를 실행하여 JAVA_HOME 환경변수가 정상적으로 설정되었는지 확인할 수 있습니다.


tomcat.service를 수정합니다.
```
sudo vi /etc/systemd/system/tomcat.service
```
tomcat.service 파일을 수정하여 JAVA_HOME 환경 변수를 올바르게 설정해야 합니다. 다음과 같이 파일을 수정할 수 있습니다.
```
Environment=JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.19.0.7-1.el9_1.x86_64
```

파일을 저장하고 종료합니다.

다음 명령어를 입력하여 systemd에 변경된 설정을 적용합니다.

```
sudo systemctl daemon-reload
```

서비스를 등록하고 시작합니다.

```
sudo systemctl start tomcat
sudo systemctl enable tomcat
```

## 방화벽
Tomcat의 기본 포트는 8080이므로 방화벽에서 8080 포트를 열어주어야 합니다. 방화벽 구성을 확인하려면 다음 명령어를 실행하십시오.

```
sudo firewall-cmd --list-all
```

방화벽에 8080 포트가 열려 있지 않은 경우 다음 명령어를 실행하여 방화벽에 8080 포트를 추가할 수 있습니다.

```
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
```

이제 Tomcat 9.0.74이 설치되었으며 http://localhost:8080로 접속하여 확인할 수 있습니다.


## Nginx와 연동
nginx와 Tomcat을 연동하려면 nginx의 설정 파일에 Tomcat으로 전달할 요청을 정의해야 합니다.

다음은 nginx와 Tomcat을 연동하기 위한 예시 설정 파일입니다. 아래 설정을 nginx의 설정 파일(/etc/nginx/nginx.conf)에 추가하시면 됩니다.

```
http {
    upstream tomcat {
        server 192.168.56.110:8080;
        keepalive 32;
    }

    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; 
            proxy_set_header Host $http_host;
            proxy_set_header X-NginX-Proxy true;

            proxy_pass http://tomcat/;
            proxy_redirect off;
        }
    }
}
```

위 설정 파일에서, upstream 블록은 nginx가 Tomcat으로 전달할 요청을 정의합니다. server 블록은 요청을 받을 포트와 서버 이름을 지정하고, location 블록은 요청이 들어왔을 때 Tomcat으로 전달할 설정을 정의합니다.

위 설정 파일에서는 /로 들어온 요청이 모두 Tomcat으로 전달되도록 설정하였습니다. 이 설정을 변경하여 필요한 요청만 Tomcat으로 전달되도록 수정할 수 있습니다.

설정 파일을 변경한 후에는 nginx를 재시작하여 변경 사항을 적용하시면 됩니다.

```
sudo systemctl restart nginx
```

이후 http://192.168.56.100으로 접속하여 Tomcat과 nginx가 정상적으로 연동되었는지 확인하시면 됩니다.