---
layout: home
---
# Mysql
Mysql을 설치하고 접속하는 방법에 대해서 학습합니다.  

## Mysql이란


## 설치
래드햇 계열의 경우 `yum`을 통하여 mysql을 설치 가능합니다.
* [yum 설치](/database/mysql/yum)

우부툰 계열의 경우 `apt`을 통하여 mysql을 설치 가능합니다.
* [apt 설치](/database/mysql/apt)


## 실행 및 재시작
mysql을 설치한 후에는 별도로 명령을 입력하여 서버를 실행해 주어야 합니다. `service` 또는 `systemctl` 명령을 통하여 서비스 데모을 실행할 수 있습니다. 

* [서비스 실행](service)


## 보완설정 및 접속
* [패스워드 설정](/database/mysql/password)

### 외부접속 허용
Localhost 외의 외부 IP에서 mysql에 접속을 하기 위해서는 추가 환경설정을 변경해 주어야 합니다.

## 접속
* [콘솔 접속](/database/mysql/client)

`MysqlWorkBench`는 GUI 방식으로 mysql 데이터베이스에 접속을 관리하는 클리이언트 입니다.
* [workbench](/database/client/mysqlworkbench) 설치 및 실행하기

DBEver는 mysql 말고도 다양한 데이터베이스에 접속하여 관리할 수 있습니다.
* [dbever](/database/client/dbeaver) 설치 및 실행하기

HeidiSQL은 윈도우용 mysql을 설치하면 같이 설치가 됩니다.
* [HeidiSQL 설치하기](/database/client/heidisql)