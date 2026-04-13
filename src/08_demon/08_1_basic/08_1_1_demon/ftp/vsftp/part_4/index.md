---
layout: home
title: "방화벽 허용"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 방화벽 허용

## 방화벽 허용 
외부에서 FTP 서버에 접근하도록 방화벽 포트를 허용합니다.
```bash
sudo ufw allow ftp
sudo ufw reload
```

> 문제가 계속 발생시 : 원활한 외부 접속을 허용하기 위해 systemctl stop ufw 명령으로 잠시 방화벽을 끔


---

[⬅️ 이전](../)
