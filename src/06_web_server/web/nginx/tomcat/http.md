---
layout: home
---

# Nginx 톰켓 연동(Http)
웹서버인 Nginx와 WAS인 톰켓을 연동합니다.

## 준비작업
가상머신 2대를 준비하여 각각에 nginx와 tomcat을 별도로 설치한 후에 서로 vm을 연동합니다.

vm간 서로 통신을 하기 위하여 추가 네트워크 어뎁터를 선택하고, 연결 방식을 `내부 내트웍`으로 선택합니다.

vm에서 수동으로 ip를 변경합니다. 사설 아이피 `192.168.1.xx`로 설정합니다. 내부 통신이기 때문에 게이트웨이는 설정하지 않습니다.


## HTTP 프로토콜을 이용한 연동
* Nginx 설정을 변경합니다.

```bash
sudo vi /etc/nginx/site-available/default
```

`server`블럭을 찾아서 `location`안에 `proxy_pass`를 설정합니다.
```
location / {
  proxy_pass http://192.168.1.20:8080;
}
```
> 가상머신에서 8080 포트로 통신이 가능하도록 `포트포워딩`을 허용합니다.

nginx를 재시작합니다.
```bash
sudo service nginx restart
```

* tomcat9 설정파트

`/etc/tomcat9/server.xml` 파일을 수정합니다.

`<Connector>` 엘리먼트를 찾습니다. protocol 속성을 "HTTP/1.1"로 설정합니다.
수정하면 다음과 같습니다.
```xml
<Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
```

톰켓을 재시작합니다.

```bash
sudo systemctl restart tomcat9 
```

* 결과 확인
localhost로 접속을 합니다. 결과 페이지가 nginx가 아닌 톰켓 화면이 나오면 성공입니다.


