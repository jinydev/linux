---
layout: home
title: "1. 사전 요구 사항 LAMP 스택"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 1. 사전 요구 사항 LAMP 스택

## 1. 사전 요구 사항 (LAMP 스택)

Nextcloud 구동을 위해 반드시 설치되어 있어야 하는 3가지입니다.

1. **웹 서버**: Apache 또는 Nginx (PHP 연동)
2. **PHP**: PHP 8.x 이상 및 주요 모듈들 (`php-xml`, `php-mbstring`, `php-curl`, `php-zip`, `php-gd` 등)
3. **DB 서버**: MySQL 또는 MariaDB

> 💡 **참고**: `dnf install -y httpd mariadb-server php php-mysqlnd php-gd php-xml php-mbstring php-zip php-curl` 로 일괄 설치 가능합니다.

---


---

[⬅️ 이전](../)
