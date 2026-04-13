---
layout: home
---

# Mysql 서비스
systemd를 통하여 mysqld 서비스를 실행합니다.

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

