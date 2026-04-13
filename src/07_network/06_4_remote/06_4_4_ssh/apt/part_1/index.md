---
layout: home
title: "방화벽 설정"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 방화벽 설정

## 방화벽 설정
ssh를 접속하기 위해서는 방화벽을 허용해 주어야 합니다. 우분투에서 기본적으로 사용되는 방화벽은 iptables이나 ufw입니다. 만약 방화벽이 설치되어 있지 않다면, 방화벽을 설치하고 활성화해야 합니다.  

 다음과 같이 `22`번 포트를 허용합니다.

```bash
sudo ufw allow 22
```

또는
```bash
sudo ufw allow ssh
```

포트 접속을 허용하였다면 방화벽을 다시 로드 합니다.

```
$ ufw reload
```
ufw 방화벽이 활성화되었으며, SSH 포트(기본값은 22번)를 열어 다른 컴퓨터나 디바이스에서 우분투 시스템에 SSH로 연결할 수 있습니다

"Firewall not enabled (skipping reload)" 메시지는 방화벽이 활성화되어 있지 않기 때문에 방화벽을 다시로드하지 않겠다는 의미입니다. 

방화벽을 활성화합니다.
```bash
sudo ufw enable
```

만일 방화벽이 설치되어 있지 않다면 다음과 같이 ufw 패키지를 설치합니다.
```bash
sudo apt-get install ufw
```


---

[⬅️ 이전](../)
