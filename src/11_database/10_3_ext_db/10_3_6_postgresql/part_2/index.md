---
layout: home
title: "DB 접속하기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# DB 접속하기

## DB 접속하기

psql 명령을 입력하여 DB에 접속해 봅니다.

```
postgres@test:~$ psql
psql (12.5 (Ubuntu 12.5-0ubuntu0.20.04.1))
Type "help" for help.

postgres=#
```

현재 설치된 버젼은 12.5 입니다.

또는 sudo 계정으로 postgreSql에 바로 접속을 할때에는 다음과 같이 입력합니다.

```
sudo -u postgres pgsql
```

test 사용자 계정에서 다음과 같이 postgreSql로 바로 진입하는 것을 볼 수 있다.

```
test@test:~$ sudo -u postgres psql
psql (12.5 (Ubuntu 12.5-0ubuntu0.20.04.1))
Type "help" for help.

```

#### 종료하기

postgreSql에서 종료하고 나갈때는 `\q`를 입력합니다.

```
postgres=# \q
postgres@test:~$
```


---

[⬅️ 이전](../)
