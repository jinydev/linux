---
layout: home
title: "환경설정"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 환경설정

## 환경설정
mysql 환경을 설정합니다. 설정은 `/etc/my.cnf` 파일에 위치합니다. 
vi 에디터를 이용하여 정보를 수정합니다.  

```
vi /etc/my.cnf
```

다음과 같이 설정을 추가합니다.
```ini
[client]
default-character-set = utf8mb4

[mysql]
default-character-set = utf8mb4

[mysqldump]
default-character-set = utf8mb4
```

`[mysqld]` 서버쪽 설정 하단에 추가합니다.
```ini
skip-character-set-client-handshake
init_connect = "SET collation_connection = utf8mb4_unicode_ci"
init_connect = "SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci"

character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
```
> UTF8는 기본적으로 3바이트나, 이모티콘 등도 같이 표현하기 위하여 4바이트 타입의 UTF8 형식으로 설정합니다.


---

[⬅️ 이전](../)
