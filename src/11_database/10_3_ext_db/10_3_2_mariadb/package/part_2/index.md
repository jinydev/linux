---
layout: home
title: "MariaDB 최신버젼"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# MariaDB 최신버젼

## MariaDB 최신버젼
---
리눅스 패포판은 기본적으로 `최신 버젼`의 패키지를 제공하지 않습니다. 
최신의 mariadb를 설치하기 위해서는 목록을 갱신해 주어야 합니다.

저장소의 목록은 https://mariadb.org/download/#mariadb-repositories 에서 확인을 할 수 있습니다.

<!-- Broken Image Removed: ../../../../img/image-20210101152711026.png -->

Linux 패보판 운영체제와 설치하고자 하는 MaraiaDB 버젼을 선택합니다. 
그럼 입력해야 하는 목록을 자동적으로 생성해 줍니다. 이를 실행합니다.

```bash
$ sudo apt-get install software-properties-common dirmngr apt-transport-https
$ sudo apt-key adv --fetch-keys 'https://mariadb.org/mariadb_release_signing_key.asc'
$ sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] https://mirror.yongbok.net/mariadb/repo/10.5/ubuntu focal main'
```

새로운 패키지 저장소 목록을 추가했다면, 목록을 갱신합니다.

```bash
$ sudo apt update
```

<br>


---

[⬅️ 이전](../)
