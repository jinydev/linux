---
layout: home
title: 09.서버스와 데몬
description: 리눅스 서비스 및 데몬 관리
keywords: linux, daemon, service, systemd
---

## 09.[서버스와 데몬](/demon)
---
서비스와 데몬은 백그라운드에서 실행되는 프로그램으로, 서비스는 사용자가 명령어를 입력하여 실행되며, 데몬은 시스템이 부팅될 때 자동으로 실행됩니다.  

### 09-1.서버, 서비스 및 데몬
* [서버란?](/demon/server)
* [데몬이란?](/demon/demon)
* [서비스란?](/demon/service)

### 09-2.데몬의 실행 및 관리
* [systemd란](/demon/systemd)
* [런-레벨](/demon/runlevel)
* [service](/demon/service)  
* [systemctl](/demon/systemctl)  

### 09-3.파일 전송 데몬
다양한 리눅스의 데몬을 학습해 보고 설치를 해보도록 합니다.

* [ftp](/demon/ftp) : 파일올리기
* [Samba](/demon/samba)

### 09-4.도메인 네임 서비스
Linux 서버의 DNS는 도메인 이름을 IP 주소로 변환하여 네트워크의 리소스를 찾고 연결하는 서비스입니다.  
* [dns란?](/demon/dns)
* [dns 수정 및 설정](/demon/dns/setting)

### 09-5.메일 관련 데몬
* [Mail](/demon/mail)

* Postfix 메일 서버 설치와 설정
* Dovecot 메일 서버 설치와 설정
