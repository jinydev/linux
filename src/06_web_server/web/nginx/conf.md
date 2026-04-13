---
layout: home
---

# Nginx 설정


## 기본포트 변경
기본적으로 80번 포트를 listen 합니다. 이를 수정하고자 할때에는 
`/etc/ngnix/sites-enabled/default` 의 내용을 수정합니다.

## nginx 설정
- package(apt-get을 통한 설치)의 경우: /etc/nginx에 위치
- 직접 compile한 경우: /usr/local/nginx/conf, /usr/local/etc/nginx

### 검사
```
// configuration file syntax check
$ sudo nginx -t
```

