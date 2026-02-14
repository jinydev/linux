---
layout: home
title: 05.기본 명령어
description: 리눅스 기본 명령어
keywords: linux, command, cli
---

## 05.기본 명령어
---
리눅스를 사용하기 위한 기본적인 명령어들에 대해서 알아 보도록 합니다.

### 05-1.프로그램 설치
리눅스에서 프로그램을 설치하는 방법은 여러 가지가 있습니다. 소스 코드를 컴파일하여 설치하는 방법과 패키지 관리자를 사용한 설치방법이 있습니다.

#### 소스 코드를 컴파일하여 설치하는 방법
리눅스에서는 소스 코드를 직접 컴파일하여 프로그램을 설치할 수도 있습니다. 이 방법은 패키지 관리자를 사용하지 않으므로, 최신 버전의 프로그램을 설치하고자 할 때 유용합니다.  
* [컴파일이란](/system/compile)
* [컴파일 설치](/system/compile/install)

#### 패키지 관리자를 사용한 설치방법
리눅스 배포판마다 다른 패키지 관리자를 사용합니다. 대표적인 패키지 관리자로는 `APT`, `YUM`, `DNF`, `Pacman` 등이 있습니다. 각 패키지 관리자는 고유한 명령어를 제공하며, 해당 명령어를 사용하여 프로그램을 설치할 수 있습니다.  

* [패키지 관리란?](/system/package)

데비안 계열  
* [DPKG와 APT](/system/package/apt)  

래드햇 계열  
* [rpm과 yum](/system/package/yum)
* [dnf](/system/package/dnf)


### 05-2.SSH 설치 및 터미널접속
리눅스 터미널 접속이란, 터미널 프로그램을 사용하여 리눅스 서버나 컴퓨터에 원격으로 접속하는 것을 말합니다. 터미널 접속을 통해 리눅스 시스템을 원격으로 관리하고 작업할 수 있으므로, 서버 운영이나 개발 작업 등에서 필수적인 기술입니다.

#### [원격 접속](/system/remote)  
터미널 접속을 통해 CLI(Command Line Interface)를 통해 리눅스 시스템을 제어하고, 명령어를 입력하여 작업을 수행할 수 있습니다. 

* [ssh](/system/remote/ssh)  
일반적으로 SSH(Secure Shell) 프로토콜을 사용하여 원격으로 터미널 접속을 수행합니다. SSH를 사용하면 인터넷을 통해 안전하게 원격 서버에 접속할 수 있습니다. 

* [telnet](/system/remote/telnet)
Telnet이나 FTP를 사용하여 원격 서버에 접속하는 것이 있지만, 보안상의 이유로 사용되지 않습니다. 

  
#### 클라이언트 접속도구
* [putty 설치](/system/remote/putty) 
* [윈도우터미널](/system/remote/winterm)

### 05-3.GUI 접속도구
gui환경의 작업을 원하는 경우에는 vnc를 이용할 수 있습니다.
* [vnc](/system/remote/vnc)
* 윈도우 원격접속

### 05-4.[기본명령어](/command)
* 도움말
* [명령어 히스토리](/command/history)
