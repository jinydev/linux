---
layout: home
typora-copy-images-to: ./img
---

# nginx 톰켓 연동
Nginx와 Tomcat 연동설정합니다.
> 참조: https://haengsin.tistory.com/114?category=900169

## Nginx 설정 파일 수정
`nginx.conf` 혹은 `default.conf` 열어 수정합니다. 
* root 사용자가 아닐 경우 sudo 명령어 사용하여 write 권한 줄 것
* default.conf는 nginx.conf에서 포함하는 기본 설정

```bash
sudo chmod +w /etc/nginx/conf.d/default.conf
vi /etc/nginx/conf.d/default.conf
```

다음과 같이 설정 파일 수정

Nginx 재시작
```
sudo systemctl restart nginx
```

## 연동 확인

웹 브라우저에 포트번호 지정없이 서버 IP 주소로 접속
nginx 화면이 아닌 Tomcat 화면이 나오면 완료
