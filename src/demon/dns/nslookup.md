---
layout: home
---

# nslookup
nslookup은 도메인 `이름` 또는 `IP 주소 정보`를 얻기 위해 DNS(도메인 이름 시스템) 서버를 쿼리하는 데 사용되는 명령줄 도구입니다. 일반적으로 네트워크 연결 문제를 해결하거나 DNS 구성을 확인하는 데 사용됩니다.

nslookup을 사용하여 사용자는 도메인 이름이나 IP 주소를 입력하고 해당 IP 주소, 메일 교환(MX) 서버 및 기타 DNS 레코드를 포함하여 해당 도메인에 대한 정보를 받을 수 있습니다. 또한 이 도구를 사용하면 사용자가 특정 DNS 서버를 쿼리하고 받은 응답에 대한 자세한 정보를 볼 수 있습니다.

## nslookup의 일반적인 용도는 다음과 같습니다.
* 네트워크 연결 문제 해결: DNS 서버를 쿼리하여 사용자는 도메인 이름이 올바른 IP 주소로 확인되는지 또는 DNS 서버가 요청에 응답하는지 확인할 수 있습니다.
* DNS 구성 확인: nslookup을 사용하여 DNS 레코드가 올바르게 구성되었는지, 도메인 이름이 올바른 IP 주소로 확인되는지 확인할 수 있습니다.
* 이메일 문제 조사: 사용자는 도메인 이름의 MX 레코드를 쿼리하여 해당 도메인의 이메일 처리를 담당하는 메일 서버를 확인할 수 있습니다.

nslookup은 Windows, Linux 및 macOS를 포함한 대부분의 운영 체제에서 사용할 수 있으며 명령줄을 통해 액세스할 수 있습니다.

## 실습
Domain name으로 ip를 찾아 봅니다. `nslookup` 명령을 입력합니다.

```bash
poly@poly-VirtualBox:~$ nslookup
> www.naver.com
;; communications error to 127.0.0.53#53: timed out
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
www.naver.com   canonical name = www.naver.com.nheos.com.
Name:   www.naver.com.nheos.com
Address: 223.130.200.107
Name:   www.naver.com.nheos.com
Address: 223.130.195.200
>
```
