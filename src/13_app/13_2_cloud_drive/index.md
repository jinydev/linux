---
layout: home
title: "13.2 오픈소스 클라우드 스토리지 (Nextcloud)"
---

# 13.2 사설 클라우드 드라이브 구축 (Nextcloud)

[Nextcloud(넥스트클라우드)](https://nextcloud.com/)는 PHP와 데이터베이스(MySQL/MariaDB)를 기반으로 구동되는 세계 1위의 강력한 오픈소스 클라우드 스토리지입니다. 구글 드라이브(Google Drive)나 드롭박스(Dropbox)와 동일한 파일 동기화, 공유, 협업 기능을 여러분의 개인 리눅스 서버에 완전히 독립적으로 구성할 수 있습니다. 

이번 챕터에서는 앞서 배운 [9장 웹 서비스(Apache/PHP)] 와 [10장 데이터베이스(MariaDB)] 지식을 응용하여 Nextcloud를 인스톨해 봅니다.

---

## 1. 사전 요구 사항 (LAMP 스택)

Nextcloud 구동을 위해 반드시 설치되어 있어야 하는 3가지입니다.

1. **웹 서버**: Apache 또는 Nginx (PHP 연동)
2. **PHP**: PHP 8.x 이상 및 주요 모듈들 (`php-xml`, `php-mbstring`, `php-curl`, `php-zip`, `php-gd` 등)
3. **DB 서버**: MySQL 또는 MariaDB

> 💡 **참고**: `dnf install -y httpd mariadb-server php php-mysqlnd php-gd php-xml php-mbstring php-zip php-curl` 로 일괄 설치 가능합니다.

---

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

## 3. Nextcloud 다운로드 및 배치

공식 홈페이지에서 아카이브 압축 파일을 다운로드하여 웹 서버 경로(`DocumentRoot`)로 이동시킵니다.

```bash
# wget으로 최신 zip/tar 형태의 릴리즈 다운로드
wget https://download.nextcloud.com/server/releases/latest.zip

# 압축 해제
unzip latest.zip

# 아파치 루트 디렉토리(/var/www/html)로 폴더 이동
sudo mv nextcloud /var/www/html/

# (중요) 웹 서버 데몬이 파일들을 수정/저장할 수 있도록 소유권(chown) 전부 위임!
sudo chown -R apache:apache /var/www/html/nextcloud
```
> [!CAUTION] 
> 소유권(`chown`) 변경을 생략하면, 브라우저에서 접속 시 디렉토리 쓰기 불가능 에러로 인해 설치 화면이 뜨지 않습니다.

---

## 4. 웹 인스톨러 구동 및 완료

서버의 IP가 `192.168.0.100` 이라고 가정할 때, 브라우저 주소창에 다음을 입력하여 접속합니다.
* **접속 주소**: `http://192.168.0.100/nextcloud`

### 입력 옵션 지침
접속하면 표시되는 화려한 설치 마법사 화면에 다음과 같이 기입합니다.
1. **관리자 계정 만들기**: 본인이 사용할 영문 ID와 비밀번호를 자유롭게 기입합니다.
2. **데이터 폴더**: `/var/www/html/nextcloud/data` (자동 입력됨. 실제 하드 용량이 큰 경로로 변경 가능)
3. **데이터베이스 설정**: 앞서 2단계에서 생성한 정보를 넣습니다.
   * 사용자: `next_user`
   * 암호: `강력한비밀번호`
   * DB이름: `nextcloud_db`
   * 호스트: `localhost`

[설치 완료] 버튼을 누르면 DB 스키마가 자동 생성되고 나만의 사설 클라우드 드라이브가 완성됩니다! PC용, 모바일용 동기화 앱도 지원하므로 실생활에 즉시 활용해보세요.
