---
layout : home
---

HTTPS
======================

# HTTPS

### **HTTP(HyperText Transfer Protocol)**

HTTP는 인터넷에서 웹 서버와 사용자 컴퓨터에 설치된 웹 브라우저 사이에 문서를 전송하기 위한 통신 규약(Protocol)이다. 즉, 인터넷에서 하이퍼텍스트(HyperText)를 전송(Transfer) 하기 위해 사용되는 통신 규약(Protocol)인 것이다.

HTTP 서버는 기본 포트인 80번 포트에서 서비스 대기 중이며, 클라이언트(웹 브라우저)가 TCP 80 포트를 사용해 연결하면 서버는 요청에 응답하면서 자료(정보)를 전송한다. HTTP는 정보를 '텍스트'로 주고받는다. 단순 텍스트를 주고받기 때문에 네트워크에서 전송 신호를 인터셉트하는 경우 원하지 않는 데이터 유출이 발생할 위험이 있다.

이러한 위험을 방지하기 위해 고안된 것이 바로 HTTPS이다.

### **HTTPS(HyperText Transfer Protocol over Secure Socket Layer)**

HTTPS(HyperText Transfer Protocal Secure Socket) HTTPS는 HTTP에 S(Secure Socket)을 추가한 것이다. 기본 골격이나 사용 목적 등은 기존의 HTTP의 그것과 거의 동일하지만, 데이터를 송수신하는 과정에 '보안'요소가 추가된 것이 가장 큰 차이점이라 할 수 있다. 쉽게 말해 HTTPS를 사용하면 서버와 클라이언트 사이의 모든 통신 내용이 암호화된다는 것.

![https://blog.kakaocdn.net/dn/bm260z/btrSE9ZmfTh/H6KelVAdWnYqM0W8ORKMh0/img.png](https://blog.kakaocdn.net/dn/bm260z/btrSE9ZmfTh/H6KelVAdWnYqM0W8ORKMh0/img.png)

SSL(Secure Sockets Layer) 인증서는 클라이언트가 서버로 보내는 정보를 암호화한다. 이렇게 전송된 데이터는 중간에 탈취된다 할지라도 암호화되어 있기 때문에 해독이 불가하다.

### **HTTPS 사용 목적(HTTPS 사용 시 장점)**

HTTPS을 사용하는 이유는 크게 아래 두가지로 설명 가능하다.

첫 번째는 **보안 목적**이다. 클라이언트와 서버 간의 데이터를 주고받는 과정에서 패스워드와 같은 개인정보를 비롯한 민감한 정보들을 악의적인 목적으로 탈취할 수 있는 위험에서 벗어나기 위함이다. 단순 정보 공유 차원의 정적 웹(Static Web Page)이 아닌 결제 시스템이 도입되어 있는 쇼핑몰과 같은 사용자와 서버 간 정보를 주고받아야 하는 경우 HTTPS를 적용하여 보안을 강화할 필요가 있다.

![https://blog.kakaocdn.net/dn/8uPS3/btrSHvmBKEE/KrQQvTSZJKknNOYG6GyWak/img.jpg](https://blog.kakaocdn.net/dn/8uPS3/btrSHvmBKEE/KrQQvTSZJKknNOYG6GyWak/img.jpg)

두 번째는 **마케팅적 측면에서의 장점** 때문이다. 단순 정보 공유 차원의 정적 웹일지라도 HTTPS 사용을 추천하는 이유가 바로 '검색 시 우선순위'때문이다. 네이버, 다음은 물론 구글 역시 검색 엔진 최적화 관련 내용을 웹 상에 적용시키고 있다. SEO(Search Engine Optimization) 즉, 검색 엔진 최적화를 위해서도 HTTP 대신 HTTPS 보안 접속을 적용해야 한다. 동일한 키워드의 페이지가 있다고 가정할 때, 사용자가 키워드 검색 시 상위 노출되는 기준 중 하나가 바로 이 보안 요소이며, HTTP 사이트보다 HTTPS 사이트가 우선 노출될 수 있다는 것이다.