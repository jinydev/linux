---
layout: home
title: "실습 login Servlet"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# 실습 login Servlet

## 실습: login Servlet

login servlet 실행

```
http://localhost:8080/MyFirstApp/index.html
http://localhost:8080/MyFirstApp
```

![image-20230324155527261](../../img/image-20230324155527261.png)

GET 방식으로 전

http://localhost:8080/MyFirstApp/login?id=heejinlee&passwd=passwd

![image-20230324155547670](../../img/image-20230324155547670.png)

Servlet 을 작성해 보자

* New- Dynamic Web Project
  - Generate web.xml

![image-20230324155642643](../../img/image-20230324155642643.png)

WebContent/index.html

```
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title> MyFirstApp-Login </title>
</head>
<body>

<h1> Login </h1>
<form action="login" method="get">
<label id= "id_id"> ID   : </label> 
<input type ="text" id="id_id" name="id" /><br>
<label id= "id_passwd"> PASSWD  : </label> 
<input type ="text" id="id_passwd" name="passwd"/><br>
<input type ="submit" value ="로그인"/>
</form>

</body>
</html>
```

Src/LoginServlet.java

```
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
// TODO Auto-generated method stub

String id = request.getParameter("id");
String passwd = request.getParameter("passwd");

response.setContentType("text/html;charset=euc-kr");
PrintWriter out = response.getWriter();
out.println("ID : " + id +"<br>");
out.println("PASSWORD : " + passwd + "<br>");

response.getWriter().append("Served at: ").append(request.getContextPath());
}

```

WebContent/WEB-INF/web.xml

Web.xml 에 servlet mapping 넣어줌

```
……  
 <welcome-file-list>
    <welcome-file>index.html</welcome-file> 	
	……
 </welcome-file-list>

  <servlet>
  	<servlet-name>LoginServlet</servlet-name>
  	<servlet-class>kopo.ac.kr.LoginServlet</servlet-class>
  </servlet>
  
  <servlet-mapping>
  	<servlet-name>LoginServlet</servlet-name>
  	<url-pattern>/login</url-pattern>
  </servlet-mapping> 
</web-app>

```

![image-20230324160114838](../../img/image-20230324160114838.png)

Servlet을 호출할 때, Tomcat의 주소를 쓰지 않아도 된다.

* Tomcat의 주소가 노출되지 않음. Ip, port모두

* Tomcat의 주소가 변경가능 


---

[⬅️ 이전](../)
