# 클라우드 컴퓨팅 관련 기술

# **1. 가상화 기술**

- **하드웨어 리소스 논리적으로 다룰 수 있게 만드는 메커니즘**
- 하나의 물리 서버 -> 여러 개 서버 환경 구축
- 여러 대 물리적 서버 -> 하나의 서버 환경으로 통합
- 종류 ) **서버 가상화, 네트워크 가상화, 스토리지 가상화**

## **서버 가상화 기술**

**서버 리소스 최대한 활용 가능**, 공간 절약, 비용 절감

**종류) 하이퍼바이저 형, 호스트 OS형, 컨테이너 형**

![https://blog.kakaocdn.net/dn/eb11R0/btrLhQeKYvW/fFB3OnmC7oI79uUKea9Zu0/img.png](https://blog.kakaocdn.net/dn/eb11R0/btrLhQeKYvW/fFB3OnmC7oI79uUKea9Zu0/img.png)

#### **하이퍼바이저 형**

**물리 서버 HW -> 하이퍼바이저 가상화 소프트웨어 -> Guest OS**

종류) VMware vSphere, Hyper-V, Xen, KVN

#### **컨테이너 형**

![https://blog.kakaocdn.net/dn/dBeabB/btrLiBgYTeI/eQ6E0x0hrzViqUZNNATcm0/img.png](https://blog.kakaocdn.net/dn/dBeabB/btrLiBgYTeI/eQ6E0x0hrzViqUZNNATcm0/img.png)

- **하나의 OS환경에서 application을 실행하기 위한 영역을 여러 개로 나누어 사용**
- 컨테이너는 하나의 process
- application 실행 환경을 가상화한 것
- **다른 클라우드로 옮기기 쉬움**
- **성능저하 거의 없음, 빠르게 시작 정지 가능**
- guest OS 필요 없음 -> 디스크 사용량 절약
- **대표적인 컨테이너 플랫폼 : Docker**

## **네트워크 가상화 기술**

![https://blog.kakaocdn.net/dn/c6d1U6/btrLhYp9Uvm/VtrBLp40gVWBgMf219p0z0/img.png](https://blog.kakaocdn.net/dn/c6d1U6/btrLhYp9Uvm/VtrBLp40gVWBgMf219p0z0/img.png)

네트워크 물리적 구성 얽매이지 않게 하는 유연성 필요

**VLAN (virtual LAN)**

- **물리적 네트워크 -> 여러 개의 논리적 네트워크**
- 논리적으로 분할된 네트워크는 라우터를 거쳐야 통신 가능 -> 조직단위로 네트워크 나누어 조직 안에 한정된 데이터를 전송
- **클라우드와 데이터 센터 사이에 VLAN 이용 -> private 환경 구축**

**VPN(virtual private network)**

- 불특정 다수가 이용하는 네트워크에 가상으로 전용선과 같은 사설망 연결하는 기술

# **2. 분산처리 기술**

대량의 빅데이터를 여러 서버에 **분산하여 동시에 병렬로 빠르고 효율적 처리하는 기술**

클러스터링 : 여러 서버를 결합하여 **하나의 컴퓨터로 보이게 함**

### **분산처리 구현 소프트웨어**

- **Apache Hadoop**
    - 1대의 master server와 여러 대의 slave server
    - 대용량 데이터 일괄처리
- **Apache Spark**
    - 메모리 안에서 대량 데이터 병렬 분산 처리

# **3. 데이터베이스 기술**

**NoSQL(Not only SQL)**

- **대량의 데이터 분산시켜 고속으로 처리하는 분산 데이터베이스**
- key-value 형, column 지향형, document 지향형, graph 지향형

# **4. 스토리지 기술**

### **Block storage**

블록단위 logical volume을 block 단위로 액세스, 빠른 전송 가능

- **AWS의 EBS 서비스**

### **File storage**

파일 단위로 저장, 파일 공유 기능

- NFS(network file system), NAS(network attached storage)

파일서버

### **Object storage**

**데이터를 객체 단위로 처리**

**HTTP 프로토콜 기반의 REST(Representational State Transfer) 형식의 API 사용**

갱신 빈도가 적은 데이터, 대량의 데이터 저장, 장기 보존

# **5. API (Application Program Interface)**

프로그램이 가진 기능이나 리소스를 외부에 다른 프로그램이 호출하여 이용하기 위한 명령이나 함수, 데이터 형식 등을 정한 규약

API를 통해 외부 프로그램으로 클라우드 서비스를 조작한다. (CLI, SDK, API gateway 이용)

# **6. 클라우드 네이티브 아키텍처**

클라우드 컴퓨팅 사업자가 제공하는 리소스를 활용하여 서비스를 구축하는 방법론

![https://blog.kakaocdn.net/dn/b5yO3s/btrLiac0HxJ/yOdaBbV9w9xUE2aQ6bgyf1/img.png](https://blog.kakaocdn.net/dn/b5yO3s/btrLiac0HxJ/yOdaBbV9w9xUE2aQ6bgyf1/img.png)

### **마이크로 서비스 아키텍처**

- 하나의 application을 작은 서비스의 집합체로 구현
- 각각의 service = API와 같은 간단한 방법으로 연계
- 컴포넌트별 개발 -> 개발의 신속성
- 컴포넌트의 추가와 교체 -> 필요시 빠르게 대응

**여러 함수로 프로그램 구성 -> 각 함수 : 마이크로 서비스**

**API를 통해 각각의 함수 (마이크로 서비스)가 연결이 된다.**

### **서버리스 아키텍처**

- Fully managed cloud service (완전히 관리되는 서비스) -> **HW 종속 X, 운영체제 고려 X**
- 사용자는 서버 존재를 의식하지 않고 응용프로그램 실행
- 클라우드 서비스의 각 컴포넌트와 연계, 개별 기능을 조합하여 서비스를 개발

**여러함수의 프로그램 구성 X,**

**각 사용자의 요청에 따른 해당 함수 실행 -> 사용자는 이 함수가 어떤 서버에서 실행되는지 알 필요가 없다.**

**(서버리스, 완전히 관리되는 서비스)**

# **7. 개발과 운영의 통합 (DevOps)**

![https://blog.kakaocdn.net/dn/bKzPRf/btrLhtYpNWV/kMkd8A7Y0HxQeEPY3KrUo1/img.png](https://blog.kakaocdn.net/dn/bKzPRf/btrLhtYpNWV/kMkd8A7Y0HxQeEPY3KrUo1/img.png)

**Development및 Operation이 함께 협력 -> 완성도 높은 소프트웨어 신속하게 개발**

결정된 부분을 먼저 개발 -> 배포하는 스피드 중시형 **(개발을 하면서 운영을 같이함.)**

**개발 입장**

- **IaaS 클라우드 환경의 보급**으로 애플리케이션 개발 **운영환경을 지원하는 PaaS 서비스가 완비**된다.
- 기업의 서비스 제공 범위가 전 세계로 넓어지고 있다.

**운영 입장**

- **운영 담당자가 서버 설정**
- **자동화: 많은 수의 서버를 소규모 인원으로 운영 -> 운영부서에서 개발부서로 리소스가 이전되는 움직임**

---
## 참고 문헌
[Amazon AWS 백서 및 기술 안내서](
https://aws.amazon.com/ko/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=*all&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=*all&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all)