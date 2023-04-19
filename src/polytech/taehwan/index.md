---
layout: home
---

# Taehwan Report
- [ 20230417 - Day1-리눅스-배포판-소개](./2023-04-17-Day1-리눅스-배포판-소개.md)<br>
- [ 20230418 - Day2-Linux-OS의-구성요소-중-Shell](./2023-04-18-Day2-Linux-OS의-구성요소-중-Shell.md)<br>
- [ 20230419 - Day3-리눅스-사용자(User)와-그룹(Group)](./2023-04-19-Day3-리눅스-사용자(User)와-그룹(Group).md)<br>


# 리눅스 배포판 소개

[https://commons.wikimedia.org/wiki/File:Linux_Distribution_Timeline.svg](https://commons.wikimedia.org/wiki/File:Linux_Distribution_Timeline.svg)

## 데비안(Debian)

- 데비안 GNU/Linux
- 파생된 배포판: 우분투(ubuntu), 리눅스 민트(Linux Mint) 등

- 주요 특징
    - 패키지 설치 및 업그레이드의 단순함: 패키지 매니저 apt 등을 이용
        - (node.js의 npm이나 python의 pip나 homebrew의 brew와 같은 것)
    - 설치파일 확장자 .deb
    - 북한 붉은별os (linux 배포판)
    

### 우분투 리눅스(Ubuntu Linux)

- “Ubuntu”는 “우리가 함께 있기에 내가 있다.”라는 고대 아프리카 단어
- 2004년 10월, 4.10버전 첫 출시
- 파생된 배포판: 리눅스 민트(Linux Mint) 등
- 주요 특징: GNOME을 기본 데스크탑 환경으로 사용

### 리눅스 민트(Linux Mint)

- 요즘 제일 많이 쓰고 있는 리눅스 배포판
- 우분투 리눅스 기반으로 → GUI의 외향적 이미지 더 집중

## 레드햇(RedHat)

- 1995년, Bob Young이 창립한 리눅스 배포판 회사

- 패키지 매니저 RPM이용
- 설치파일 확장자 .rpm

### 레드햇 계열 배포판

- RebHat Enterprise Linux (RHEL) : 기업용 배포판
- CentOS(The Community ENTprise Operating System) : RHEL의 오픈소스 버젼
- Fedora : RHEL을 더 좋게 관리하려고, 커뮤니티에 무료로 공개해서 버그나 피드백을 받는 페도라 프로젝트

- 파생 배포판
    - 오라클 리눅스
    - Rocky Linux

## 슬랙웨어(slackware)

- 1994년에는 리눅스를 이용하려면 → os의의 구성요소들인 커널, 쉘, 애플리케이션, 인스톨러(설치과정에 해당하는) 등을 각각 다운 받아야 했는데
- 슬랙웨어가 이런 것들을 모두 CD-ROM 하나에 넣어서 배포했다 → 이것이 첫 리눅스 배포판
- 파생 배포판
    - 수세 리눅스(SUSE Linux)

## 젠투 리눅스(Gentoo Linux)

- 개발자, 네트워크 전문가를 위한 배포판
- 파생 배포판
    - 구글, 크롬OS
        - ex) 크롬 OS를 탑재한 ChromeBook
    - 크로미움 OS (Chromium OS)
        - 구글 크롬 OS의 오픈 소스 개발 버전
        - 오래된 노트북 있으면 한번 써보시길, 유튜브 머신, 넷플릭스 머신으로 쓸만함