---
layout: home
---

# 방화벽 설정
서버는 다양한 서비스들을 제공합니다. 제공되는 서비스를 구분하기 위하여 포트를 활용합니다. 

## 접속제한
---
기본적으로 서버는 다양한 포트들을 개방해 놓고 있다. 일부는 권한이 없는 사람들이 포트를 통하여 접속을 하기도 한다.
방화벽은 이러한 포트를 비활성화 하여 접속을 제한하거나, 허용할 수 있게 만드는 것이다.
* 보안을 위하여 외부에 서비스를 제공할 때 필요한 포트만 열어주는 방식으로 사용할 것


## 방화벽 설정
---
방화벽을 설정할 때에는 `ufw` 명령어를 사용한다.

다음은 웹서비스를 하는 80번 포트를 열여주는 방화벽 설정이다.
```bash
$ ufw allow 80
```

## GUI 기반의 방화벽 설정
---
GUI환경에서는 보다 편리하게 방화벽을 설정할 수 있는 `gufw` 응용프로그램을 제공한다.  

### 패키지 설치
이 프로그램을 사용하기 위해서는 다음과 같이 별도로 패키지를 설치해 주어야 한다.
```bash
$ sudo apt-get install gufw
$ gufw
```

### 실행

![image-20230324183101920](./img/image-20230324183101920.png)


## SeLinux 방화벽

selinux 방화벽 상태 확인
```
[root@localhost ploy]# sestatus
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      33
```

selinux 방화벽 끄기
```
grubby --update-kernel ALL --args selinux=0
```

## 방화벽 설정 
방화벽과 관련된 패키지들을 설치합니다.
```
dnf install -y firewall-config
```