---
layout: home
title: "접속 주소 확인"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 접속 주소 확인

## 접속 주소 확인
`ifconfig` 명령으로 서버의 IP 주소 확인

```bash
poly@poly-VirtualBox:/srv/ftp$ ifconfig
enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::7cac:debc:82dc:b444  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:17:48:bc  txqueuelen 1000  (Ethernet)
        RX packets 56675  bytes 85372089 (85.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4359  bytes 296103 (296.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

enp0s8: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.56.114  netmask 255.255.255.0  broadcast 192.168.56.255
        inet6 fe80::6fee:caa9:42b4:a0e2  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:85:76:27  txqueuelen 1000  (Ethernet)
        RX packets 690  bytes 58667 (58.6 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 557  bytes 75170 (75.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 203  bytes 19696 (19.6 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 203  bytes 19696 (19.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

호스트 전용 어뎁터로 연결된 `192.168.56.114`를 확인할 수 있습니다.


---

[⬅️ 이전](../)
