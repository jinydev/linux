---
layout: home
title: "apache와 tomcat 둘다 활용"
---

[⬅️ 이전](../) &nbsp;|&nbsp; [🏠 분류 목차](../../../)

# apache와 tomcat 둘다 활용

## apache와 tomcat 둘다 활용

* DocumentRoot는 apache에서 처리.

* MyFirstApp은 Tomcat인 ajp13_Worker가 처리 

![image-20230324160222530](../../img/image-20230324160222530.png)

* Apache
  - Index.html
    - Static file, apache document root 하위의 directory에 대한 Link들

* * [http://localhost](http://localhost/) 접속하면 apache의 index.html이 보임

* Tomcat
  * MyFirstApp deploy
  * Greeting deploy 

* 설정
  * MyFirstApp, Greeting인 경우 tomcat으로 요청 보내기
  * 나머지는 apache에서 담당

Greeting app

* 인사와 시간을 찍어주는 servlet 하나만 존재

![image-20230324160425908](../../img/image-20230324160425908.png)

![image-20230324160435093](../../img/image-20230324160435093.png)

Greeting app

* Src/HiServlet.java

```
protected void doGet
(HttpServletRequest request, HttpServletResponse response) 
throws ServletException, IOException {
// TODO Auto-generated method stub

SimpleDateFormat format1 =
 			 new SimpleDateFormat ( "yyyy-MM-dd HH:mm:ss"); 
Date time = new Date();
String time1 = format1.format(time); 

response.getWriter().println("\n  Hi !!! \n");
response.getWriter().println(time1);

response.getWriter().append("\n Served at: ")	.append(request.getContextPath()); 
 
}
```

* WEB-INF/Web.xml

```
<servlet>
  <servlet-name>HiServlet</servlet-name>
  <servlet-class> kopo.ac.kr.HiServlet </servlet-class>
</servlet>
  
<servlet-mapping>
  <servlet-name>HiServlet</servlet-name>
  <url-pattern>/hi</url-pattern>
</servlet-mapping>

```

WebContent/greeting.html

* 동작 확인용

![image-20230324160615908](../../img/image-20230324160615908.png)

Apache Document Root에 index.html과 directory 추가

* dir 추가

* MyFirstApp, Greeting 추가 – 요청이 tomcat으로 가는지, apache로 오는지 확인

![image-20230324160654718](../../img/image-20230324160654718.png)

Apache Document root/index.html

```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>Hello Hello</title>
</head>
<body> 
<p> <a href="index2.html">index2.html in the same directory</a> </p>
<p> <a href="/MyFirstApp/">Login</a>  </p> 
<p> <a href="/Greeting/">context path가 Greeting인 경우 - index.html이 없어서 동작 안함</a>  </p>
<p> <a href="/Greeting/greeting.html">/Greeting/greeting.html 실행 - 정상 동작</a></p>
<p> <a href="/Greeting/hi">/Greeting/hi 실행 - 정상 동작</a>  </p>
<p> <a href="/Greeting/abc.html">apache에는 존재하는 Greeting/abc.html - 동작 안함</a></p> 
<p> <a href="/dir">index.html in the director "dir"- Apache - 정상 동작</a></p>
</body>
</html>

```

War는 compile된 java 코드인 class로 이루어짐.

War로 배포시 java source code를 같이 배포하지 않는경우가 대부분

* 보안상의 문제 – 코드를 알면 취약점 파악 용이
* 회사 대외비 – 코드를 알면 원천 기술 공개되므로 (solution 회사들)

Java Decompiler

* Class로 이루어진 war를 java source file로 볼수 있게 해주는 것

* http://java-decompiler.github.io/

![image-20230324161326128](../../img/image-20230324161326128.png)

---

[⬅️ 이전: Java8 (Yum)](../8/yum/) &nbsp;|&nbsp; [🏠 분류 목차](../../../../) &nbsp;|&nbsp; [다음: 톰켓 및 jsp 테스트 ➡️](../jsp/)


---

[⬅️ 이전](../)
