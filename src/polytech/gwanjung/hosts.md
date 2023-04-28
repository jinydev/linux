---
layout: home
---
## hosts 파일이란?
- 호스트 이름에 대응하는 IP 주소가 저장 되어 있어서 도메인 이름 시스템인 DNS에서 주소 정보를 제공받지 않고도 서버의 위치를 찾게 해주는 파일
쉽게 풀어서 설명하자면
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FviEBv%2FbtqKwrfnPaw%2Fr0rcKUiKff0liHTyKiVqqk%2Fimg.png)

브라우저 화면을 열고 url으로 https://www.naver.com을 입력 했을 때 https://www.naver.com 이란 URL 에 해당하는 IP 주소를 DNS에 요청하고 DNS 에서 제공 받은 IP로 접속 하는 겁니다.
이 때 굳이 DNS 에서 도메인에 해당하는 IP를 찾지 않고도 주소를 찾을 수 있게 해주는 파일이 바로 hosts 입니다.
위 사진은 호스트 파일을 문서 편집기로 열었을 때의 모습입니다.
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fmd7Xk%2FbtqKte2l5wE%2F7UCFAOtjrMekKvDNRY7PQ0%2Fimg.png)
- 호스트 파일을 수정할 때는 IP + 공백 + 호스트이름 을 적어주면 적용되고 127.0.0.1 은 기본적으로 자신의 컴퓨터 서버를 뜻 합니다.
- 이를 응용해서 해커들이 해킹할 때도 아주 많이 응용합니다.
- https://www.naver.com 의 호스트를 해커들이 특정 페이지의 ip로 지정하고 해당페이지에서는 정보를 빼내는 소스를 작성해놓고 기다리는 방식으로 로 말입니다.
- 그러면 https://www.naver.com 으로 접속하려고 할때 해커가 만들어 놓은 페이지에 접속하게 되는 방식입니다.

## 정리

▶ 호스트파일의 역할

 - 호스트 이름에 대응하는 IP 주소가 저장되어 있어서 도메인 이름 시스템(DNS)에서 주소 정보를 제공받지 않고도 서버의 위치(IP)를 찾게 해준다.

▶ 호스트 파일 사용 장점

 - 인터넷 속도 향상

 - 리소스 사용을 줄임

 - 보안 문제 예방적 대처

▶ 호스트 파일 사용 단점

 - 사이트 방문이 차단될 수 있다

 - 페이지 내에서 부분 차단된 경우 디자인, 속도 문제

▶ 호스트 파일 저장 위치

 C:\windows\system32\drivers\etc\hosts

▶ 호스트 파일 작성 원칙

- 샵 기호(#)로 시작하는 줄(line)은 주석문, 개별 줄(line) 앞이나 호스트 이름 다음에 작성

- 각 항목은 한 줄(line)로 작성

- 항목은 IP 주소 + 호스트 이름 순서로 제한

- 호스트 이름과 IP 주소의 간격은 최소한 1칸을 띄움

- 호스트 이름 부분에 'IP 주소' 등록 제한 : 호스트의 IP 주소 검색이 목적. IP 주소를 이미 찾은 상태

- 호스트 이름의 글자수는 255자로 제한

- 프로토콜 형식 'http:', 와일드카드 문자 '*', 주소 맨끝에 사선기호 '/' 사용 제한