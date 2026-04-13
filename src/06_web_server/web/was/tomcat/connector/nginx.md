---
layout: home
typora-copy-images-to: ./img
---

# nginx 톰켓 연동
Ubuntu에서 Nginx와 Tomcat을 연동을 합니다. `Nginx`는 정적 페이지를 처리하고, Tomcat 은 동적 페이지를 처리한다. 이러한 역할 배분을 통해 더 빠른 응답을 기대할 수 있다.

## Nginx의 장점
* Apache와 달리 구성 시스템이 없어 빠른 속도
* Request 에 대해 Event-Driven 방식으로 동작
* 정적 파일에 대해 Apache 요청의 2배량을 제공
* 2019년 4월 기준 Apache 사용량 추월

## Nginx 및 Tomcat 설치
먼저 Nginx와 Tomcat을 설치해야 합니다. 다음 명령을 사용하여 Nginx 및 Tomcat을 설치할 수 있습니다.

```bash
sudo apt-get update
sudo apt-get install nginx
sudo apt-get install tomcat9
```

## 톰캣 구성
다음으로 특정 포트에서 실행되도록 Tomcat을 `구성`해야 합니다. 

### 포트변경
기본적으로 Tomcat은 포트 `8080`에서 실행됩니다. 이 포트를 변경하려면 텍스트 편집기를 사용하여 `/etc/tomcat9/server.xml` 파일을 열고 다음 행을 찾으십시오.


```bash
<Connector port="8080" protocol="HTTP/1.1"
```

포트 번호를 원하는 포트로 변경합니다. 예를 들면 다음과 같습니다.

```bash
<Connector port="8081" protocol="HTTP/1.1"
```

파일을 저장하고 종료합니다.


### Nginx 구성
다음으로 요청을 Tomcat에 `프록시`하도록 Nginx를 구성해야 합니다. 텍스트 편집기를 사용하여 `/etc/nginx/sites-available/default` 파일을 열고 다음 줄을 추가합니다.


```bash
location / {
proxy_pass http://localhost:8081;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

파일을 저장하고 종료합니다.


### 구성 테스트

마지막으로 다음 명령을 사용하여 Nginx와 Tomcat을 모두 다시 시작하여 구성을 테스트할 수 있습니다.


```bash
sudo systemctl restart nginx
sudo systemctl restart tomcat9
```

두 서비스를 모두 다시 시작한 후 웹 브라우저에서 http://localhost를 방문하여 Nginx를 통해 Tomcat 웹 애플리케이션에 액세스할 수 있어야 합니다.