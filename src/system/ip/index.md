---
layout: home
---

## IP확인
리눅스에서 ip를 확인하는 방법은 기본적으로 `ifconfig` 입니다.

하지만, Ubuntu 20.04 버젼이상 부터는 바로 ifconfig 명령을 사용할 수 없습니다. 이를 사용하기 위해서는 먼저 `net-tools`를 설치해 주어야 합니다.

```
# sudo apt-get update
# sudo apt-get upgrade

# sudo apt-get install net-tools
```

설치 완료후에 터미널 창에서 `ifconfig` 명령을 입력합니다.

## 고정 IP로 변경하기
> https://it-svr.com/ubuntu-22-04-lts-static-ip/
ubuntu를 서버로 사용하는 경우라면, 외부에서의 접근을 위하여 고정 IP를 사용하는 경우가 많습니다.

먼저 현재 사용하고 있는 `인터페이스 이름`을 확인해야 합니다.
`ifconfig` 명령을 사용합니다.

저의 경우에는 `wlo1` 이름을 가지고 있습니다.
기본적으로 Ubuntu의 Network 관리는 `netplan`을 사용합니다.
root 권환으로 network 설정을 편집합니다.

```
vi /stc/netplan/01-network-manager-all.yaml
```

설정 파일을 수동으로 iP를 지정합니다.

```yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    ens18:
      addresses:
      - 192.168.1.12/24
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
      routes:
        - to: default
          via: 192.168.1.1
  version: 2
```

netplan apply 명령어로 변경한 설정값을 적용
