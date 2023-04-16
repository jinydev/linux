---
layout: home
---

# Curl
`curl`은 command line 용 data transfer tool 이다.


* DOWNLOAD / UPLOAD 모두 가능하다.

* HTTP / HTTPS / FTP / LDAP / SCP / TELNET / SMTP / POP3 등 주요 프로토콜을 지원한다.

* LINUX / UNIX 계열 및 Windows 등 주요한 OS에서 구동되므로 여러 플랫폼과 OS에서 유용하게 사용할 수 있다.

* ibcurl 이라는 C 기반의 library가 제공되므로 C / C++ 프로 그램 개발시 위의 protocol과 연계가 필요하다면 libcurl을 손쉽게 연계할 수 있다.

* libcurl은 PHP, RUBY, PERL 및 여러 언어에 바인딩 되어 있으므로 사용하는 언어나 개발 환경에 맞게 libcurl을 사용할 수 있다.



## CURL 설치
우분투에 curl을 설치해 봅니다.

```bash
sudo apt install curl
```

curl이 잘 설치가 되었는지 확인합니다.
```bash
hojin@hojin3:/home$ curl --version
curl 7.81.0 (x86_64-pc-linux-gnu) libcurl/7.81.0 OpenSSL/3.0.2 zlib/1.2.11 brotli/1.0.9 zstd/1.4.8 libidn2/2.3.2 libpsl/0.21.0 (+libidn2/2.3.2) libssh/0.9.6/openssl/zlib nghttp2/1.43.0 librtmp/2.3 OpenLDAP/2.5.13
Release-Date: 2022-01-05
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets zstd
```

## 명령

* `-f`  
HTTP 요청 헤더의 contentType을 multipart/form-data로 보낸다.

* `-s`  
진행 과정이나 에러 정보를 보여주지 않는다.(–silent)

* `-S`  
SSL 인증관련

* `-L`  
서버에서 301, 302 응답이 오면 redirection URL로 따라간다.
apt-key : apt가 패키지를 인증할 때 사용하는 키 리스트를 관리한다. 이 키를 사용해 인증된 패키지는 신뢰할 수 있는 것으로 간주한다.
add 명령어는 키 리스트에 새로운 키를 추가하겠다는 의미이다.