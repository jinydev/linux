---
layout: home
---

# Domain Name System
Linux 서버의 DNS는 도메인 이름을 IP 주소로 변환하여 네트워크의 리소스를 찾고 연결하는 서비스입니다.

* [dns란](dns)

## hosts 파일을 이용하여 네트워크 접속
* [window host](window)
* [linux host](window)


## 네임 서버를 이용하여 네트워크 접속

![image-20230409190253697](./img/image-20230409190253697.png)


* 기하급수적으로 늘어나는 네트워크 상의 컴퓨터에 대한 모든 IP 정보를 파일 하나에 기록하는 것은 무리

* 이름 해석(Name Resolution)을 전문적으로 해 주는 서버 컴퓨터가 필요해짐 (=DNS 서버 = 네임 서버) 

* 네임 서버는 인터넷에서 변화하는 모든 컴퓨터의 URL과 IP 정보를 실시간 제공

* 사용자는 URL만 외우면, ip주소를 몰라도 됨

![image-20230409190341296](./img/image-20230409190341296.png)


## NSLookup
nslookup 명령은 도메인 이름 및 IP 주소 정보에 대해 DNS 서버를 쿼리하는 데 사용되는 도구입니다. 

* [실습](nslookup)

## Host 동작실습
리눅스의 `/etc/hosts` 파일 수정하여, 우리가 일상적으로 사용하는 사이트의 ip를 조작해 봅니다.

실습목표
* /etc/hosts 파일의 작동을 이해한다.
* 네임 서버가 하는 기본적인 역할을 이해한다.
* IP주소를 얻기 위해 어떤 순서로 작동하는지 확인한다.

Domain name과 ip를 바꿔보자.

* [www.naver.com](http://www.naver.com/)의 ip을
   [www.daum.net](http://www.daum.net/)로 변경

결과 화면 (엉뚱한 사이트로 접속)
![image-20230409190518150](./img/image-20230409190518150.png)



## IP주소를 얻는 내부 흐름

![image-20230409190540106](./img/image-20230409190540106.png)

Order hosts,bind hosts 먼저 조회하고, 그 후에 resolv.conf를 본다는 의미


## 도메인 이름 체계
* [domain](domain)


## 로컬 네임 서버가 작동하는 순서

* PC가 사용하는 네임 서버가 `/etc/resolv.conf` 파일에 `nameserver IP주소`로 설정되어 있는데, 
   이 네임 서버를 로컬 네임 서버라고 부름

* 그래서 www.nate.com의 IP주소를 요구하면 이 로컬 네임 서버에 질문을 함

* 로컬 네임 서버가 혼자서 모든 컴퓨터 도메인 이름을 관리할 수는 없기 때문에, 다음처럼 동작

![image-20230409190734514](./img/image-20230409190734514.png)

![image-20230409190748855](./img/image-20230409190748855.png)


