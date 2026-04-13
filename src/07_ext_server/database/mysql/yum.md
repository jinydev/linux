---
layout: home
---

# Mysql 설치
리눅스 서버에 Mysql 데이터베이스를 설치합니다.

## 리포지터리 확인 및 등록

오라클 mysql 사이트에 접속하여 설치를 위한 레포지터리를 확인합니다.

시스템에 mysql을 설치할 수 있도록 리포지터리 주소를 등록합니다.

```
yum localinstall 주소
```


## 설치하기


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

## 실행 및 중지
Mysql 데이터베이스는 항상 실행되고 있는 데몬(demon)과 같은 성격을 가집니다. 이를 위해서 서비스를 통하여 실행을 해 주는 것이 좋습니다.

시작하기
```
systemctl start mysqld
```
> 서비스 실행이름이 `mysql`이 아닌 끝에 `d`가 붙은 `mysqld`입니다. `d`는 demon을 의미합니다.

서버가 잘 실행이 되고 있는지 프로세스를 확인합니다.
```
ps -ef | grep mysql
```

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


## 테스트 데이터베이스 만들기

스키마 목록 확인하기
```
show databases;
```

새로운 스키마 생성하기
```
CREATE DATABASE 스키마명;
```
> 데이터베이스 문자셋을 같이 설정할때는 다음과 같이 합니다.
> ```
> CREATE DATABASE 스키마명 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
> ```

스키마 접속권한 유저 생성 및 권환 부여
```
CREATE USER '사용자명'@'%' IDENTIFIED WITH mysql_native_password BY 'xxx';
GRANT ALL PRIVILEGES ON *.* TO '사용자명'@'%' WITH GRANT OPTION;
```
> 모든 IP접속에 허용을 할때에는 `%`로 지정합니다.
> 권한은 `스키마.테이블`로 설정합니다. 만일, `*.*`로 설정하게 되면 모든 스키마와 모든 테이블에 대해서 권한을 부여하게 됩니다.

패스워드 변경하기
```
ALTER USER 사용자명 IDENTIFIED WITH mysql_native_password BY 'yyyy';
```


Max-Connections 설정
```
show variables like '%max_connection%';
set global max_connections=100;
```


