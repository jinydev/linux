---
layout : home
---
# Choi Kyeong Min Report 

# **터미널(Terminal)과 쉘(Shell)**

![https://velog.velcdn.com/images/cataiden/post/31a8dfdc-fd26-41f5-b106-cfd2969ba98b/linux_shell.png](https://velog.velcdn.com/images/cataiden/post/31a8dfdc-fd26-41f5-b106-cfd2969ba98b/linux_shell.png)

## 터미널(terminal) ?

> 터미널(terminal)은 사용자와 컴퓨터의 인터페이스이다.
> 
- 터미널은 입출력이 가능한 하드웨어로서, console 이라고도 부릅니다. 명령어를 입력받고 출력하는 곳이자 명령을 입력하는 쉘을 실행하기 위한 껍데기라고 생각하면 편합니다.
    
    ![https://velog.velcdn.com/images%2Fcataiden%2Fpost%2F616d69d9-69cc-43d5-8e6d-1e86f39b8174%2Fterminal2.png](https://velog.velcdn.com/images%2Fcataiden%2Fpost%2F616d69d9-69cc-43d5-8e6d-1e86f39b8174%2Fterminal2.png)
    
- 이는 윈도우, MacOS, Linux 다양한 운영체제에서 쉽게 찾아볼 수 있는데, 우리가 이렇게 접할 수 있는 터미널은 물리적인 하드웨어를 소프트웨어로 구현한 것입니다. 따라서, '터미널 에뮬레이터(Terminal Emulator)'라는 표현이 더 정확할 듯 합니다.
- 우리는 이러한 터미널 에뮬레이터를 통해 그래픽 인터페이스없이 키보드만으로도 컴퓨터에게 다양한 명령을 내림으로써 연산 기능을 수행할 수 있습니다.

## 쉘(shell) ?

> 쉘은 운영체제 상에서 다양한 운영체제 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램이다.
> 
- 쉘은 Command Line Interface(CLI) 로 구현된 프로그램입니다. 주로 사용자가 입력하는 명령어들을 해석하는 해석기(translator)의 역할을 수행합니다. 즉, 사용자는 쉘을 통해 명령어를 입력하고 해당 명령어가 쉘에 의해 해석되어 커널(kernal)로 전달됩니다. 커널에서는 각 명령을 실행하게 되고, 우리는 출력되는 결과를 하드웨어를 통해 확인하게 되는 것입니다.

![https://velog.velcdn.com/images%2Fcataiden%2Fpost%2F5ae3fc1c-e1e2-4585-ac3d-92323536d673%2Fshell.png](https://velog.velcdn.com/images%2Fcataiden%2Fpost%2F5ae3fc1c-e1e2-4585-ac3d-92323536d673%2Fshell.png)

- 위 사진은 터미널을 실행한 뒤, 쉘이 실행된 모습입니다.
- 우리는 윈도우의 cmd, Mac의 bash 등 까만 화면을 자주 접한적이 있습니다. 특히나, Linux를 학습하기 위해서는 터미널과 쉘에 대해 깊게 학습하여야 합니다. Linux 서버 환경에서는 그래픽 유저 인터페이스(GUI)를 제공하지 않는 경우가 일반적이라 터미널과 쉘을 통한 CLI를 사용하여 컴퓨터를 조작하여야 하기 때문입니다.
- 또한, CLI가 입출력 전달이나 개발 환경 구축 및 관리, 서버 관리 등 다양한 점에서 GUI보다 활용도가 높아 다양한 개발 도구들이 CLI 환경을 채택하고 있습니다.

## 정리

> 그렇다면 터미널과 쉘은 어떤 차이가 있을까?
> 
- 결론적으로 터미널 위에 쉘이 실행되는 것입니다. 터미널은 곧 명령을 입력하는 쉘을 실행하기 위한 토대라고 볼 수 있습니다.
- 즉, 터미널이 TV라면 쉘은 방송이고, 우리가 TV를 켬과 동시에 방송이 송출되는 것과 같이 터미널이 실행됨과 동시에 쉘이 실행되어 명령을 입력할 수 있게 되는 것입니다.