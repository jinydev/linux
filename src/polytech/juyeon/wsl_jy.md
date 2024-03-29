---
layout : home
---

# JuYeon Report

# WSL(Windows Subsystem for Linux)

![wsl 이미지](https://xeppetto.github.io/images/WSLnDocker/20210312-what-is-WSL/wsl_zp_logo.jpg)

## **WSL이란?**

### Windows Subsystem for Linux

윈도우 운영체제에서 리눅스 환경을 에뮬레이션 하여 사용할 수 있도록 만든 기술로 

쉽게 말해, `마이크로소프트가 윈도우 운영체제에서 리눅스를 사용할 수 있도록 만든 기능`입니다.
<br/><br/>

## **WSL의 탄생 배경**

WSL 개발 이전에는 윈도우에서 리눅스를 사용하려면 Virtual Machine과 같은 도구(Virtual Box, VMware 등)을 이용하여 가상 환경을 구성하거나 듀얼 부팅 설정을 해야 했습니다. 

이 과정에서 CPU, Memory의 문제나 복잡한 네트워크 설정의 문제 등으로 성능과 용량적 측면에서 불편한 점이 많았기에 이러한 문제를 해결하기 위해 WSL이 등장하게 되었습니다.
<br/><br/>

## **WSL의 기능**
![WSL우분투](https://blog.desdelinux.net/wp-content/uploads/2019/06/Windows10_kernelLinux.jpg)

VM과 같은 느린 환경이 아니라 윈도우에서 리눅스 환경처럼 Powershell을 Bash 처럼 사용하고, Linux 명령어(sed, awk, vim, apt 등)를 사용할 수 있으며 Linux 커널조차 이용할
<br/><br/>

## **WSL의 장점**

<aside>
🔶 WSL vs 가상머신

1. 성능
WSL은 가상머신을 사용하지 않기 때문에 가볍고 빠릅니다. WSL1은 윈도우와 리눅스 간의 파일 시스템을 호환하여 사용하기 때문에 가상머신보다 빠릅니다. WSL2는 가상머신을 사용하지만 Hyper-V 기술을 사용하여 가상머신의 오버헤드를 최소화하고, 개선이 지속적으로 이루어지고 있습니다.
2. 편의성
WSL을 사용하면 윈도우와 리눅스 간의 파일 공유, 환경 설정 등이 더욱 편리해집니다. 가상머신을 사용하면 윈도우와 리눅스 간의 파일 공유를 위해 별도의 네트워크 설정이 필요하거나 파일 공유를 위한 별도의 드라이버를 설치해야 할 수도 있습니다. 하지만 WSL에서는 윈도우 파일 시스템을 직접 접근하여 파일 공유가 가능하고, 환경 설정도 간단합니다.
3. 개발 도구 및 서비스
WSL에서는 다양한 리눅스 배포판과 개발 도구, 서비스를 사용할 수 있습니다. 예를 들어, Python, Ruby, Node.js, Apache 등의 프로그래밍 언어와 도구를 사용할 수 있습니다. 또한, Docker를 WSL에서 사용할 수 있기 때문에 개발 및 배포 과정에서 매우 편리합니다.
4. 운영체제 간의 호환성
WSL을 사용하면 윈도우와 리눅스 간의 운영체제 간 호환성이 더욱 높아집니다. 예를 들어, 윈도우에서는 Bash 쉘을 사용할 수 없었지만 WSL을 통해 Bash 쉘을 사용할 수 있게 되어 유닉스 기반의 스크립트를 실행하거나, 리눅스용 프로그램을 윈도우에서 실행할 수 있게 되었습니다.
</aside>
<br/><br/>

## **WSL 버전**

![Untitled](https://user-images.githubusercontent.com/127701871/232748273-c6daa0b0-344d-4c84-8262-2110388b8b39.png)

<br/>
WSL에는 버전 1과 버전 2가 있는데 이들 버전 간의 가장 큰 차이점은 가상화 방식이라는 점입니다.

1. WSL 1

WSL 1은 처음 도입된 WSL 버전으로, Linux 커널을 가상화하지 않고 Windows 시스템 위에서 동작하는 `호환 레이어`를 통해 Linux 바이너리를 실행합니다. 이 방식으로 인해 WSL 1은 파일 시스템 성능이 떨어지는 등 일부 제한 사항이 있지만, Windows와 Linux 간의 상호 운용성을 제공하며 `빠른 시작 속도`를 보입니다.

1. WSL 2

WSL 2는 Windows 시스템 위에서 `Linux 커널을 가상화`하는 방식으로 동작합니다. 이를 위해 `Hyper-V`가상화 기술을 사용하여 Linux 커널을 가상화하고, Linux 파일 시스템을 Windows 파일 시스템에 연결합니다. 이 방식으로 인해 WSL 2는 높은 성능과 파일 시스템 성능 향상, 더 나은 도구 지원 등을 제공합니다. 하지만 가상화에 필요한 자원을 더 많이 사용하기 때문에 시작 속도가 느리며, Hyper-V가 활성화되어 있어야 합니다.

`즉!  WSL 1은 호환성과 빠른 시작 속도를 중시하는 반면, WSL 2는 높은 성능과 파일 시스템 향상을 중시합니다. 따라서 사용자의 요구에 따라 적절한 버전을 선택하여 사용할 수 있습니다.`