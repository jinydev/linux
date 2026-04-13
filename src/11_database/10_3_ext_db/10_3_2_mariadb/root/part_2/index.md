---
layout: home
title: "mysql root 비빌번호 분실"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# mysql root 비빌번호 분실

## mysql root 비빌번호 분실
---
root 비밀번호를 분실한 경우 다음과 같이 재설정한다.

####  step1. mysqld 중지
먼저 마리아DB 서버데몬을 중지합니다.

```
$ sudo systemctl stop mariadb
```

마리아DB를 `안전 모드`로 실행을 합니다. 
다음과 같이 mysql_safe 스크립트를 통하여 실행이 가능합니다.

```
$ sudo /usr/bin/mysqld_safe --skip-grant &
```

> `&` 표시를 같이하게 되면, `백그라운드` 모드로 마리아DB가 실행이 됩니다.

#### step2. root계정 비밀번호 변경

백그라운드로 실행되는 마리아DB에 접속을 합니다. 이때 패스워드는 지정하지 않아도 됩니다.

```
$ sudo mysql -u root
```

sql 쿼리를 이용하여 root 사용자의 패스워드를 변경합니다.

```
MariaDB [mysql]> update user set password=password('변경할 비밀번호') where user='root';
MariaDB [mysql]> flush privileges;
MariaDB [mysql]> exit;
```
 

#### step3. 접속 확인
변경한 패스워드를 이용하여 접속을 테스트 해봅니다.

```
mysql -uroot -p
Enter password:
MariaDB [(none)]> 
```
 

#### step4. 서비스 재시작
root 비밀번호가 잘 변경이 되었다면, 마리아DB를 재실행 합니다.

```
$ sudo systemctl stop mariadb
$ sudo systemctl start mariadb
```

---

[⬅️ 이전: 마리아DB 패키지 설치](../package/) &nbsp;|&nbsp; [🏠 분류 목차](../../../../) &nbsp;|&nbsp; [다음: 시작/정지/상태/활성화 ➡️](../service/)


---

[⬅️ 이전](../)
