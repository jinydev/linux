---
layout: home
---

# HTTPS
Let's Encrypt를 사용하여 임시 도메인에 대한 SSL/TLS 인증서를 얻고 HTTPS를 설정할 수 있습니다.

Let's Encrypt를 사용하려면 Apache 또는 Nginx와 같은 웹 서버를 설치하고 HTTP를 통해 웹 사이트를 제공하도록 구성해야 합니다. 또한 Let's Encrypt에서 SSL/TLS 인증서를 자동으로 가져와 구성할 수 있는 도구인 Certbot을 설치해야 합니다.

## Certbot 설치
Ubuntu에 Certbot을 설치하려면 다음 단계를 따르십시오.

다음 명령을 실행하여 시스템에 Certbot PPA를 추가합니다.

```
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot 
```

## 인증서를 생성

인증서를 생성하려면 다음 명령을 실행할 수 있습니다.
```bash
sudo certbot --nginx # 엔진엑스에 등록된 도메인 인증서 생성
```

Certbot을 설치하고 HTTP를 통해 웹 사이트를 제공하도록 웹 서버를 구성한 후에는 다음 명령을 실행하여 인증서를 얻을 수 있습니다.

```bash
sudo certbot --apache -d your_domain_name
```

```bash
sudo certbot certonly --nginx --domain example.com --webroot -w /var/www/html -d example.com -d www.example.com
```

your_domain_name을 Bind9로 설정한 실제 도메인 이름으로 바꿉니다.


인증서가 성공적으로 생성되었는지 확인합니다.
```
sudo certbot certificates
```

이 명령은 방금 생성한 인증서를 포함하여 Certbot이 생성한 모든 인증서 목록을 표시합니다.



## 연장


Certbot은 SSL/TLS 인증서를 얻고 구성하는 과정을 안내합니다. 프로세스가 완료되면 웹사이트가 HTTPS를 통해 제공됩니다.


Let's Encrypt 인증서는 90일 동안만 유효합니다. 웹 사이트가 HTTPS를 통해 계속 제공되도록 하려면 인증서가 만료되기 전에 갱신해야 합니다. 다음 명령을 실행하도록 cron 작업을 설정하여 Certbot을 사용하여 인증서를 자동으로 갱신할 수 있습니다.

```
sudo certbot renew
```
