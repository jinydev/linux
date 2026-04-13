---
layout: home
title: "추가설치"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 추가설치

## 추가설치
yum list php-*
yum install php-<extension_name>

yum install php-mysql php-pdo

```
# rpm -Uvh http://rpms.remirepo.net/enterprise/remi-release-7.rpm
[root@jiny ~]# rpm -Uvh http://rpms.remirepo.net/enterprise/remi-release-7.rpm
Retrieving http://rpms.remirepo.net/enterprise/remi-release-7.rpm
warning: /var/tmp/rpm-tmp.raA66z: Header V4 DSA/SHA1 Signature, key ID 00f97f56: NOKEY
error: Failed dependencies:
        epel-release = 7 is needed by remi-release-7.6-2.el7.remi.noarch

```

Install yum-utils as we need the yum-config-manager utility.

```
yum install yum-utils
```

그리고 yum을 최신으로 업데이트 합니다.

```
yum update
```

Now you have to chose which PHP version you want to use on the server. If you like to use PHP 5.4, then proceed to chapter 4.1. To install PHP 7.0, follow the commands in chapter 4.2, for PHP 7.1 chapter 4.3, for PHP 7.4 use chapter 4.4 and for PHP 7.3 follow chapter 4.5 instead. Follow just one of the 4.x chapters and not all of them as you can only use one PHP version at a time with Apache mod_php.

### php 5.4
권장하지 않습니다. 기본적으로 설치되어 있는 오래된 버전입니다. 

```
# yum install php
```
명령을 입력하면 설치할 수 있습니다.

### 7.0
We can install PHP 7.0 and the Apache PHP 7.0 module as follows:

```
yum-config-manager --enable remi-php70
yum install php php-opcache
```

### 7.1
If you want to use PHP 7.1 instead, use:

```
yum-config-manager --enable remi-php71
yum install php php-opcache
```

### 7.3
If you want to use PHP 7.3 instead, use:

```
# yum-config-manager --enable remi-php73
# yum install php php-opcache
```


---

[⬅️ 이전](../)
