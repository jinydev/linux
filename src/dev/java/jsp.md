---
layout: home
typora-copy-images-to: ./img
---

# 톰켓 및 jsp 테스트

`/var/lib/tomcat10/webapps/ROOT/`에 jsp 코드를 작성합니다.

```jsp
<!DOCTYPE html>
<html>
<head>
	<title>Hello World</title>
</head>
<body>
	<h1>Hello World!</h1>
	<p>This is a JSP page running on Apache Tomcat.</p>
	<p>Current date and time is <%= new java.util.Date() %>.</p>
</body>
</html>
```

웹 브라우저에서 http://localhost:8080/hello.jsp로 이동합니다. 간단한 "Hello World!"가 표시되어야 합니다. 현재 날짜 및 시간과 함께 메시지.




## JSP
JSP는 JAVA언어를 기반으로 국내 SI 프로젝트에서 주로 사용되는 웹개발 방식 입니다.
> https://blog.lael.be/post/858

## 자바버젼
JSP 프로젝트는 JAVA 버전에 영향을 많이 받는다. 


## 자바 컴파일 과정

> https://velog.io/@0sunset0/%EC%9E%90%EB%B0%94-%EC%BB%B4%ED%8C%8C%EC%9D%BC-%EA%B3%BC%EC%A0%95-%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC%EC%99%80-%EC%9D%B8%ED%84%B0%ED%94%84%EB%A6%AC%ED%84%B0-%EC%B0%A8%EC%9D%B4
