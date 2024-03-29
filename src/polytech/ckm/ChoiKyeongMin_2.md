---
layout : home
---
# Choi Kyeong Min Report
# 정적페이지 vs 동적페이지

## **정적 페이지**

- 저장된 그대로 사용자에게 전달되는 웹 페이지입니다.
- 서버에 저장된 데이터가 변경되지 않는 한 사용자는 고정된 웹 페이지를 보게 됩니다.
- 정적 웹 페이지들은 업데이트를 전혀 하지 않거나 거의 할 필요가 없는 내용에 적절합니다.
- 저장된 데이터만 보여줄 수 있어 서비스가 한정적입니다.
- 삽입/수정/삭제 등의 작업이 모두 수동적이므로 관리가 힘듭니다.

## **동적 페이지**

- 서버가 사용자의 요청에 대하여 데이터를 가공한 후 생성되는 웹 페이지입니다.
- 사용자의 상황, 시간, 요청 등에 따라 달라지는 웹 페이지를 보게 됩니다.
- 같은 페이지라도 사용자마다 다른 결과의 웹 페이지를 볼 수 있습니다.
- 웹 사이트의 구조에 따라 삽입/수정/삭제 등의 작업이 용이 합니다.
- 정적 페이지에 비해 속도가 느립니다.

## **차이점**

- **정적 페이지**
    - 웹 서버만 있으면된다.
    - 저장되어있는 것을 보여주기때문에 속도가 빠르다.
- **동적 페이지**
    - 웹 서버 + 웹 어플리케이션 서버가 필요하다.
    - 정적 페이지에 비해 많은 메모리를 소비하여 속도가 느리다.

**웹 서버**

- 웹 클라이언트의 요청을 받아서 요청을 처리하고 그 결과를 웹 클라이언트에게 응답한다.
- HTML, CSS, JS(JavaScript), 이미지를 웹 클라이언트에게 제공할때 사용한다.
- 웹 브라우저와 같은 클라이언트로부터 HTTP요청을 받아들이고, HTML 문서와 같은 웹 페이지를 반환한다.

**웹 애플리케이션 서버**(Web Application Server, **WAS**)

- 웹 애플리케이션과 서버 환경을 만들어 동작시키는 기능을 제공하는 소프트웨어 프레임워크이다.
- 아파치 톰캣(Apache Tomcat), 레진(Resi), 제이런(JRun) 등이 있다.
- 영어권에서는 Application Server 약자 AS로 불린다.
- 웹 서버로부터 동적 페이지를 요청받아 요청을 처리하고 그 결과를 웹서버로 보여준다.

![https://blog.kakaocdn.net/dn/d39Ziz/btqBVgsBlRt/tb2tj2ZO3gJiKGldfrVV90/img.png](https://blog.kakaocdn.net/dn/d39Ziz/btqBVgsBlRt/tb2tj2ZO3gJiKGldfrVV90/img.png)

                       <애플리케이션 서버 방식의 요청 처리>

- 웹 애플리케이션 서버를 통해서 간접적으로 웹 애플리케이션 프로그램을 실행한다.
- 웹 애플리케이션 서버는 애플리케이션 프로그램의 실행 결과를 웹 서버에 전달해주며, 웹 서버는 웹 애플리케이션 서버로부터 전달받은  응답 결과를 웹 클라이언트에 전송한다.

![https://blog.kakaocdn.net/dn/cptsvf/btqBRvLtpmu/tARtYVOKQ9WpbAMHE7kVfk/img.png](https://blog.kakaocdn.net/dn/cptsvf/btqBRvLtpmu/tARtYVOKQ9WpbAMHE7kVfk/img.png)

                      <애플리케이션 서버 방식에서의 서버 간 구성도>

### **Web Server와 Web Application Server(WAS)를 구분하는 이유**

1. WAS는 DB 조회나 다양한 로직 처리를 담당하고 단순한 정적 컨텐츠는 Web Server에서 제공하도록 기능을 분리하여 서버 부하 방지의 효과가 있습니다.
2. SSL에 대한 암복호화 처리에 Web Server를 사용하여 물리적으로 분리하여 보안 강화할 수 있습니다.
3. 특히 대용량 웹 어플리케이션의 경우(여러 개의 서버 사용) Web Server와 WAS를 분리하여 장애 극복에 쉽게 대응할 수 있고 무중단 운영을 가능하게 합니다.

**결론**

- **자원 이용의 효율성 및 장애 극복, 배포 및 유지보수의 편의성 을 위해 Web Server와 WAS를 분리합니다.**
- **Web Server를 WAS 앞에 두고 필요한 WAS들을 Web Server에 플러그인 형태로 설정하면 더욱 효율적인 분산 처리가 가능합니다.**