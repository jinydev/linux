---
layout:home
---

# 패키지 관리
시스템에 소프트웨어 를 치하고 유지 및 관리하는 방법

### 패키지 사용 이전과 이후
소스코드 다운받아 컴파일해야 소프트웨어 사용가능했지만 지금은 배포업체로부터 패키지를 설치하면 사용가능하다.

## 패키지 시스템

* 주요 패키지 시스템 분류 (일반적으로 호환X)
  
|패키지 시스템| 배포판(일부만 나열) |
|---|---|
|데비안 스타일(.deb)|Debian, Ubuntu, Xandros, L1nsp1re|
|레드햇 스타일(.rpm)|Fedora, CentOS, Red Hat Enterprise Linux, openSUSE, Mandriva, PCLinuxOS |

## 패키지 시스템 동작 원리
### 패키지 파일
- 소프트웨어 키지를 구성하고 있는 파일들의 압축된 형태
- 설치될파일 + 패키지의 메타데이터

### 저장소
테스트용 저장소 : 일반적인 배포 형태로 릴리즈하기 전, 사용자들이 미리 버그를 찾고자 사용할 수 있음.
개발용 저장소 : 주요 배포판에 포함될 작업 중인 패키지들 저장

### 의존성
- 패키지가 공유 라이브러리와 같은 공유 자원을 필요로 한다.
- 의존성 문제를 해결하기 위해 해당 패키지와 관련된 모든 의존성들까지 설치되도록함.

### 고수준과 저수준 패키지 툴
저수준 툴 : 패키지 파일 설치 및 삭제하는 작업을 관리
고수준 툴 : 메타데이터 검색 및 의존성 문제 해결

* 패키지 시스템 도구
  
|배포판|저수준 도구|고수준 도구|
|---|---|---|
|데비안형식|dpkg|apt-get, aptitude|
|페도라. 레드햇 엔터프라이즈 리눅스. 센트OS|rpm|yum|


## 일반적인 패키지 관리 작업

### 저장소에서 패키지 찾기
* 패키지 검색 명령어
  
|형식| 배포판|
|---|---|
|데비안|apt-get update; apt-cache 'search_string'|
|레드햇|yum search 'search_string'|


### 저장소에 있는 패키지 설치하기
* 패키지 설치 명령어
  
|형식| 배포판|
|---|---|
|데비안|apt-get update; apt-get install 'package_name'|
|레드햇|yum-get install 'package_name'|


### 패키지 파일에서 패키지 설치하기
* 저수준 패키지 설치 명령어
  
|형식| 배포판|
|---|---|
|데비안|dpkg --install 'package_file'|
|레드햇|rpm -i 'package_file''|


### 패키지 삭제하기
* 패키지 삭제 명령어
  
|형식| 배포판|
|---|---|
|데비안|apt-get remove 'package_name'|
|레드햇|yum erase 'package_name'|



### 저장소로부터 패키지 업데이트하기
* 패키지 업데이트 명령어
  
|형식| 배포판|
|---|---|
|데비안|apt-get update; apt-get upgreade|
|레드햇|yum update|


### 패키지 파일에서 패키지 업데이트하기
* 저수준 패키지 업그레이드 명령어
  
|형식| 배포판|
|---|---|
|데비안|dpkg --install 'package_file'|
|레드햇|rpm -U 'package_file'|


### 설치된 패키지 확인하기
* 패키지 목록 명령어
  
|형식| 배포판|
|---|---|
|데비안|dpkg --list|
|레드햇|rpm -qa|


### 패키지 설치여부 알아보기
* 패키지 설치확인 명령어
  
|형식| 배포판|
|---|---|
|데비안|dpkg --status 'package_name'|
|레드햇|rpm -q 'package_name'|


### 설치된 패키지 정보 표시하기
* 패키지 정보확인 명령어
  
|형식| 배포판|
|---|---|
|데비안|apt-cache show 'package_name'|
|레드햇|yum info 'package_name'|


### 특정 파일과 관련된 패키지 검색하기
* 패키지 파일(출처) 확인 명령어
  
|형식| 배포판|
|---|---|
|데비안|dpkg --search 'file_name'|
|레드햇|rpm -qf 'file_name'|