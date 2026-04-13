---
layout: home
---

# Mysql 패스워드 설정
데이터베이스 보완을 위하여 비밀번호를 설정합니다.

## 최초 비밀번호 확인

mysql은 보안을 위하여 `임시 비밀번호` 설정되어 있습니다. 임시 비밀번호는 `/var/log/mysqld.log` 안에 숨겨져서 기록이 되어 있습니다.

```
`grep` 명령어를 통하여 `temporary password`를 찾아 봅니다.
```

## 보안설정 실행
`mysql_secure_installation`은 데이터베이스 보안을 위한 비밀번호 및 설정 프로그램입니다. 

```
$sudo mysql_secure_installation 
```
> 최초의 비밀번호를 물어 보게 됩니다. grep을 찾은 `임시 비밀번호`를 입력합니다.


새로운 비밀번호를 설정합니다. 다음과 같은 과정을 따라 입력해 주세요.

```
hojin@hojin:~$ sudo mysql_secure_installation

NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!

In order to log into MariaDB to secure it, we'll need the current
password for the root user. If you've just installed MariaDB, and
haven't set the root password yet, you should just press enter here.

Enter current password for root (enter for none):
OK, successfully used password, moving on...

Setting the root password or using the unix_socket ensures that nobody
can log into the MariaDB root user without the proper authorisation.

You already have your root account protected, so you can safely answer 'n'.

Switch to unix_socket authentication [Y/n]
Enabled successfully!
Reloading privilege tables..
 ... Success!


You already have your root account protected, so you can safely answer 'n'.

Change the root password? [Y/n]
New password:
Re-enter new password:
Password updated successfully!
Reloading privilege tables..
 ... Success!
```
> 비밀번호를 설정할때는 `대문자`, `특수문자`, `숫자`를 같이 혼용하여 만들어야 합니다.

테스트를 위한 익명 사용자를 허용할 것인지를 설정합니다. `y`를 선택하여 익명 사용자를 제외합니다.
```
By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.

Remove anonymous users? [Y/n]
 ... Success!
```

원격지에서 리모트로 연결하는 것을 허용할 것인지를 선택합니다.
```
Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.

Disallow root login remotely? [Y/n]
 ... Success!
```
> 실제 서비스를 운영하는 경우에는 `n`를 선택합니다.


테스트 데이터베이스를 남겨둘 것인지를 물어봅니다. `y`를 선택하여 테스트 데이터도 같이 삭제를 합니다. 
```
By default, MariaDB comes with a database named 'test' that anyone can
access.  This is also intended only for testing, and should be removed
before moving into a production environment.

Remove test database and access to it? [Y/n]
 - Dropping test database...
 ... Success!
 - Removing privileges on test database...
 ... Success!
```

권환 테이블을 갱신할 것인지를 물어봅니다.
```
Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.

Reload privilege tables now? [Y/n]
 ... Success!

Cleaning up...

All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.

Thanks for using MariaDB!
hojin@hojin:~$
```

