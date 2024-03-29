---
layout: home
---

# 가상머신

## **가상머신이란?**

하드웨어를 소프트웨어적으로 구현해서 그 위에서 운영체제가 작동하도록하는 기술

- 가상머신은 하나의 물리적인 컴퓨터에서 여러 개의 가상 컴퓨터를 생성하는 기술
- 하드웨어 자원(프로세서, 메모리, 저장장치 등)을 가상화하여 각 가상 컴퓨터가 독립적인 운영체제(OS)를 실행할 수 있게 하는 것
    
    ⇒ 하드웨어가 진짜 존재하는 것처럼 가상화 
    <br/><br/>

**[가상머신 사용 시의 컴퓨터 구조]**

![가상머신](https://user-images.githubusercontent.com/127702320/233243105-b29bd578-428f-46ed-a0fd-cb5ef0bf4959.png)


- Linux
    - Rocky, Ubuntu, CentOS …

## **가상머신을 사용하는 이유(장점)**

- **다른 운영체제**를 사용해야 하는 경우(맥OS에서 윈도우, 윈도우에서 리눅스)
    - 특정 OS에서만 돌아가는 프로그램 사용 시 ex) ActiveX(과거)
    - 시스템 유연성이 높아짐
    <br/><br/>
- **독립된 작업공간**이 필요한 경우 (바이러스 회피)
    - 바이러스 의심 프로그램을 반드시 실행해야 할 경우 가상환경 안에서 실행하여 바이러스 회피 가능
    <br/><br/>
- **스냅샷(Snapshot)**을 이용하여, 가상 컴퓨터의 상태를 미리 저장해 둘 수 있어서, 문제 발생 시 쉽게 이전 상태로 **복구** 가능 (백업)
    <br/><br/>
- 하나의 머신에서 **여러명**에게 운영체제 환경을 **제공**
    - 자유도가 높아짐, 비용 절감
    <br/><br/>
- 하드웨어 자원의 효율성이 높아지는 장점
    - 물리적인 서버의 CPU나 메모리 등의 자원이 남아있을 때, 해당 자원을 가상 서버에 동적으로 할당하여  물리적인 서버 자원의 효율성을 높이고, 더 많은 가상 서버를 운영할 수 있도록 도와줌
    <br/><br/>
## **가상머신의 단점**

- 성능 저하 : 물리적인 `컴퓨터 자원`을 여러 개의 가상 머신이 공유하기 때문에 발생
    - 하드웨어 자원 한계 : 실제 하드웨어 자원을 가상화하여 사용하므로, 실제 하드웨어 자원 한계를 넘어서는 작업을 수행할 수 없음
    - ex) 대용량 처리나 그래픽 작업 수행 → 성능 저하
    <br/><br/>
- 호환성 문제 : 일부, 가상머신이 지원하는 운영체제 버전이 한정되어 있거나, 가상머신에서 사용하는 가상 그래픽 카드가 실제 하드웨어와 호환이 되지 않을 가능성 존재
    <br/><br/>
- 보안 위협 : 바이러스 회피 효과가 있긴 하지만, 실제 하드웨어처럼 보안 기능을 가지고 있지 않기 때문에, 가상머신 위에서 실행되는 운영체제에 보안 취약점이 있을 경우, 해당 가상머신의 모든 운영체제와 데이터가 위협 받을 수 있음
    <br/><br/>
- 유지보수의 어려움 : 유지보수가 힘들 경우 가상머신 시스템의 안정성과 성능에 영향을 미칠 수 있음
    <br/><br/>
> *성능 저하 문제 → 가상머신뿐만 아니라 호스트 컴퓨터에서 실행되는 `다른 프로세스`와도 공유되므로 성능 저하 문제가 발생할 수 있습니다. 이러한 이유로, 가상머신을 사용할 때는 `호스트` 컴퓨터의 사양과 가상머신의 `자원 할당` 등을 고려하여 성능 저하 문제를 최소화할 필요가 있다.*
> 

![chatgpt](https://user-images.githubusercontent.com/127702320/233243176-747b59bf-a20c-4e4a-87b3-d742c0751a37.png)


## 가상 머신 소프트웨어 종류

- Virtual Box
    - 오라클에서 만든 가상머신 솔루션
    - 오픈소스
    - 무료
    - 커뮤니티 지원 활발  
    <br/><br/>
- VMware
    - 무료 버전인 VMware Player와 유료 버전인 VMware Workstation
    - 보안 기능 : 보안 취약점 검사하고 보호할 수 있는 기능
    - 가상머신 클러스터링 및 고급 네트워크 기능 제공
    <br/><br/>
- Hyper-V, Virtual PC 등등
    - 마이크소프트에서 제공하는 가상화 소프트웨어
    - 윈도우 운영체제에서만 실행
    - Hyper-V는 더욱 큰 규모의 가상화 작업을 위해 설계되었고, Virtual PC는 더욱 개인용으로 사용하기 적합
 <br/><br/>
cf. VMware는 보안 관리 기능을 제공 →  예를 들어, VMware vSphere는 가상화 환경에서 실행되는 서버 가상 머신들의 보안을 관리하기 위한 다양한 보안 기능을 제공한다. 이에는 가상 머신 암호화, 가상 머신 보안 패턴 검색, 가상 머신에서 실행되는 애플리케이션 보안 등이 포함된다. 또한 VMware vSphere는 가상 머신의 보안 상태를 모니터링하고 관리하는 보안 관리 도구를 제공하여 가상 머신의 보안을 강화할 수 있다.