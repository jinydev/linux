---
layout: home
---

# Mysql 클라이언트 접속


## 콘솔 접속
mysql 서버를 설치하게 되면 콘솔 client 접속 프로그램도 같이 설치가 됩니다. 콘솔창에서 `mysql` 명령을 입력하면 됩니다.

### 비밀번호를 이용한 접속
mysql 보안을 위하여 root 비밀번호를 설정햔 경우라면 사용자 정보와 비밀번호를 같이 입력해 주어야 합니다.
> root [비밀번호 설정](/database/mysql/password)

이제 설정한 비밀번호를 이용하여 접속을 해보도록 합니다. 

```
hojin@hojin:~$ mysql -u root -p
```
> 접속을 위해서 사용자 아이디 `-u` 옵션과 비밀번호 `-p`옵션을 같이 사용합니다.

콘솔 입력시 비밀번호는 입력하지 않습니다. 대신에, mysql 클라이언트가 실행이 되면서 패스워드를 물어보게 됩니다. 다음과 같이 실습을 해보도록 합니다.

```
hojin@hojin:~$ mysql -u root -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 67
Server version: 10.5.8-MariaDB-1:10.5.8+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> exit
Bye
```

데이터베이스 접속을 종료할때에는 `exit`를 입력합니다.


## MysqlWorkBench
`MysqlWorkBench`는 GUI 방식으로 mysql 데이터베이스에 접속을 관리하는 클리이언트 입니다.

* [워크벤치 설치하기](/database/client/mysqlworkbench)

## DBEaver
mysql 말고도 다양한 데이터베이스에 접속하여 관리할 수 있습니다.

* [DBEaver 설치하기](/database/client/dbeaver)

## HeidiSQL
윈도우용 mysql을 설치하면 같이 설치가 됩니다.

* [HeidiSQL 설치하기](/database/client/heidisql)
