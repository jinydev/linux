---
layout: home
---

# IP 확인
리눅스에서는 `ifconfig`명령을 통하여 서버의 아이피를 확인할 수 있습니다.

## Netstat 확인
ifconfig 명령을 사용하기 위해서는 리눅스에 Netstat가 설치되어 있어야 합니다.

`netstat` 명령어를 입력해 봅니다.

```
$ netstat
```

실행결과
```
hojin@hojin3:~$ netstat
Command 'netstat' not found, but can be installed with:
sudo apt install net-tools
```

netstat가 설치되어 있지 않습니다. apt 명령어를 통하여 설치 합니다.
```
$sudo apt install net-tools
```

실행결과
```
hojin@hojin3:~$ sudo apt install net-tools
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  net-tools
0 upgraded, 1 newly installed, 0 to remove and 73 not upgraded.
Need to get 204 kB of archives.
After this operation, 819 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 net-tools amd64 1.60+git20181103.0eebece-1ubuntu5 [204 kB]
Fetched 204 kB in 2s (132 kB/s)
Selecting previously unselected package net-tools.
(Reading database ... 24179 files and directories currently installed.)
Preparing to unpack .../net-tools_1.60+git20181103.0eebece-1ubuntu5_amd64.deb ...
Unpacking net-tools (1.60+git20181103.0eebece-1ubuntu5) ...
Setting up net-tools (1.60+git20181103.0eebece-1ubuntu5) ...
Processing triggers for man-db (2.10.2-1) ...
```

## ifconfig로 ip 정보 확인하기

```
$ ifconfig
```

실행결과
```
hojin@hojin3:~$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.23.192.132  netmask 255.255.240.0  broadcast 172.23.207.255
        inet6 fe80::215:5dff:fe6e:2a49  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:6e:2a:49  txqueuelen 1000  (Ethernet)
        RX packets 18713  bytes 28011397 (28.0 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2630  bytes 191037 (191.0 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```


물리적 연결된 네트워크만 볼때는 `-a` 옵션을 같이 사용합니다.

```bash
hojin@hojin3:~$ ifconfig -a
bond0: flags=5122<BROADCAST,MASTER,MULTICAST>  mtu 1500
        ether 4e:42:37:a7:9d:0f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

dummy0: flags=130<BROADCAST,NOARP>  mtu 1500
        ether 92:8c:4e:82:e3:c2  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.23.192.132  netmask 255.255.240.0  broadcast 172.23.207.255
        inet6 fe80::215:5dff:fe6e:2a49  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:6e:2a:49  txqueuelen 1000  (Ethernet)
        RX packets 18889  bytes 28230892 (28.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2714  bytes 196781 (196.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 2  bytes 100 (100.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2  bytes 100 (100.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

sit0: flags=128<NOARP>  mtu 1480
        sit  txqueuelen 1000  (IPv6-in-IPv4)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

tunl0: flags=128<NOARP>  mtu 1480
        tunnel   txqueuelen 1000  (IPIP Tunnel)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

## 직접 ip 변경하기
`/etc/network` 티렉터리에 interfaces 파일에 설정되어 있습니다.

