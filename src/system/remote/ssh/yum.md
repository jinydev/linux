---
layout: home
title: "래드햇 계열에서 OpenSSH 설치하기"
---

# 래드햇 계열에서 OpenSSH 설치하기
`yum` 명령어를 사용하여 OpenSSH 서버를 설치합니다.

## 설치하기
우선 터미널 창을 열고, `root` 권한으로 로그인합니다. 다음 명령어를 입력하여 `OpenSSH` 서버를 설치합니다.

```bash
yum install openssh-server
```
설치가 완료되면 SSH 서버가 실행되고 있습니다.

## 클라이언트 접속
이제 다른 컴퓨터나 디바이스에서 리눅스 서버에 SSH로 연결할 수 있습니다. SSH 접속을 위해서는 별도의 SSH 클라이언트가 필요합니다.  

*  macOS나 Linux 시스템에서는 터미널을 열고 ssh 명령어를 사용하여 연결할 수 있습니다. 
* Windows 시스템에서는 PuTTY와 같은 SSH 클라이언트 프로그램을 사용할 수 있습니다.
