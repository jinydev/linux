---
layout: home
title: "접속하기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 접속하기

## 접속하기
mysql은 보안을 위하여 `임시 비밀번호` 설정되어 있습니다. 임시 비밀번호는 `/var/log/mysqld.log` 안에 숨겨져서 기록이 되어 있습니다.

`grep` 명령어를 통하여 `temporary password`를 찾아 봅니다.
```
grep `temporary password` /var/log/mysqld.log
``` 

이후에는 보안 설정을 위하여 비밀번호와 접속 권환을 변경해 주어야 합니다.
* [패스워드 설정](/database/mysql/password)

mysql 콘솔 클라이언트 통하여 데이터베이스에 접속을 해보도록 합니다.

```
mysql -u root -p
```

콘솔에서 데이터베이스를 조작하기 위해서는 sql 문법 학습이 필요로 합니다.
* [sql 문법 학습하기](https://database.jiny.dev/sql)


---

[⬅️ 이전](../)
