---
layout: home
title: "ssh 설치하기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# ssh 설치하기

## ssh 설치하기
ssh를 통하여 서버에 접속을 하기 위해서는 별도의 `ssh 서비스` 서버 프로그램을 설치해 주셔야 합니다.
ssh 서버를 구축하기 위해서는 2단계 작업이 필요 합니다.

* [apt](../apt/)로 명령으로 우분투 리눅스에 설치하기
* [yum](../yum/)로 명령으로 로키 리눅스에 설치하기

### ssh 설치여부 확인하기
apt 명령으로 먼저 ssh가 설치가 되어 있는지 확인을 합니다.
```bash
s
hojin@hojin-VirtualBox:~$ apt list --installed | grep ssh

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

libssh-4/jammy,now 0.9.6-2build1 amd64 [installed,automatic]
openssh-client/jammy-updates,now 1:8.9p1-3ubuntu0.1 amd64 [installed,automatic]
openssh-server/jammy-updates,now 1:8.9p1-3ubuntu0.1 amd64 [installed,automatic]
openssh-sftp-server/jammy-updates,now 1:8.9p1-3ubuntu0.1 amd64 [installed,automatic]
ssh-import-id/jammy,jammy,now 5.11-0ubuntu1 all [installed,automatic]
ssh/jammy-updates,jammy-updates,now 1:8.9p1-3ubuntu0.1 all [installed]
hojin@hojin-VirtualBox:~$

```

### ssh 서버 설치
`apt` 명령어를 사용하여 패키지를 설치합니다.

```
$sudo apt-get install openssh-server
```

설치된 sshd가 실행중인지 확인을 합니다.
```bash
ps -ed | grep sshd
```

### VirtualBox 네트워크 추가 설정
외부에서 VirtualBox안에 있는 Ubuntu를 접속을 하기 위해서틑 포트 포워딩을 통한 활성화를 해주어야 합니다.
VirtualBox 메뉴에서 `장치`->`네크워크`->`네트워크 설정`을 선택합니다.

![image-20230329185149729](../../img/image-20230329185149729.png)

SSH는 기본적으로 22번 포트를 사용합니다. 윈도우 호스트의 22번 포트와 VM의 22번 포트를 연결해 주어야 합니다.

> 실제 서버를 사용하는 경우 보안을 위하여 다른 번호를 사용합니다.

![image-20230329185246081](../../img/image-20230329185246081.png)


---

[⬅️ 이전](../)
