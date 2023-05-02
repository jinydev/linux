## 웹서비스란?
---


<img src ="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdQfQaR%2Fbtqyj4cOApX%2FshCFObpKPqOQ6KeMLLXWm0%2Fimg.png">

- 웹 서비스는 네트워크 상에서 상호운용 가능한 기계 간의 통신을 지원하도록 설계된 소프트웨어 시스템
- Machine-Processable 포맷 (WSDL)으로 기술된 인터페이스이다.
- 다른 시스템들은 일반적으로 XML 직렬화로 HTTP를 사용하여 전달되는 SOAP 메시지를 사용하여 웹 서비스와 상호작용한다.
- 월드 와이드 웹(WWW)과는 달리 웹 서비스는 순수 컴퓨터와 컴퓨터간의 상호작용을 위한 시스템이다.
- 2002년에는 3가지 주요 표준(SOAP, WSDL, UDDI) 모두를 사용하는 것을 웹 서비스라고 정의하였으나, 2003년부터 어느 한가지만을 사용해도 웹 서비스를 구현한 것으로 정의하고 있다.

## 웹서비스의 등장 배경

<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbwv598%2FbtqymU7FA1B%2FIvrPGkMK9mALj3Snpex5ck%2Fimg.png">

**기존의 통합 방식**

- 서로 다른 플랫폼 기반 어플리케이션 간 통신 수단이 상이하여 통합이 사실상 어려움
- 통합을 위해 EDI, VAN, Adapter, EAI/B2Bi 등 proprietary한 기술/솔루션을 적용하거나 전면 재개발
- **→ 많은 시간, 투자, 리소스가 요구**

**웹 서비스의 등장**

- 인터넷과 XML 기반 SOAP과 같이 표준화된 통신 수단을 사용하여 서로 다른 플랫폼 기반 어플리케이션간 통신이 가능해짐
- **→ 별도의 솔루션을 도입할 필요 없이 통합이 가능해져 비용과 시간을 절약**

## 웹서비스의 특징

- **시스템 구조의 유연성** : 메인 프레임 또는 서버-클라이언트 방식과 달리 유연한 소프트웨어 구조를 통해 이질적인 데이터 표준을 유연하게 통합/운영
- **사용의 편리성** : 사용자는 소프트웨어를 설치한 후 자연스럽게 서비스를 제공받게 되며, 인터넷을 연결할 수 있는 유/무선 단말기를 통해 장소에 관계없는 접근 가능
- **기존 시스템의 통합 환경을 제공** : 이질적인 어플리케이션간의 통합 서비스를 제공받을 수 있고, 새로운 시스템과의 통합도 자동적으로 이루어진다.
- **비용 효율적** : 분산 시스템의 소프트웨어 간 통합을 자동화적으로 이행해줌으로써 개별 기업마다 투입해야 하는 IT 개발 및 운영 비용을 절감

## 웹서비스의 구성 요소

<img src ="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FeuNTN3%2Fbtqyj268UmA%2FR0EtGXdtvNlkGS2y5nhsKK%2Fimg.png">

웹 서비스의 구성요소로는 크게 **SOAP, WSDL, UDDI** 세가지가 있다.

**WSDL(Web Service Description Language)**

- 웹 서비스를 표현하고 기술하는 언어(서비스 표현 언어)
- 웹 서비스의 공개 인터페이스를 설명하기 위한 XML 문법
- 공개 인터페이스
    - 공개적으로 사용할 수 있는 기능들의 정보
    - XML 메시지를 위한 데이터 타입 정보
    - 사용된 전송 프로토콜에 관한 바인딩 정보
    - 특정한 서비스 위치에 관한 주소 정보
- WSDL은 SML(Service Metadata Locator) 메시지 시스템에 꼭 필요한 것은 아니지만 SOAP 메시지를 기술하기 위한 빌트인 익스텐션(built-in extensions)을 포함하고 있다.

**UDDI(Universal Description, Discover and Integration)**

- 필요한 서비스를 찾을 수 있는 웹 서비스 레지스트리 (서비스 등록, 검색)
- 웹 서비스와 비즈니스를 발행(Publish) / 검색(Find)하기 위한 기술적인 스펙
- UDDI 데이터 범주
    - White 페이지 : 회사에 대한 일반적인 정보 (비즈니스 이름, 세부내용, 주소)
    - Yellow 페이지 : 회사나 서비스가 제공하는 분류된 데이터 (표준 분류법을 토대로 산업, 제품, 지리적 코드 별로 나뉜 데이터)
    - Green 페이지 : 웹 서비스에 대한 기술적인 정보 (외부 스펙을 가리키거나 웹 서비스 호출에 대한 주소)

**SOAP(Simple Object Access Protocol)**

---

- SOAP은 SOA(서비스 지향 아키텍처)와 SOA와 관련된 웹 서비스 규격의 필수적인 부분이다.
- 발신자와 수신자 사이의 메시지 경로를 만들어 주기 때문에 안전을 준수하는 접속, 접속 제어, 신뢰성 있는 전달과 오류 복구, 동적 서비스 발견 등을 지원한다.
- SOAP의 메시지는 XML에서 high-level로 정의되지만, 대부분의 SOAP 어플리케이션은 XML로 작성된 WSDL을 사용한다.
- SOAP의 데이터 구조는 XML을 기반으로 하고 있는데, 이는 웹 페이지를 정의하는데 사용되는 HTML과 여러 면에서 유사하다.
- XML은 대체로 사람이 읽을 수 있어 SOAP 메시지를 쉽게 이해할 수 있게 하지만, 이진 데이터를 수용하는 CORBA 및 RPC 프로토콜에 비해 상대적으로 메시지를 크게 만든다.
- SOAP의 가장 큰 단점은 헤비급 아키텍처를 위한 헤비급 프로토콜이라는 것이다. 메시지가 일련의 노드를 통과하여 각각 처리되어야 한다는 개념은 소프트웨어에 대한 프로토콜과 서비스 버스 아키텍처 모델을 혼합한 것으로 보이며, 그 두 가지 모두 오늘날 일반적으로 사용되는 마이크로 서비스 기반 개발에 최적으로 간주되지 않는다.
