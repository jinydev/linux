---
layout: home
---

# Apache Tomcat

## Tomcat 이란

웹 애플리케이션 배포 및 관리를 위한 플랫폼을 제공하는 오픈소스 JAVA 기반 웹 애플리케이션 서버

- 오픈 소스 웹 서버 및 서블릿 컨테이너 소프트웨어로 많은 운영체제에서 사용 가능
- 정적 및 동적 웹 콘텐츠를 제공할 수 있으며 HTTP 및 HTTPS 프로토콜을 모두 처리 가능
- 웹 응용 프로그램을 배포하고 관리하기 위해 커뮤니티에서 널리 사용되는 대중적인 웹 서버

Tomcat은 웹 서버, 서블릿 컨테이너, JSP 컨테이너를 비롯한 여러 구성 요소로 구성됨

- 웹 서버 구성요소: HTTP 요청 및 응답 처리 담당
- 서블릿 컨테이너: Java 서블릿 및 JSP 관리를 담당
- JSP 컨테이너: JSP 페이지를 Java 서블릿으로 컴파일 하는 역할

*서블릿: Java를 이용하여 웹 페이지를 동적으로 생성하는 서버측 프로그램

### 아파치 vs 톰캣

Apache는 Web Server이고, Tomcat은 WAS인 것을 기억하자

Web Server: 정적인 데이터 처리하는 서버
단순 이미지나 html파일과 같은 http 요청을 처리하는 웹 서버

WAS(Web Applicataion Server): 동적인 데이터 처리 서버
클라이언트 요청을 받아 요청을 처리하고 다시 클라이언트에게 응답해주는 역할

[https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fq7Z09%2Fbtq0NwrPm5t%2F2JxFBzxS1O4Ww80uFY0Etk%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fq7Z09%2Fbtq0NwrPm5t%2F2JxFBzxS1O4Ww80uFY0Etk%2Fimg.png) 

**정리**

- 

|  | 장점 | 단점 |
| --- | --- | --- |
| Apache | 처리 속도가 빠르다. 구조가 단순하여 비용 절감. | 정적인 데이터만 처리 가능. 다른 서비스와 상호작용 불가 |
| Tomcat | 데이터 흐름이 유동적. DB 등 여러 서비스 가능. | 아파치에 비해 속도가 느림. 부가적인 비용 발생. 트래픽 과부하에 약함 |