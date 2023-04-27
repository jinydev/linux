---
layout: home
---

# __리눅스 - 우분투(Ubuntu)__
## __0421. 방화벽__ 
<hr/>

> 방화벽은 불필여한 네트워크 연결을 차단하고 외부공격으로부터 시스템을 보호함   
> 리눅스 서버에서 특정 사용자만 해당 서버에 접속하도록 해야 함   

- 리눅스에서는 대표적으로 iptables와 firewalld 두 가지 방화벽 명령어가 있음   
1. iptables
    - `iptables -L` : 현재 적용중인 방화벽 규칙을 조회
    - `iptables -F` : 모든 방화벽 규칙을 삭제
    - `iptables -A [CHAIN] -p [PROTOCOL] --dport [PORT] -j [TARGET]` : 지정한 [CHAIN]에 [PROTOCOL] 프로토콜, [PORT] 포트로 들어오는 트래픽을 [TARGET]으로 전달   
    - `iptables -P [CHAIN] [TARGET]` : 기본 정책을 [TARGET]으로 설정
2. firewalld
    - `firewall-cmd --state` : 방화벽 상태를 확인
    - `firewall-cmd --get-active-zones` : 활성화된 존을 조회
    - `firewall-cmd --zone=[ZONE] --add-port=[PORT]/[PROTOCOL]` : [ZONE]에 [PROTOCOL] 프로토콜, [PORT] 포트를 허용
    - `firewall-cmd --zone=[ZONE] --set-default-zone` : 기본 존을 설정   

- 현재 대부분의 리눅스 배포판에서는 firewalld가 기본 방화벽 도구로 사용되고 있음.   
- firewalld는 zone, service, port 등의 논리적인 개념을 도입하여 사용자가 보다 쉽게 방화벽 규칙을 설정할 수 있음. 
- 네트워크 인터페이스의 변경을 적극적으로 감지하여 자동으로 방화벽 규칙을 업데이트하며, 더욱 다양한 기능을 제공함.
- iptables는 매우 강력하고 유연한 방화벽 도구이지만, 설정하기가 복잡하고 사용하기 어려움. 
- 네트워크 인터페이스의 변경을 수동으로 감지해야하고, 덜 직관적인 방식으로 규칙을 설정해야 함.
- 대부분의 리눅스 사용자는 firewalld를 사용하여 더 쉽고 안전하게 방화벽을 설정하고 유지보수하고 있음   
      
   
### **시스템 firewalld 설치**
```linux
--yum을 이용하여 firewalld를 설치
sudo yum install firewall   


--서버 부팅/재부팅 시 자동으로 firewalld데몬이 실행되게 함
--원하는 서비스나 port를 통과할 수 있게 열어줘야 함
sudo systemctl enable firewalld   
sudo systemctl start firewalld   


--방화벽을 다 막고 있다고 생각하고 원하는 서비스에 대해 해제하는 방법 
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
--추가하기
sudo firewall-cmd --permanent --remove-service=http
sudo firewall-cmd --permanent --remove-service=http
--제거하기
```

> sudo : 관리자 권한으로 실행해라   
> firewall-cmd : firewall cli명령어   
> --permanent : 영구적으로 실행해라 (default zone에 등록됨)   
> --add-service : 해당 서비스를 추가해라   
> --remove-service : 해당 서비스를 삭제해라   

```linux
--특정 port로 방화벽 해제
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-port=81/tcp
sudo firewall-cmd --permanent --add-port=82/tcp


sudo firewall-cmd --permanent --remove-port=80/tcp
sudo firewall-cmd --permanent --remove-port=81/tcp
sudo firewall-cmd --permanent --remove-port=82/tcp


--특정IP에 대해 방화벽 해제하기
sudo firewall-cmd --permanent --add-source=192.168.0.100
sudo firewall-cmd --permanent --remove-source=192.168.0.100


--변경된 firewall구성을 적용 설정후 반드시 리로딩하여 반영
sudo firewall-cmd --reload

--현재 방화벽 리스트 보기
firewall-cmd --list-all
```