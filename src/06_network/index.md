---
layout: home
title: 06.네트워크
description: 리눅스 네트워크 기초 및 설정
keywords: linux, network, ip, tcp/ip
---

## 06.[네트워크](/network)
---


### 06-1.네트워크 장비(라우팅과 라우터)
네트워크 장비는 컴퓨터 네트워크에서 데이터를 전송하고 수신하는 기능을 담당하는 장치로, 라우터, 스위치, 허브 등이 있습니다. 이들 장비는 네트워크의 안정성과 속도, 보안 등을 유지하고 관리하는 역할을 합니다.  

* [네트워크 구성](/network/wire)
  - 유선네트웍
  - 무선네트웍
* [LAN](/network/hardware)
* [WAN](/network/hardware)
* [스위치와 허브](/network/hardware)
* [ROUTER](/network/hardware)

### 06-2.네트워크 기초
네트워크는 인터넷을 비롯한 다양한 네트워크 환경에서 데이터 통신이 가능하도록 지원합니다. 이러한 시스템들은 리눅스의 기본적인 구성 요소이며, 이를 이해하는 것이 리눅스를 다루는 데 중요합니다.

* [IP 주소](/network/ip)
* [클래스](/network/ip/class)
* [서브넷 마스크](/network/ip/mask)

* [포트](/network/ip/port)
* [소켓](/network/ip/soket)
* [주소체계](/network/ip/address)

* [tcp/ip](/network/tcp)

### 06-3.네트워크 설정과 보안
리눅스에서 네트워크 설정을 위한 방법에 대애허 알아 봅니다. 
* 기본적인 네트워크 명령어의 사용법 (ex. ifconfig, ip, route 등)
* 네트워크 인터페이스의 구성과 설정 방법
* [호스트 이름](/network/host)
* [도메인](/network/domain)
* [Demon](/network)

#### 네트워크 보안 기초
리눅스에서 보안은 시스템 자원 및 데이터를 외부의 공격으로부터 안전하게 보호하는 것을 의미합니다.  

방화벽 설정  
* [방화벽](/network/firewall)
* [ACL](/network/acl)

### 06-4.포트 포워딩 [NAT 설정](/network/nat)
리눅스에서 NAT(Network Address Translation)는 프라이빗 네트워크 주소를 퍼블릭 네트워크 주소로 변환하여 인터넷 접속을 가능하게 하는 기술입니다.  
- [net](/network/nat)
- [포트 포워딩](/network/nat)
  * [virtualBox](/network/nat/virtualbox)
  * [vmware](/network/nat/vmware)


### 리눅스 네트워크 설정
* [ip확인 및 설정](/system/ip)
