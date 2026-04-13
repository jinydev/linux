---
layout: home
title: "설정"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 설정

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


---

[⬅️ 이전](../)
