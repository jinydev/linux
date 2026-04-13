---
layout: home
---

# 리눅스 서버2대를 통하여 Nginx, Tomcat 연동하기
2대의 리눅스 서버를 준비합니다.

## Nginx 설치
1번 서버에 Nginx를 설치하기 위해 터미널에서 다음 명령어를 입력합니다.

```bash
sudo apt-get update
sudo apt-get install nginx
```

방화벽을 설정합니다.

```bash
sudo ufw allow 80/tcp
```

VirtualBox에서 네트워크 탭에서 Net설정의 포트 포워딩을 설정합니다.


## Tomcat 설치하기
2번 서버에 Tomcat을 설치하기 위해 터미널에서 다음 명령어를 입력합git pull니다.

자바 설치
```bash
sudo apt install default-jdk -y
```
> Ubuntu 22.04 Live Server에서는 기본적으로 default-jdk 패키지가 설치되어 있지 않습니다. 대신에 openjdk 패키지를 설치하여 JDK를 사용할 수 있습니다.

```bash
sudo apt-get install tomcat9
```

위 명령어를 실행하면 Tomcat 9가 설치됩니다. Tomcat을 시작하려면 다음 명령을 실행합니다.

```
sudo systemctl start tomcat9
```

Tomcat이 부팅 시 자동으로 시작하도록 하려면 다음 명령을 실행합니다.

```
sudo systemctl enable tomcat9
```

Tomcat이 정상적으로 실행되고 있는지 확인하려면 브라우저에서 http://localhost:8080을 엽니다. Tomcat 화면이 표시되면 설치가 성공적으로 완료된 것입니다.

* 방화벽 설정
Tomcat이 제대로 작동하려면 방화벽에서 포트 8080에 대한 액세스를 허용해야 합니다. 다음 명령어를 사용하여 방화벽에서 포트 8080을 엽니다.

```
sudo ufw allow 8080
```
위 명령어를 실행하면 방화벽에서/ㅅ체 8080 포트로의 액세스가 허용됩니다.


## Nginx와 Tomcat 연동하기

### Nginx 설정
nginx를 설치한 후에는 /etc/nginx/sites-available/ 디렉토리에 새로운 설정 파일을 생성합니다.
```
sudo nano /etc/nginx/sites-available/my-app
```

설정 파일에 다음과 같은 내용을 추가합니다. server_name에는 자신의 도메인이나 IP 주소를 입력합니다.

```
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://tomcat-server-ip:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

설정 파일을 저장하고 닫은 후, 심볼릭 링크를 생성합니다.

```
sudo ln -s /etc/nginx/sites-available/my-app /etc/nginx/sites-enabled/
```

### 톰켓 설치 및 설정

다음으로, 자바와 톰켓을 설치합니다.
```
sudo apt-get update
sudo apt-get install default-jdk tomcat9
```

Tomcat 구성 파일을 수정하기 위해 다음 명령을 실행합니다.

```
sudo nano /etc/tomcat9/server.xml
```

Connector 태그 내에 다음과 같은 설정을 추가합니다.

```
<Connector port="8080" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443"
           proxyName="your-domain.com"
           proxyPort="80" />
```
