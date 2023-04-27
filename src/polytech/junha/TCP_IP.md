---
layout: home
---

# TCP/IP

**정의**

인터넷에서 데이터를 전송하는데 사용되는 프로토콜 스택

### Protocol

![protocol](https://static.javatpoint.com/tutorial/computer-network/images/tcp-ip-model.png)

- error-free를 위한 미리 정의된 의사 단계
- OSI 7 layers (OSI reference model)
    - physical
    - Data link
    - **Network: - IP (Internet Protocol)**
    - **Transport - TCP(Transmission Control Protocol), UDP(User Datagram Protocol)**
    - Session
    - Presentation
    - Application

즉, TCP/IP는 OSI 7계층의 3, 4 레이어의 TCP와 IP를 합쳐 부르는 말

TCP/IP를 사용하겠다는 것은 
[1] IP 주소 체계를 따르고, 
[2] IP 라우팅을 이용해 목적지에 도달하며,
[3] TCP의 특성을 활용해 송신자와 수신자의 논리적 연결을 생성하고, 
[4] 신뢰성을 유지하겠다는 의미

### Network Layer (3 Layer)

- IP가 활용되는 부분으로, 한 Endpoint(사용자)가 다른 Endpoint(사용자)로 가고자 할 경우, 경로와 목적지를 찾아줌
- 위를 라우팅이라고 하며 대역이 다른 IP들이 목적지를 향해 제대로 찾아갈 수 있도록 돕는 역할

### Transport Layer (4 Layer)

- 송신자와 수신자의 논리적 연결을 담당하는 부분으로, 신뢰성 있는 연결을 유지할 수 있도록 도와줌
- Endpoint 간에 연결을 생성하고 데이터를 얼마나 보내고 받았는지, 제대로 받았는지 등을 확인
- TCP와 UDP가 있다

### TCP

**개요**

TCP는 근거리 통신망이나 인트라넷, 인터넷에 연결된 컴퓨터에서 실행되는 프로그램간에 일련의 옥텟을 안정적으로, 순서대로, 에러 없이 교환할 수 있게 함

IP가 패킷들의 관계를 이해하지 못하고 목적지를 찾아가는 것에 중점을 둔다면, TCP는 통신하고자 하는 양쪽 단말(Endpoint)이 통신할 준비가 되었는지, 데이터가 제대로 전송되었는지, 데이터가 가는 도중 변질되지는 않았는지, 수신자가 얼마나 받았고 빠진 부분은 없는지 등을 점검

IP Header와 TCP Header를 제외한 TCP가 실을 수 있는 데이터 크기를 **세그먼트**라고 부름

**TCP 작동 (3-way handshake)**

1. 송신자가 수신자에게 SYN을 날려 통신이 가능한지 확인. Port가 열려 있어야함
2. 수신자가 송신자로부터 SYN을 받고 SYN/ACK을 송신자에게 날려 통신할 준비가 되었음을 알림
3. 송신자가 수신자의 SYN/ACK를 받고 ACK를 날려 전송 시작을 알림

*SYN, ACK: TCP Header의 요소

**TCP 특징**

- 흐름 제어
    - TCP Header내의 Window Size를 사용해 한번에 받고/보낼 수 있는 데이터의 양을 정함
    - window는 일정량의 데이터를 뜻하고, Window size는 수신자가 정함. 또한 상황에 따라 조절
    - 수신자는 받은 데이터양을 확인하여 송신자에게 보냄 → Acknowledgment Number
    수신자가 N번째의 데이터를 받았으면 Acknowledgment Number에 1을 추가하여 N+1을 보냄
    - 위의 데이터 순서번호를 Sequence Number라고 부름
- 혼잡 제어
    - 데이터가 지나가는 네트워크 망의 혼잡또한 중요하다
    - Slow Start: 송신자는 연결 초기에 데이터 송출량을 낮게 잡고 보내면서 수신자의 수신을 확인하며 데이터 송출량을 조금씩 늘림