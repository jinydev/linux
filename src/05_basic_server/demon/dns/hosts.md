---
layout: home
---

# hosts 파일을 이용하여 네트워크 접속
인터넷에 연결된 컴퓨터가 수십 ~ 수백대로 늘어남에 따라서 `hosts` 파일에 URL과 IP주소를 매핑하여 기록해 놓는 방식을 사용합니다.

* 예)  102.54.94.97 naver.com
* 38.25.63.10  google.com
* 127.0.0.1 localhost

## Windows의 경우
Windows 호스트 파일은 호스트 이름을 IP 주소에 매핑하는 C:\Windows\system32\drivers\etc\hosts에 있는 텍스트 파일입니다. 사용자가 웹 사이트나 서버에 액세스하려고 할 때 운영 체제에서 도메인 이름을 IP 주소로 확인하는 데 사용됩니다.  

```
C:\Windows\system32\drivers\etc\hosts
```
사용자가 웹 브라우저에 URL을 입력하거나 네트워크 리소스에 액세스하면 운영 체제는 먼저 호스트 파일을 확인하여 호스트 이름이 나열되어 있는지 확인합니다. 호스트 이름이 나열되면 운영 체제는 해당 IP 주소를 사용하여 서버 또는 리소스에 연결합니다. 호스트 이름이 나열되지 않은 경우 운영 체제는 IP 주소를 얻기 위해 DNS 서버를 쿼리합니다.


메모장과 같은 텍스트 편집기로 호스트 파일을 편집하여 호스트 이름-IP 주소 매핑을 추가하거나 수정할 수 있습니다. 이는 웹 애플리케이션을 테스트하거나 DNS 서버에 의해 차단된 웹 사이트 또는 리소스에 액세스하는 데 유용할 수 있습니다.

다음과 같이 설정을 참조 합니다.
```
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost

127.0.0.1 12753 #Samsung Analytics

192.168.56.114 jinydev.com
```

호스트 파일을 수정하려면 관리 권한이 필요하며 호스트 파일에 대한 변경 사항은 즉시 적용됩니다. 또한 호스트 파일에 실수가 있으면 네트워크 연결 문제가 발생할 수 있으므로 수정하기 전에 원래 호스트 파일을 백업하는 것이 중요합니다.  

## 리눅스의 경우
Linux의 /etc/hosts 파일은 호스트 이름에 대한 IP 주소 매핑이 포함된 일반 텍스트 파일입니다. Windows 호스트 파일과 마찬가지로 운영 체제에서 도메인 이름을 IP 주소로 확인하는 데 사용됩니다.  

```
/etc/hosts
```

사용자가 도메인 이름을 사용하여 웹 사이트나 서버에 액세스하려고 하면 운영 체제는 먼저 /etc/hosts 파일을 확인하여 도메인 이름이 나열되어 있는지 확인합니다. 도메인 이름이 나열되면 운영 체제는 해당 IP 주소를 사용하여 서버 또는 리소스에 연결합니다. 도메인 이름이 나열되지 않으면 운영 체제는 DNS 서버를 쿼리하여 IP 주소를 얻습니다.


vim 또는 nano와 같은 텍스트 편집기로 /etc/hosts 파일을 편집하여 호스트 이름-IP 주소 매핑을 추가하거나 수정할 수 있습니다. 이는 웹 애플리케이션을 테스트하거나 DNS 서버에 의해 차단된 웹 사이트 또는 리소스에 액세스하는 데 유용할 수 있습니다.


/etc/hosts 파일에 대한 수정 사항은 즉시 적용되며 파일에 실수가 있으면 네트워크 연결 문제가 발생할 수 있습니다. 따라서 수정하기 전에 원본 /etc/hosts 파일을 백업하는 것이 좋습니다. 또한 /etc/hosts 파일을 편집하려면 관리 권한이 필요합니다.