---
layout: home
---

# __리눅스 - 라우터__
## __0425. 라우터와 라우팅__ 
<hr/>   

> 라우팅은 네트워크에서 경로를 선택하는 프로세스   
컴퓨터 네트워크는 노드라고 하는 여러 시스템과 노드를 연결하는 경로 또는 링크로 구성됨   
상호 연결된 네트워크에서 두 노드 간의 통신은 여러 경로를 통해 이루어짐   

## 라우팅은 미리 정해진 규칙을 사용하여 **최상의 경로를 선택**
   
- ### 라우팅이 중요한 이유 - 네트워크 장애를 최소화
    - 라우팅은 네트워크 통신의 **효율성을 높임**
    - 네트워크 통신 장애가 발생하면 웹 사이트 페이지가 로드될 때까지 **사용자가 기다리는 시간이 길어짐**
    - 웹 사이트 서버에서 많은 수의 사용자를 처리하지 못해 **서버의 작동이 중단될 수 있음**
    - 라우팅은 네트워크가 정체 없이 최대한 많은 용량을 사용할 수 있도록 **데이터 트래픽을 관리**<br/><br/>
- ### **라우터**는 컴퓨팅 디바이스와 네트워크를 다른 네트워크에 연결하는 네트워킹 디바이스
    1. **경로 결정**
        - 라우터는 소스에서 대상으로 이동하는 **데이터의 경로를 결정** 지연, 용량 및 속도와 같은 네트워크 지표를 분석하여 최상의 경로를 찾으려고 시도
    2. **데이터 전달**
        - 라우터는 선택한 경로의 다음 디바이스로 데이터를 전달하여 최종적으로 대상에 도달하도록 함
        - 디바이스와 라우터는 동일한 네트워크에 있거나 서로 다른 네트워크에 있을 수 있음
    3. **로드 밸런싱**
        - 경우에 따라 라우터가 여러 경로를 사용하여 데이터 패킷의 여러 사본을 전송할 수 있음<br/><br/>
- ### 라우팅은 어떻게 작동하나? 
    - 데이터 **패킷**의 형태로 **네트워크를 통해 이동**
    - 패킷이 대상으로 이동하는 동안 여러 라우터가 패킷을 **여러 번 라우팅**할 수 있음
    - 라우터는 수백만 개의 패킷에 대해 초당 수백만 번 이 프로세스를 수행함
    - **데이터 패킷이 도착**하면 라우터는 먼저 **라우팅 테이블에서 그 주소를 찾고**, 목적지 까지 가는 데 가장 적합한 버스 노선을 찾기 위해 버스 시간표를 참조하는 승객에 비유할 수 있음
    - 그런 다음 라우터는 패킷을 네트워크의 다음 지점을 전달하거나 이동함<br/><br/>
- ### 정적라우팅 vs 동적라우팅
    - **정적라우팅** : 네트워크 관리자가 정적테이블을 사용하여 네트워크 경로를 **수동으로 구성하고 선택**. **네트워크 설계나 파라미터가 일정하게 유지**될 것으로 예상되는 경우에 유용함
    - **동적라우팅** : 동적라우팅에서 라우터는 **실제 네트워크 조건에 따라 런타임에 라우팅 테이블을 만들고 업데이트**함. 동적 라우팅 테이블을 만들고 유지관리하고 업데이트하는 규칙 집합인 동적 라우팅 프로토콜을 사용하여 소스에서 대상까지 **가장 빠른 경로를 찾음**<br/><br/>

- ### 라우팅 프로트콜 종류
    라우팅 프로토콜은 **내부 게이트웨이** 프로토콜과 **외부 게이트웨이** 프로토콜이라는 2가지 범주로 분류됨   
    내부 게이트웨이 프로토콜은 단일 조직에서 관리자가 제어하는 네트워크인 자율 시스템에서 가장 효과적으로 작동함
    외부 게이트웨이 프로토콜은 두 자율 시스템 간의 정보 전송을 관리하는 데 보다 적합함
    - **내부게이트웨이 프로토콜**   
        이 프로토콜은 자율 시스템을 평가하고 다음과 같은 다양한 지표를 기준으로 라우팅과 관련한 결정을 내림
        - 홉 수 또는 소스와 대상 간의 라우터 수
        - 지연 또는 소스에서 대상으로 데이터를 전송하는 데 걸린 시간
        - 대역폭 또는 소스와 대상 간의 링크 용량<br/><br/>
    - **Routing Information Protocol**   
        Routing Information Protocol(RIP)은 홉 수를 기준으로 네트워크 간의 최단 경로를 결정. RIP는 대규모 네트워크를 구현하는 데 적합하지 않기 때문에 현재는 사용되지 않는 레거시 프로토콜임.<br/><br/>
    - **Open Shortest Path First Protocol**   
        Open Shortest Path First(OSPF) 프로토콜은 자율 시스템의 다른 모든 라우터에서 정보를 수집하여 데이터 패킷의 대상까지 가장 짧고 빠른 경로를 식별. 다양한 라우팅 알고리즘 또는 컴퓨터 프로세스를 사용하여 OSPF를 구현할 수 있음.<br/><br/>
    - **외부 게이트 웨이 프로토콜**   
        Border Gateway Protocol(BGP)은 유일한 외부 게이트웨이 프로토콜.<br/><br/>
    - **Border Gateway Protocol**   
        BGP는 인터넷을 통한 통신을 정의합니다. 인터넷은 서로 모두 연결되어 있는 대규모 자율 시스템의 모음. 모든 자율 시스템에는 Internet Assigned Numbers Authority에 등록하여 할당받는 Autonomous System Number(ASN)가 있음.<br/><br/>