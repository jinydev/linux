---
layout: home
---

# CentOS
---
CentOS(Community Enterprise Operating System)는 Red Hat Enterprise Linux(RHEL) 소스 코드를 기반으로 만들어진 무료 오픈소스 리눅스 운영체제입니다. RHEL과 동일한 패키지와 도구를 제공하지만, RHEL과 달리 CentOS는 무료로 제공됩니다.

## RHEL 호환 리눅스 배포판
CentOS는 서버와 엔터프라이즈 환경에서 매우 안정적인 운영체제로 인기가 높습니다. 이는 CentOS의 코드가 RHEL에서 파생되어 있기 때문입니다. 또한 CentOS는 무료 지원 및 보안 업데이트를 제공하기 때문에 기업에서 안정적인 시스템을 구축하고 운영하는 데 많이 사용됩니다.



![파일:Centos-logo-light.svg](./img/658px-Centos-logo-light.svg.png)



CentOS는 다양한 서버 역할에 맞는 패키지를 제공합니다. Apache, MySQL, PHP, PostgreSQL, Samba 등의 서버 소프트웨어를 포함한 다양한 패키지를 지원합니다. 또한, CentOS는 가상화 기술을 지원하고 있으며, KVM, Xen, VirtualBox, VMware 등의 가상화 플랫폼에서 호스팅될 수 있습니다.

CentOS는 여러 가지 릴리스 버전이 있으며, 일반적으로 각 버전은 최소 7년간 지원됩니다. CentOS 8부터는 CentOS Stream과 같은 릴리스 전환 방식이 도입되었으며, CentOS Stream은 RHEL과 더 가까운 개발 버전으로 분류됩니다.

## CentOS 버젼
CentOS의 버전은 보통 7.x 또는 8.x와 같이 표현됩니다. 7.x는 CentOS 7 시리즈를 의미하며, 8.x는 CentOS 8 시리즈를 의미합니다. 

### CentOS 7
CentOS 7은 2014년에 출시된 CentOS의 7.x 시리즈로, RHEL 7의 소스 코드를 기반으로 만들어졌습니다.

CentOS 7은 10년간의 장기 지원(LTS)을 제공합니다. 이는 2024년까지 보안 패치 및 업데이트를 지속적으로 제공할 것을 의미합니다.

CentOS 7은 다양한 새로운 기능을 제공하며, Systemd를 도입함으로써 부팅과 관련된 작업을 향상시켰습니다. 또한, XFS 파일 시스템을 기본으로 제공하여 대용량 파일 처리 및 스토리지 관리에 용이합니다.

CentOS 7은 또한 Docker, Kubernetes, OpenStack 등과 같은 최신 기술들을 지원하고 있어, 클라우드 기반 인프라 및 컨테이너 기술과의 연동성이 뛰어납니다.

마지막으로, CentOS 7은 사용자 친화적인 GNOME 3 데스크탑 환경과 함께 서버용으로 설계된 Minimal 설치 옵션을 제공합니다.

### CentOS 8
CentOS 8은 2019년에 출시된 CentOS의 8.x 시리즈로, RHEL 8의 소스 코드를 기반으로 만들어졌습니다.

CentOS 8은 CentOS 7보다 더 많은 새로운 기능과 업데이트가 제공됩니다. 특히, CentOS 8에서는 모듈 기능이 추가되어 필요한 패키지만 설치하고 업그레이드할 수 있습니다. 또한, AppStream 리포지토리를 통해 다양한 언어와 스택을 사용할 수 있습니다.

CentOS 8은 RHEL 8에서 도입된 Systemd의 업그레이드된 버전을 사용하여, 서비스 관리 및 부팅 시스템의 성능을 개선했습니다. 또한, XFS 파일 시스템을 기본으로 사용하며, Btrfs 및 Stratis와 같은 새로운 파일 시스템도 지원합니다.

CentOS 8은 또한 새로운 컨테이너 관리 시스템인 Podman을 도입하여, 컨테이너 이미지 및 컨테이너 실행 환경을 관리할 수 있습니다. 또한, SELinux 정책과 같은 보안 기능도 개선되었습니다.

마지막으로, CentOS 8은 사용자 친화적인 GNOME 3 데스크탑 환경과 함께 서버용으로 설계된 Minimal 설치 옵션을 제공합니다.



## 개발중단
CentOS 개발 중단은 2020년 12월에 Red Hat이 CentOS의 장기 지원 버전(LTS)을 2021년 말에 종료하고 대안으로 CentOS Stream을 제공한다는 발표로 시작되었습니다. 이는 Red Hat이 RHEL을 무료로 사용할 수 있는 CentOS를 더 이상 지원하지 않기로 결정하였기 때문입니다.

이에 따라 CentOS의 사용자들은 CentOS Stream으로의 전환이나 대안 운영체제로의 이전을 고민하게 되었습니다. 그 중 하나가 Rocky Linux입니다. Rocky Linux는 CentOS 개발자 중 한 명인 Gregory Kurtzer가 CentOS LTS 종료 발표 후 만든 CentOS 대안 운영체제입니다. Rocky Linux는 RHEL 코드를 기반으로 만들어졌으며, CentOS처럼 무료 및 개발자 중심의 커뮤니티 운영 방식을 채택하고 있습니다.

Rocky Linux는 CentOS와 유사한 패키지 및 라이브러리를 제공하며, RHEL과의 호환성을 유지하고 있습니다. CentOS와 동일하게 장기 지원(LTS) 계획을 가지고 있으며, CentOS LTS가 종료될 예정인 2021년 말부터 LTS 버전을 제공할 예정입니다.

따라서 CentOS를 사용하고 있던 사용자들은 Rocky Linux로 전환하여 CentOS와 유사한 환경에서 작업을 계속할 수 있습니다.



## CentOS 설치





## 설치후 확인

