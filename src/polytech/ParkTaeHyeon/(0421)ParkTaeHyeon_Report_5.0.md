---
layout: home
---

# VNC(Virtual Network Computing)의 정의

컴퓨터 환경에서 RFB 프로토콜을 이용하여 원격으로 다른 컴퓨터를 제어하는 그래픽 데스크톱 공유 시스템

자판과 마우스 이벤트를 한 컴퓨터에서 다른 컴퓨터로 전송하여 네트워크를 통해 그래픽 화면을 갱신하는 방식

서버와 뷰어로 나뉘게 됨 서버는 원격으로 제어하려는 컴퓨터에 설치, 뷰어는 원격으로 접속하여 제어하는 컴퓨터에 설치

VNC를 사용하면 원격으로 다른 컴퓨터를 제어할 수 있으며 먼 거리에서 작업할 수 있음

이를 통해 서로 다른 위치에 있는 사용자들이 효율적으로 협업할 수 있음

이는 또한 오픈소스이며 Windows, Linux, macOS 등 다양한 운영체제에서 사용할 수 있다.

암호화 기능을 제공하여 보안성을 높일 수 있고 다양한 애플리케이션과 통합되어 사용할 수 있다.

## VNC 프로그램의 종류

### RealVNC

유료 및 무료 버전이 존재하며 크로스 플랫폼(Windows, Mac, Linux)을 지원한다. 또한 AES-256과 같은 강력한 암호화 기술을 제공하여 보안성이 뛰어나다.

- AES-256은 대칭키 암호화 알고리즘 중 하나로 동일한 키를 사용하여 암호화 및 복호화를 수행, AES-256은 블록 암호화 방식으로 데이터를 128비트 블록으로 분할하여 암호화함
- 크로스 플랫폼은 여러 가지 운영체제 및 하드웨어에서 실행되는 것을 의미함.

![ㅇ](https://help.realvnc.com/hc/article_attachments/360005900258/mceclip0.png)

### TightVNC

무료로 제공되며, Windows, Mac, Linux를 지원한다. 암호화 기술은 RealVNC에 비해 약하나 간단하고 가벼운 프로그램이다.

![ㅇ](https://www.tightvnc.com/screenshots/accesscontrol.png)

### UltraVNC

무료로 제공되며, Windows 전용이다. TightVNC보다 더 강력한 암호화 기술을 제공하며, 파일 전송 기능 또한 있다. 클라이언트는 리눅스도 지원하긴 한다.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/UltraVNC_Viewer.png/300px-UltraVNC_Viewer.png)

### TigerVNC

무료로 제공되며, Linux전용이다. 기존 VNC 프로그램에 비해 더 빠른 속도와 높은 화질을 제공한다.

![](https://hackware.ru/wp-content/uploads/2020/05/tigervnc-server-2.png)

### TurboVNC

무료로 제공되며, Linux전용이다. TigerVNC와 비슷한 기능을 제공하지만 OpenGL 그래픽 지원이 가능하며 다른 VNC 클라이언트와 연동이 용이하다.

- OpenGL : 컴퓨터 게임, 가상 현실 등 2D 및 3D 그래픽을 지원하는 크로스 플랫폼 그래픽 API이다.

![](https://filecr.com/_next/image/?url=https%3A%2F%2Fmedia.imgcdn.org%2Frepo%2F2023%2F03%2Fturbovnc%2Fturbovnc-free-download-01.jpg&w=1080&q=75)