---
layout: home
title: "방화벽 설정"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 방화벽 설정

## 방화벽 설정
FTP 서버에 방화벽을 설정해줘야 합니다. Ubuntu의 기본 방화벽인 ufw를 사용하여 설정합니다.

```
sudo ufw allow 20/tcp
sudo ufw allow 21/tcp
sudo ufw allow 40000:50000/tcp
sudo ufw enable
```

* ufw allow 20/tcp: FTP 서버의 데이터 포트를 열어줍니다.
* ufw allow 21/tcp: FTP 서버의 제어 포트를 열어줍니다.
* ufw allow 40000:50000/tcp: FTP 서버의 Passive 모드에서 사용하는 포트를 열어줍니다.
* ufw enable: 방화벽을 활성화합니다.


---

[⬅️ 이전](../)
