# 클라우드 컴퓨팅

# **4. 클라우드 컴퓨팅 서비스 모델**

![https://blog.kakaocdn.net/dn/YGTIl/btrLiB82LAe/7Hn6lzq6oXdPKJnLeREJV1/img.png](https://blog.kakaocdn.net/dn/YGTIl/btrLiB82LAe/7Hn6lzq6oXdPKJnLeREJV1/img.png)

### **4.1 IaaS(Infrastructure as a Service)**

- 사업자는 사용자에게 pay-as-you-go access 제공 **`(사용자는 지불한 만큼 HW 리소스 사용)`**
- **사용자가 직접적인 IT 리소스 제어 능력 향상**

### **4.2 PaaS(Platform as a Service)**

- 사업자는 cloud-based environment + infrastructure 제공 **`(개발환경을 제공)`**
- **사용자는 PaaS에서 제공한 개발환경 이용하여 application 개발**
- 애플리케이션 실행 환경이나 데이터베이스 등 미리 준비되어 있음

### **4.3 SaaS(Software as a Service)**

- 사업자는 software / application 제공
- 사용자는 구독하고 web 또는 API 이용하여 access

# **5. 클라우드 컴퓨팅의 장-단점**

### **5.1 장점**

- **`경제성 (쓴 만큼 지불 -> 자본비용을 가변 비용으로 대체)`**
- **`유연성 : 리소스 필요시 필요한 만큼만 확장, 축소`**
- **가용성** : 장애 발생해도 계속 사용 가능 -> 여러 컴퓨터에 가상화, 이중화/ 사용자는 클라우드 서버의 장애 알지 못함
- 빠른 구축 속도
- 손쉬운 글로벌 서비스
- 강력한 **보안**

### **AWS academy**

- 예측을 근거로 한 데이터 센터 투자, 사용한 양에 대해서 지불
- 거대 규모의 경제 실현 -> 비용 절감
- 용량 추정 불필요 -> 필요할 때 리소스 추가 및 축소 가능 (온디맨드 조정)
- 속도 및 민첩성 향상 (빠른 구축)
- 데이터센터 관리 비용 투자 불필요
- 몇 분 만에 전 세계에 배포

### **5.2 단점**

- 생각보다 비싼 비용 청구
- 클라우드의 의존성
- 데이터 보관의 불안함

# **6. 클라우드 컴퓨팅 이용 모델**

![https://blog.kakaocdn.net/dn/no13B/btrLhPNHebA/YLCnnEP5NRN61BFo3qAgBk/img.png](https://blog.kakaocdn.net/dn/no13B/btrLhPNHebA/YLCnnEP5NRN61BFo3qAgBk/img.png)

### **On-premise**

- 회사 내에 자체적으로 데이터 센터 보유
- 시스템 구축, 운용까지 직접 수행

### **deployment model**

- **`private cloud`**
    - **독점적으로 사용되는 클라우드, 자사 전용 환경**
    - **on-premise private cloud (자사 전용 클라우드 환경 구축 운용)**
    - **hosted private cloud (공급자 회사가 해당 회사에 독점적으로 데이터 센터 제공)**
- **`community cloud`**
    - **기업/조직들이 클라우드 시스템을 데이터센터에서 공동 운영**
- **`public cloud`**
    - **클라우드 사업자가 시스템 구축 (ex: AWS)**
- **`hybrid cloud`**
    - **private, public, community 서비스들과 on-primise 시스템을 연계시켜 활용**