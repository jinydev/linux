---
layout: home
title: 10.웹 서버스
description: 아파치, nginx 웹 서버 운영
keywords: linux, web, apache, nginx, https
---

## 10.웹 서버스
---
리눅스의 웹 서비스는 Apache, Nginx 등의 웹 서버 소프트웨어를 사용하여 다양한 웹 사이트 및 웹 어플리케이션을 호스팅하고 제공합니다.

### 10-1.web 서버란
웹 서버는 인터넷 상에서 HTTP를 통해 클라이언트의 요청에 응답하여 웹 페이지나 파일 등을 제공하는 컴퓨터 프로그램입니다.

* [웹서비스란?](/web/service)

#### 리눅스 웹서버
* [Web Server의 역할](/web/server)
* [Web server의 장점](/web/server)
* [웹 서버의 종류](/web/server)


### 10-2.아파치
아파치 웹서버는 가장 대중적인 오픈 소스 웹서버로, HTML 문서 및 웹 페이지를 제공하는 소프트웨어입니다.  

* [아파치란](/web/apache)
* [apt로 설치하기](/web/apache/apt) 
우분투 환경에서 아파치 웹서버를 설치하는 방법에 대해서 알아 봅니다.
* [yum으로 설치하기](/web/apache/yum) 
centOS 환경에서 설치하는 방법에 대해서 알아 봅니다.
* [아파치 설정](/web/apache/conf)


### 10-3.엔진엑스
엔진엑스 웹서버는 가벼우면서도 고성능인 웹 서버로, 동시접속자가 많은 웹사이트나 애플리케이션의 처리에 적합한 소프트웨어입니다.

* [nginx란](/web/nginx)
  * [apt로 설치하기](/web/nginx/apt) 
  * [yum로 설치하기](/web/nginx/yum) 
  * [nginx 설정](/web/nginx/conf)


### 10-4.도메인 설정 및 보완
HTTPS는 데이터를 암호화하여 보안을 유지하므로, 웹사이트에서 민감한 정보를 주고받거나 사용자 인증과 같은 중요한 작업을 수행하는 경우 반드시 사용해야 합니다.

* SSH 서버와 클라이언트

#### HTTPS
* [https란](/web/https)

#### 보안 및 인증서
* SSL 인증서 설치와 설정
* [Let's Encription](/web/https/letsEncription)








### 10-5.Was서버
서버에서 WAS(Web Application Server)란, 웹 애플리케이션을 실행하는 미들웨어로, 웹 서버와 데이터베이스 서버 사이에서 동작하여 애플리케이션의 로직 수행 및 데이터 처리를 담당하는 소프트웨어입니다.  

* [was란](/web/was)
* [was의 역할](/web/was)

### 10-6.연동설정
Web 서버는 정적인 파일 제공과 로드 밸런싱 등의 역할을, WAS는 동적인 데이터 처리와 비즈니스 로직 수행을 담당하여 서로 보완적인 역할을 합니다.

#### [톰켓서버](/web/was/tomcat)
Apache Tomcat은 웹 애플리케이션 배포 및 관리를 위한 플랫폼을 제공하는 오픈 소스 Java 기반 웹 애플리케이션 서버입니다.  
> 톰켓이 실행되기 위해서는 [java가 설치](/dev/java)되어 있어야 합니다.

* [톰켓 버젼](/web/was/tomcat)
  * [tomcat9](/web/was/tomcat/tomcat9) 패키지 설치 방법
  * [tomcat10](/web/was/tomcat/tomcat10) 다운로드 설치 방법

* WAS 연동 및 배포하기  
Tomcat과 Apache를 연결하여 Apache를 프런트 엔드 프록시 서버로 사용하여 정적 콘텐츠를 처리하고 동적 요청을 Tomcat에 전달함으로써 웹 애플리케이션의 성능과 확장성을 개선할 수 있습니다.
  * [deploy](/web/was/tomcat/deploy)
  * [connector](/web/was/tomcat/connector)
    * [아파치연동](/web/was/tomcat/connector/apache)
    * [Nginx연동](/web/was/tomcat/connector/nginx)

#### Weblogic
> 실습 : Weblogic 설치 해보자
