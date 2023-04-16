---
layout: home
---

# Tomcat 서버
Apache Tomcat은 웹 애플리케이션 배포 및 관리를 위한 플랫폼을 제공하는 오픈 소스 Java 기반 웹 애플리케이션 서버입니다.

## 톰켓 서버란
Apache Tomcat은 Java 웹 애플리케이션을 배포하고 관리하는 데 사용되는 오픈 소스 웹 서버 및 서블릿 컨테이너 소프트웨어입니다. Linux를 포함한 많은 운영 체제에서 사용할 수 있습니다.


Java를 사용하여 웹 응용 프로그램을 개발하는 경우 웹 서버에서 호스팅해야 합니다. Apache Tomcat은 Java 커뮤니티에서 널리 사용되는 웹 서버 중 하나입니다. 정적 및 동적 웹 콘텐츠를 제공할 수 있으며 HTTP 및 HTTPS 프로토콜을 모두 처리할 수 있습니다.


Tomcat은 웹 서버, 서블릿 컨테이너 및 JSP 컨테이너를 비롯한 여러 구성 요소로 구성됩니다. 웹 서버 구성 요소는 HTTP 요청 및 응답 처리를 담당하고 서블릿 컨테이너는 Java 서블릿 및 JSP(JavaServer Pages) 관리를 담당합니다. JSP 컨테이너는 JSP 페이지를 Java 서블릿으로 컴파일하는 역할을 합니다.


Tomcat은 가볍고 사용하기 쉽도록 설계되었으며 Apache HTTP Server 또는 Apache Maven과 같은 다른 Apache 소프트웨어와 함께 자주 사용됩니다. 또한 Java Servlet API, JSP(JavaServer Pages), JSF(JavaServer Faces), WebSocket 등을 비롯한 광범위한 Java 기술을 지원합니다.


웹 콘텐츠를 제공하는 것 외에도 Tomcat은 JMX(Java Management Extensions), JMX 기반 도구 및 Tomcat Manager 웹 응용 프로그램과 같은 웹 응용 프로그램을 관리하고 모니터링하기 위한 여러 기능을 제공합니다.


전반적으로 Tomcat은 웹 응용 프로그램을 배포하고 관리하기 위해 Java 커뮤니티에서 널리 사용되는 대중적이고 강력한 웹 서버입니다. 오픈 소스이며 무료로 사용할 수 있으며 yum 또는 apt-get과 같은 패키지 관리자를 사용하여 Linux 시스템에 쉽게 설치할 수 있습니다.

## 톰켓 버젼
Apache Tomcat은 초기 버전 이후로 많은 릴리스를 제공했으며 각 릴리스에는 일반적으로 버그 수정, 새로운 기능, 성능 및 보안 개선 사항이 포함됩니다. 2023년 4월 `현재 안정적인 최신 Apache Tomcat 버전은 버전 10.x`입니다.

다음은 Apache Tomcat의 주요 릴리스에 대한 간략한 개요입니다.

* Tomcat 1.x: Apache Tomcat의 초기 버전은 1998년에 출시되었으며 Java Servlet API 1.0 및 JSP(JavaServer Pages) 1.1을 기반으로 합니다.

* Tomcat 3.x: 이 릴리스에서는 Java Servlet API 2.2 및 JSP 1.1에 대한 지원을 도입했습니다.

* Tomcat 4.x: 이 릴리스에서는 Java Servlet API 2.3 및 JSP 1.2에 대한 지원이 도입되었습니다. JSF(JavaServer Faces) 프레임워크에 대한 지원도 포함되었습니다.

* Tomcat 5.x: 이 릴리스에서는 Java Servlet API 2.4 및 JSP 2.0에 대한 지원을 도입했습니다. 또한 JPA(Java Persistence API)에 대한 지원도 포함되었습니다.

* Tomcat 6.x: 이 릴리스에서는 Java Servlet API 2.5 및 JSP 2.1에 대한 지원이 도입되었습니다. 또한 JMX(Java Management Extensions)에 대한 지원과 향상된 클러스터링 지원도 포함되었습니다.

* Tomcat 7.x: 이 릴리스에서는 Java Servlet API 3.0 및 JSP 2.2에 대한 지원을 도입했습니다. 또한 비동기 서블릿, 웹 조각 및 동적 구성에 대한 지원도 포함되었습니다.

* Tomcat 8.x: 이 릴리스에서는 Java Servlet API 3.1 및 JSP 2.3에 대한 지원이 도입되었습니다. 또한 비차단 I/O 및 WebSocket 프로토콜에 대한 지원도 포함되었습니다.

* Tomcat 9.x: 이 릴리스에서는 Java Servlet API 4.0 및 JSP 2.3에 대한 지원이 도입되었습니다. 또한 HTTP/2 및 JAAS(Java Authentication and Authorization Service)에 대한 지원도 포함되었습니다.

* Tomcat 10.x: 이 릴리스에서는 Java Servlet API 5.0 및 JSP 3.0에 대한 지원을 도입했습니다. 또한 성능 향상, 보안 향상 및 컨테이너화 지원 향상이 포함되었습니다.

Tomcat의 각 릴리스는 이전 릴리스를 기반으로 하며 Java 웹 응용 프로그램을 보다 쉽게 ​​개발하고 배포할 수 있도록 하는 새로운 기능과 개선 사항을 포함합니다. 개발자는 필요한 특징과 기능에 따라 필요에 가장 적합한 Tomcat 버전을 선택하고 필요에 따라 최신 버전으로 업그레이드할 수 있습니다.

## 톰켓 설치
리눅스에 톰켓을 설치합니다.

### 패키지로 tomcat9 설치하기
apt 명령어를 통하여 패키지로 컴파일된 tomcat9을 설치합니다.
* [tomcat9](tomcat9) with APT

### tomcat10 설치
공식사이트에서 최신의 tomcat10을 다운로드 받아 설치를 합니다.
* [tomcat10](tomcat10)

## 배포
* [deploy](deploy)

## Was연동
Tomcat과 Apache를 연결하여 Apache를 프런트 엔드 프록시 서버로 사용하여 정적 콘텐츠를 처리하고 동적 요청을 Tomcat에 전달함으로써 웹 애플리케이션의 성능과 확장성을 개선할 수 있습니다.

* [connector](connector)
    * [아파치-톰켓](connector/apache)
    * [엔진엑스-톰켁](connector/nginx)

## 학습과제
* [학습과제](learn)
