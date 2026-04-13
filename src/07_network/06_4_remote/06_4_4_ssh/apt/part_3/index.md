---
layout: home
title: "OpenSSH 설치하기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# OpenSSH 설치하기

## OpenSSH 설치하기
SSH로 서버에 접속을 하기 위해서는 `openssh` 서버를 설치해 주어야 합니다.

설치전 `update`를 통하여 패키지의 목록을 갱신합니다.

```bash
sudo apt update
```

각각의 패키지들을 최신의 버젼으로 업그레이드 해 줍니다.

```bash
sudo apt upgrade
```

> update는 패키지의 목록을 갱신하는 것이고, upgrade는 갱신된 목록에 따라 설치된 패키지를 업그레이드 하는 동작입니다.

### SSH 재설치
만일 기존에 SSH서버가 설치가 되었다면, 충돌을 방지하기 위해서 완전삭제(purge) 합니다.

```bash
sudo apt purge openssh-server
```

`openssh-server`를 설치 합니다.

```bash
sudo apt install -y openssh-server 
```

### 재시작

SSH 서버를 **완전** 재시작 해 준다.

```bash
sudo service ssh --full-restart
sudo service ssh restart
```

또는 

```
$sudo systemctl restart ssh
```


---

[⬅️ 이전](../)
