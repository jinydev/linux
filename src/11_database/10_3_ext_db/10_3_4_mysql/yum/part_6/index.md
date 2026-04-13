---
layout: home
title: "테스트 데이터베이스 만들기"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 테스트 데이터베이스 만들기

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

---

[⬅️ 이전: WorkBench](../workbench/) &nbsp;|&nbsp; [🏠 분류 목차](../../../../) &nbsp;|&nbsp; [다음: Oracle ➡️](../../10_3_5_oracle/)


---

[⬅️ 이전](../)
