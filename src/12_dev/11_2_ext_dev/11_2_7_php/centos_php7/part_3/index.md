---
layout: home
title: "설치"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 설치

## 설치
CentOS는 기본적으로 오래된 PHP 5.4 버전을 지원합니다. 최신의 버전을 설치하기 위해서는 약간의 추가 작업이 필요로 합니다. 

먼저 yum 저장소를 추가합니다.
Remi CentOS 저장소를 추가합니다.

yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm

Disable Remi PHP 5.4 repository
By default, the repository for PHP 5.4 is enabled and hence, to install the latest version of PHP, you need to disable this repo. The repositories can be enabled or disabled using the yum-config-manager command. This command is provided with the yum-utils package.

yum install -y yum-utils
yum-config-manager --disable remi-php54
Enable Remi PHP 7.3 repository
To enable Remi PHP 7.3 repository, run the command below.

yum-config-manager --enable remi-php73

yum install php

설치를 확인합니다.

```
[root@jiny ~]# php -v
PHP 7.3.8 (cli) (built: Jul 30 2019 09:26:16) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.3.8, Copyright (c) 1998-2018 Zend Technologies

```


---

[⬅️ 이전](../)
