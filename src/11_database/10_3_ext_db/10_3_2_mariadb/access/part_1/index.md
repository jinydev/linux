---
layout: home
title: "외부에서 접속하기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 외부에서 접속하기

## 외부에서 접속하기
---
DB는 기본적으로 외부로부터 접속을 되지 않도록 설정되어 있다.

`/etc/mysql/mariadb.conf.d/50-server.conf` 파일을 수정합니다. 
`bind-address` 부분을 주석 처리합니다.

```
$ sudo vi /etc/mysql/mariadb.conf.d/50-server.cnf
```

아래아 같은 부분을 찾아 수정을 합니다.

```
# Instead of skip-networking the default is now to listen only on
# localhost which is more compatible and is not less secure.
#bind-address            = 127.0.0.1
```

<br>


---

[⬅️ 이전](../)
