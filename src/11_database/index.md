---
layout: home
title: 11.데이터베이스 구축하기
description: 리눅스 데이터베이스 구축. Mysql, MariaDB, PostgreSQL
keywords: linux, database, mysql, mariadb
---

## 11.[데이터베이스](/database) 구축하기
---
리눅스에 데이터베이스를 설치하고, 각종 응용 프로그램과 연동하여 서비스를 구동해 보도록 합니다.

### 11-1.데이터베이스란?
데이터베이스 서버에 대하여 좀더 자세히 알아 보도록 합니다.

* 데이터베이스의 종류
다양한 데이터베이스를 설치하고 사용을 해보도록 합니다.  

### 11-2.파일 기반형
SQLite는 경량화된 오픈소스 SQL 데이터베이스 관리 시스템으로, 서버가 필요하지 않으며 파일 기반의 데이터베이스로서 쉽게 이식성이 높은 솔루션으로 사용됩니다.
* [sqlight](/database/sqlight)

### 11-3.관계형
관계형 데이터베이스는 데이터를 테이블 형태로 정리하고, 이를 관계를 이용해 연결시켜 관리하는 데이터베이스 시스템입니다.

* [mysql](/database/mysql)
* [마리아db](/database/mariadb)
* [postgresql](/database/postgresql)
* [oracle](/database/oracle)

### 11-4.NoSQL
noSQL은 관계형 데이터베이스가 아닌 비관계형 데이터베이스를 말하며, 데이터 구조를 자유롭게 구성하고 확장성과 가용성을 높이기 위해 설계된 데이터베이스입니다.
* [몽고DB](/database/mongo)

### 11-5.In Memory 상주형
Redis와 Memcached는 모두 메모리 기반의 key-value 저장소로, 데이터를 캐싱하기 위해 사용되는 NoSQL 데이터베이스입니다.
* [redis](/database/redis)
* memcahe
