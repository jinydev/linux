---
layout: home
---

# 리눅스 패키지 관리

## 패키지
- 리눅스 패키지는 리눅스에서 소프트웨어를 설치, 업그레이드, 삭제하기 위한 소프트웨어 패키지 파일을 의미
- 패키지 종류는 데비안 계열의 `apt` 레드햇 계열의 `yum & dnf` 등이 있다.

## 패키지 관리
|계열|파일 형식|관리 도구|
|---|---|---|
|데비안|.deb|apt, apt-cache, apt-get, dpkg|
|우분투|.deb|apt, apt-cache, apt-get, dpkg|
|CentOS|.rpm|yum|
|페도라|.rpm|dnf|
- 우분투를 포함한 데비안 계열의 경우 기본 상위 수준의 패키지 관리자로 apt를 사용한다.
- 특정 파일을 처리하는 단위는 dpkg로 파일형식은 .deb이다
- yum은 레드햇 계열의 보안성을 지향하는 패키지 관리툴이다. 파일형식은 .rpm이다.
- CentOS는 레드햇의 무료버전이지만 페도라에서 두 시스템에 대한 연구개발을 진행하여, CentOS 8에서 dnf가 기본 패키지 관리로 변경되었다.
- dnf는 yum보다 빠르게 실행되고 메모리 사용량이 적으며 .rpm파일을 일관되게 처리한다고 한다. (python으로 작성됨)

## local repository
- apt/yum/dnf등은 local repository를 두고 remote에서 관련 패키지를 가져와 설치한다.
- 따라서 local repository에 추가적으로 remote주소를 추가/삭제할 수 있는데 해당 패키지를 정식으로 올려둔 곳을 사용하는게 좋다.
#### 이 부분에 있어 apt와 yum의 차이점이 있는데,
- 좋은 예로 apt의 update와 upgrade를 들 수 있다. update는 단순히 패키지 업데이트가 존재하는지 저장소 업데이트만 진행하는 과정이고 apt upgrade는 실제로 패키지를 최신 패키지로 변경하는 작업이다.
- yum의 update와 upgrade는 모두 패키지의 실제 업데이트 작업이 수행된다. yum의 update와 upgrade의 차이는 '패키지가 업데이트 되면서 더이상 사용되지 않는 파일이나 패키지를 삭제'하겠느냐의 여부를 기본으로 할 것인지 옵션으로 할 것인지가 주된 차이이다. (upgrade = default값으로 삭제)