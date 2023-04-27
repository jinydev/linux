---
layout: home
---

# bind9
Ubuntu에 BIND(Berkeley Internet Name Domain)를 설치합니다.


## 패키지 설치
명령을 실행하여 BIND를 설치합니다.

```bash
sudo apt-get update 
sudo apt-get install bind9 
```


BIND가 설치되면 구성해야 할 수 있습니다. 
명령을 실행하여 BIND 서비스를 다시 시작합니다.  
```
sudo service bind9 restart 
```

## 설정
`jinydev.com` 도메인을 예를 들어 설정하는 방법에 대해서 알아 보도록 합니다.

BIND9를 사용하여 새 도메인 jinydev.com을 설정하려면 다음 단계를 따르십시오.


* /etc/bind 디렉토리에 있는 named.conf.local 

```
sudo vi /etc/bind/named.conf.local
```

파일을 편집하여 jinydev.com에 대한 새 영역을 추가합니다.

```bash
zone "jinydev.com" {
    type master;
    file "/etc/bind/db.jinydev.com";
};
```

* /etc/bind 디렉토리에 db.jinydev.com이라는 새 영역 파일을 만듭니다.

```
sudo touch /etc/bind/db.jinydev.com
sudo vi /etc/bind/db.jinydev.com
```

```bash
$TTL    86400
@       IN      SOA     jinydev.com. admin.jinydev.com. (
                  1         ; Serial
             604800         ; Refresh
              86400         ; Retry
            2419200         ; Expire
             86400 )       ; Minimum TTL
;
@       IN      NS      ns1.jinydev.com.
@       IN      NS      ns2.jinydev.com.
@       IN      A       192.168.56.114
www     IN      A       192.168.56.114

ns1     IN      A       192.168.56.114
ns2     IN      A       192.168.56.113
```
이렇게 하면 ns1.jinydev.com 및 ns2.jinydev.com에 대한 두 개의 추가 NS 레코드와 해당 IP 주소에 대한 두 개의 A 레코드가 추가됩니다. @ 기호는 도메인 이름 자체의 줄임말이므로 @ IN NS ns1.jinydev.com입니다. jinydev.com 도메인이 ns1.jinydev.com 네임서버에 의해 제공됨을 지정합니다.

```
sudo service bind9 restart
```
명령을 실행하여 BIND9 서비스를 다시 시작하여 변경 사항을 적용합니다.

## 테스트
ip설정을 수동으로 하고, 네임서버를 bind9으로 설정한 곳으로 지정합니다.

추가한 도메인으로 접속을 합니다.

## 도메인 등록 기관
* BIND9 서버의 IP 주소로 ns1.jinydev.com 및 ns2.jinydev.com에 대한 NS 레코드를 추가하여 BIND9 서버를 가리키도록 도메인 등록 기관을 구성합니다.

## Slave DNS 구성

## 웹기반 DNS 설정 도구
음은 BIND9 DNS 서버를 관리하기 위한 무료 오픈 소스 웹 기반 도구입니다.


* Webmin: Linux 및 Unix 시스템에서 BIND9 및 기타 서비스 관리를 지원하는 무료 오픈 소스 웹 기반 시스템 관리 도구입니다.
* ISPConfig: BIND9용 DNS 관리 기능이 포함된 무료 오픈 소스 웹 호스팅 제어판입니다.
* Virtualmin: 이것은 BIND9 관리 기능을 포함하는 ISPConfig와 유사한 무료 오픈 소스 웹 호스팅 제어판입니다.

이러한 도구는 무료로 사용할 수 있지만 올바르게 설정하고 구성하려면 약간의 기술 지식이 필요할 수 있습니다. 서버에 설치하는 모든 소프트웨어가 안전하고 최신 상태인지 확인하고 DNS 서버 관리 모범 사례를 따라 보안 취약성 또는 기타 문제를 방지하는 것이 중요합니다.
