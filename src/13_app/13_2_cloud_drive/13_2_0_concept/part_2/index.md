---
layout: home
title: "2. 데이터베이스 구성 MariaDB"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 2. 데이터베이스 구성 MariaDB

## 2. 데이터베이스 구성 (MariaDB)

웹 브라우저로 설치하기 전, Nextcloud가 사용자 파일 정보를 저장할 DB와 DB계정을 생성해야 합니다.

```bash
# DB 관리자로 접속
mysql -u root -p

# DB 쿼리 실행
MariaDB> CREATE DATABASE nextcloud_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
MariaDB> CREATE USER 'next_user'@'localhost' IDENTIFIED BY '강력한비밀번호';
MariaDB> GRANT ALL PRIVILEGES ON nextcloud_db.* TO 'next_user'@'localhost';
MariaDB> FLUSH PRIVILEGES;
MariaDB> EXIT;
```

---


---

[⬅️ 이전](../)
