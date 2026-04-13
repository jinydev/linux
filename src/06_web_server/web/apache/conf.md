---
layout: home
---

## 아파치 환경설정
아파치 웹 서버의 기본 구성 파일은 `httpd.conf`입니다.  
이 파일은 보통 `/etc/httpd/conf/httpd.conf` 또는 `/etc/apache2/httpd.conf`와 같은 경로에 위치합니다.  

## 기존 설정 파일 백업
설정 파일을 수정하기 전에 기존 설정 파일을 `백업`합니다. 다음 명령을 사용하여 설정 파일의 복사본을 생성합니다.  

```bash
sudo cp /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.bak
```

설정 파일의 경로 및 이름은 시스템에서 설치된 아파치 버전 및 운영 체제에 따라 달라질 수 있습니다.  

설정 파일을 변경하면 서버를 다시 시작하여 변경 사항을 적용해야 합니다. 서버를 재시작하려면 다음 명령을 사용합니다.  
```bash
sudo systemctl restart httpd
```

## 포트설정
아파치 웹 서버가 사용하는 기본 포트는 80입니다. 이를 다른 포트로 변경하려면 Listen 지시어를 변경합니다.  

```mathematica
Listen 8080
```

## 가상 호스트 설정
아파치 웹 서버는 여러 도메인 이름 또는 IP 주소를 처리할 수 있습니다. 이를 위해 가상 호스트를 구성합니다.  

가상호스트는 기본적으로 `httpd.conf` 파일에 작성하는 것이 기본이나 복잡성을 제거하기 위해서 별도의 `httpd-vhost.conf`파일로 분리하여 관리 합니다.   
```
# Virtual hosts
Include conf/extra/httpd-vhosts.conf
```

`httpd-vhost.conf` 설정파일

```mathematica
NameVirtualHost *:80

<VirtualHost *:80>
    ServerName example.com
    DocumentRoot /var/www/example.com
    ServerAlias www.example.com     
</VirtualHost>
```

위의 예에서는 `example.com` 도메인 이름의 웹 페이지를 `/var/www/example.com` 디렉터리에서 서비스합니다. 

위의 예에서는 /var/www/html 디렉터리에 대한 색인을 활성화합니다. 

* 디렉터리 인덱싱: 디렉터리에 인덱스 파일이 없을 경우, 아파치 웹 서버는 디렉터리에 대한 색인을 생성합니다.

```mathematica
<Directory /var/www/html>
    Options +Indexes
</Directory>
```

## 접속권한 설정
사용자 계정을 생성후에 웹사이트를 실행하게 되면 permission 오류가 발생을 합니다.

해당 계정이 웹서버에 접근을 할 수 있도록 권한을 추가적으로 부여를 해야 합니다.

```bash
yum install mod_ruid2
```

## 참조
* https://joont.tistory.com/46
* http://blog.ivps.kr/72